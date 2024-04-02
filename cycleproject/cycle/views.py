from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.views.generic import ListView,CreateView,DetailView
from .models import (Cycle,Frame,Wheel,Shoe,Wea,Pantsu,CycleReview,FrameReview,WheelReview,
                     Pedal,Hundle,Brake,BrakeReview,PedalReview,HundleReview,Select)
from .forms import YourInputForm

def your_view(request):
    existing_instance = get_object_or_404(Select)

    if request.method == 'POST':
        form = YourInputForm(request.POST)
        if form.is_valid():
            # フォームのデータを取得
            title = form.cleaned_data['title']
            thumbnail = form.cleaned_data['thumbnail']

            # 別のモデルにデータを保存
            existing_instance.title = title
            existing_instance.thumbnail = thumbnail
            existing_instance.save()

            # リダイレクトや他のアクションを行う
            return redirect('cycle/select.html')
    else:
        form = YourInputForm()

    return render(request, 'cycle/select.html', {'form': form,'existing_instance':existing_instance})

class ToppageView(ListView):
    template_name = 'cycle/index.html'
    ranking_list = Cycle.objects.annotate(avg_rating=Avg('cyclereview__rate')).order_by('-avg_rating')
    new_list = Cycle.objects.order_by('-id')
    beginner_list = Cycle.objects.order_by('price')
    model = Cycle
    price_rate = Cycle.objects.values('price_rate')
    weight_rate = Cycle.objects.values('weight_rate')
    gire_rate = Cycle.objects.values('gire_rate')
    brake_rate = Cycle.objects.values('brake_rate')
    frame_rate = Cycle.objects.values('frame_rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ranking_list'] = ToppageView.ranking_list
        context['new_list'] = ToppageView.new_list
        context['beginner_list'] = ToppageView.beginner_list
        return context
    

class MainpageView(ListView):
    template_name = 'cycle/index.html'
    ranking_list = Cycle.objects.annotate(avg_rating=Avg('cyclereview__rate')).order_by('-avg_rating')
    new_list = Cycle.objects.order_by('-id')
    beginner_list = Cycle.objects.order_by('price')
    model = Cycle
    price_rate = Cycle.objects.values('price_rate')
    weight_rate = Cycle.objects.values('weight_rate')
    gire_rate = Cycle.objects.values('gire_rate')
    brake_rate = Cycle.objects.values('brake_rate')
    frame_rate = Cycle.objects.values('frame_rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ranking_list'] = ToppageView.ranking_list
        context['new_list'] = ToppageView.new_list
        context['beginner_list'] = ToppageView.beginner_list
        return context

class FramepageView(ListView):
    template_name = 'cycle/frame.html'
    model = Frame

class WheelpageView(ListView):
    template_name = 'cycle/wheel.html'
    model = Wheel

class OtherpageView(ListView):
    template_name = 'cycle/other.html'
    context_object_name = 'shoe_list'
    model = Shoe

    def get_context_data(self, **kwargs):
        context = super(OtherpageView, self).get_context_data(**kwargs)
        context.update({
            'wea_list': Wea.objects.all(),
            'pantsu_list': Pantsu.objects.all(),
        })
        return context

    def get_queryset(self):
        return Shoe.objects.all()

class CustomizepageView(ListView):
    template_name = 'cycle/customize.html'
    model = Cycle

class MainDetailView(DetailView):
    template_name = 'cycle/main_detail.html'
    model = Cycle

class MainReviewView(LoginRequiredMixin,CreateView):
    template_name = 'cycle/main_review.html'
    model = CycleReview
    fields = ('cycle','title','text','rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cycle'] = Cycle.objects.get(pk=self.kwargs['cycle_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main-detail',kwargs={'pk':self.object.cycle.id})

class FrameDetailView(DetailView):
    template_name = 'cycle/frame_detail.html'
    model = Frame

class FrameReviewView(LoginRequiredMixin,CreateView):
    template_name = 'cycle/frame_review.html'
    model = FrameReview
    fields = ('frame','title','text','rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['frame'] = Frame.objects.get(pk=self.kwargs['frame_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('frame-detail',kwargs={'pk':self.object.frame.id})
    

class WheelDetailView(DetailView):
    template_name = 'cycle/wheel_detail.html'
    model = Wheel

class WheelReviewView(LoginRequiredMixin,CreateView):
    template_name = 'cycle/wheel_review.html'
    model = WheelReview
    fields = ('wheel','title','text','rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wheel'] = Wheel.objects.get(pk=self.kwargs['wheel_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('wheel-detail',kwargs={'pk':self.object.wheel.id})

class OthershoeDetailView(DetailView):
    template_name = 'cycle/othershoe_detail.html'
    model = Shoe

class OtherweaDetailView(DetailView):
    template_name = 'cycle/otherwea_detail.html'
    model = Wea

class OtherpantsuDetailView(DetailView):
    template_name = 'cycle/otherpantsu_detail.html'
    model = Pantsu

class CycleSearch(ListView):
    model = Cycle
    template_name = 'cycle/main_list.html'

    def get_queryset(self):
        title = self.request.GET.get('title', None)
        if title:
            return Cycle.objects.filter(bike_name__icontains=title)
        else:
            return Cycle.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.request.GET.get('title', '')
        return context
    
class PedalpageView(ListView):
    model = Pedal
    template_name = 'cycle/pedal_list.html'

class BrakepageView(ListView):
    model = Brake
    template_name = 'cycle/brake_list.html'

class HundlepageView(ListView):
    model = Hundle
    template_name = 'cycle/hundle_list.html'

class PedalDetailView(DetailView):
    template_name = 'cycle/pedal_detail.html'
    model = Pedal

class HundleDetailView(DetailView):
    template_name = 'cycle/hundle_detail.html'
    model = Hundle

class BrakeDetailView(DetailView):
    template_name = 'cycle/brake_detail.html'
    model = Brake

class PedalReviewView(LoginRequiredMixin,CreateView):
    template_name = 'cycle/pedal_review.html'
    model = PedalReview
    fields = ('pedal','title','text','rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedal'] = Pedal.objects.get(pk=self.kwargs['pedal_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pedal-detail',kwargs={'pk':self.object.pedal.id})
    
class HundleReviewView(LoginRequiredMixin,CreateView):
    template_name = 'cycle/hundle_review.html'
    model = HundleReview
    fields = ('hundle','title','text','rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hundle'] = Hundle.objects.get(pk=self.kwargs['hundle_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('hundle-detail',kwargs={'pk':self.object.hundle.id})
    
class BrakeReviewView(LoginRequiredMixin,CreateView):
    template_name = 'cycle/brake_review.html'
    model = BrakeReview
    fields = ('brake','title','text','rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brake'] = Brake.objects.get(pk=self.kwargs['brake_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('brake-detail',kwargs={'pk':self.object.brake.id})
    
class FrameListView(ListView):
    template_name = 'cycle/frame_list.html'
    model = Frame

class WheelListView(ListView):
    template_name = 'cycle/wheel_list.html'
    model = Wheel

class SelectpageView(ListView):
    template_name = 'cycle/select.html'
    model = Select