from django.db import models

TIER = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
SCORE_CHOICES = [
    ('★', '★'),
    ('★★', '★★'),
    ('★★★', '★★★'),
    ('★★★★', '★★★★'),
    ('★★★★★', '★★★★★'),
]
RATE_CHOICES = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]

class Cycle(models.Model):
    title = models.CharField(max_length=100)
    bike_thumnail = models.ImageField()
    bike_name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_rate = models.IntegerField(verbose_name="値段",choices=TIER)
    weight_rate = models.IntegerField(verbose_name="重さ",choices=TIER)
    gire_rate = models.IntegerField(verbose_name="ギア",choices=TIER)
    brake_rate = models.IntegerField(verbose_name="ブレーキ",choices=TIER)
    frame_rate = models.IntegerField(verbose_name="フレーム",choices=TIER)

class Frame(models.Model):
    title = models.CharField(max_length=100)
    bike_thumnail = models.ImageField()
    bike_name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    weight_rate = models.CharField("重さ",choices=SCORE_CHOICES,max_length=100)
    strength_rate = models.CharField("強度",choices=SCORE_CHOICES,max_length=100)

class Wheel(models.Model):
    title = models.CharField(max_length=100)
    bike_thumnail = models.ImageField()
    bike_name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    weight_rate = models.CharField("重さ",choices=SCORE_CHOICES,max_length=100)
    tire_rate = models.CharField("タイヤ幅",choices=SCORE_CHOICES,max_length=100)

class Shoe(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField()
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    kotei_rate = models.CharField("固定力",choices=SCORE_CHOICES,max_length=100)
    himo_rate = models.CharField("靴紐のしやすさ",choices=SCORE_CHOICES,max_length=100)

class Wea(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField()
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    air_rate = models.CharField("空気抵抗",choices=SCORE_CHOICES,max_length=100)
    cold_rate = models.CharField("防寒性",choices=SCORE_CHOICES,max_length=100)

class Pantsu(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField()
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    air_rate = models.CharField("空気抵抗",choices=SCORE_CHOICES,max_length=100)
    hait_rate = models.CharField("衝撃吸収",choices=SCORE_CHOICES,max_length=100)

class Pedal(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField()
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    menseki_rate = models.CharField("面積",choices=SCORE_CHOICES,max_length=100)
    weight_rate = models.CharField("軽さ",choices=SCORE_CHOICES,max_length=100)

class Brake(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField()
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    seinou_rate = models.CharField("性能",choices=SCORE_CHOICES,max_length=100)
    taikyu_rate = models.CharField("耐久性",choices=SCORE_CHOICES,max_length=100)

class Hundle(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField()
    price = models.IntegerField()
    price_rate = models.CharField("値段",choices=SCORE_CHOICES,max_length=100)
    haba_rate = models.CharField("幅",choices=SCORE_CHOICES,max_length=100)
    drop_rate = models.CharField("ドロップ",choices=SCORE_CHOICES,max_length=100)

class Custo(models.Model):
    frame = models.ForeignKey(Frame,on_delete=models.CASCADE,null=True,blank=True)
    wheel = models.ForeignKey(Wheel,on_delete=models.CASCADE,null=True,blank=True)
    pedal = models.ForeignKey(Pedal,on_delete=models.CASCADE,null=True,blank=True)
    brake = models.ForeignKey(Brake,on_delete=models.CASCADE,null=True,blank=True)
    hundle = models.ForeignKey(Hundle,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

class CycleReview(models.Model):
    cycle = models.ForeignKey(Cycle,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class FrameReview(models.Model):
    frame = models.ForeignKey(Frame,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class WheelReview(models.Model):
    wheel = models.ForeignKey(Wheel,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class PedalReview(models.Model):
    pedal = models.ForeignKey(Pedal,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class BrakeReview(models.Model):
    brake = models.ForeignKey(Brake,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class HundleReview(models.Model):
    hundle = models.ForeignKey(Hundle,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Select(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)