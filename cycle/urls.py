from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToppageView.as_view(),name='index'),
    path('main/',views.MainpageView.as_view(),name='main'),
    path('frame/',views.FramepageView.as_view(),name='frame'),
    path('wheel/',views.WheelpageView.as_view(),name='wheel'),
    path('other/',views.OtherpageView.as_view(),name='other'),
    path('customize/',views.CustomizepageView.as_view(),name='customize'),
    path('main/<int:pk>/detail',views.MainDetailView.as_view(),name='main-detail'),
    path('main/<int:cycle_id>/review',views.MainReviewView.as_view(),name="main-review"),
    path('frame/<int:pk>/detail',views.FrameDetailView.as_view(),name='frame-detail'),
    path('frame/<int:frame_id>/review',views.FrameReviewView.as_view(),name="frame-review"),
    path('wheel/<int:pk>/detail',views.WheelDetailView.as_view(),name='wheel-detail'),
    path('wheel/<int:wheel_id>/review',views.WheelReviewView.as_view(),name="wheel-review"),
    path('othershoe/<int:pk>/detail',views.OthershoeDetailView.as_view(),name='othershoe-detail'),
    path('otherwea/<int:pk>/detail',views.OtherweaDetailView.as_view(),name='otherwea-detail'),
    path('otherpantsu/<int:pk>/detail',views.OtherpantsuDetailView.as_view(),name='otherpantsu-detail'),
    path('cycle_search/', views.CycleSearch.as_view(), name='cycle_search'), 
    path('pedal/',views.PedalpageView.as_view(),name='pedal'),
    path('brake/',views.BrakepageView.as_view(),name='brake'),
    path('hundle/',views.HundlepageView.as_view(),name='hundle'),
    path('pedal/<int:pk>/detail',views.PedalDetailView.as_view(),name='pedal-detail'),
    path('brake/<int:pk>/detail',views.BrakeDetailView.as_view(),name='brake-detail'),
    path('hundle/<int:pk>/detail',views.HundleDetailView.as_view(),name='hundle-detail'),
    path('pedal/<int:pedal_id>/review',views.PedalReviewView.as_view(),name='pedal-review'),
    path('brake/<int:brake_id>/review',views.BrakeReviewView.as_view(),name='brake-review'),
    path('hundle/<int:hundle_id>/review',views.HundleReviewView.as_view(),name='hundle-review'),
    path('frame_list/',views.FrameListView.as_view(),name='frame-list'),
    path('wheel_list/',views.WheelListView.as_view(),name='wheel-list'),
    path('select/',views.SelectpageView.as_view(),name='select'),
    path('selecton',views.your_view,name="your_view"),
]