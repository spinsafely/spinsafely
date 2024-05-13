from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Casino(models.Model): 
    name = models.CharField(max_length=200) 
    slug = models.SlugField(unique=True)
    small_description = models.TextField(null=True, blank=True)
    description = RichTextField()
    pros = models.TextField(null=True, blank=True, verbose_name='Artılar')
    cons = models.TextField(null=True, blank=True, verbose_name='Eksiler')
    reliable = models.FloatField(null=True, blank=True, verbose_name='Güvenilirlik', default=4.95)
    payment_speed = models.FloatField(null=True, blank=True, verbose_name='Ödeme Hızı', default=4.95)
    support = models.FloatField(null=True, blank=True, verbose_name='Destek', default=4.95)
    playable = models.FloatField(null=True, blank=True, verbose_name='Oynanabilirlik ve Kalite', default=4.95)
    bonusses = models.FloatField(null=True, blank=True, verbose_name='Bonus ve Promosyon', default=4.95)
    url = models.URLField()
    img = models.ImageField(upload_to='')
    sort = models.IntegerField(default=0)
  
    def __str__(self): 
        return self.name

class AdminReview(models.Model):
    casino = models.ForeignKey('Casino', on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    guarantee_support = models.BooleanField(default=False)
    point = models.FloatField()

class Bonus(models.Model):
    casino = models.ForeignKey('Casino', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    promo_code = models.CharField(max_length=50, blank=True, null=True, default='-')
    description = models.TextField(blank=True, null=True)

    def __str__(self): 
        return self.casino.name + ' - ' + self.title


class GameAccount(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

STATUS_CHOICES = {
    (1, "Onaylandı"),
    (2, "Onaylanmadı"),
    (3, "Beklemede"),
}

class GameDeposit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    amount = models.FloatField(default=0)
    trc20 = models.TextField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + str(self.amount)

class GameWithdrawal(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    amount = models.FloatField(default=0)
    trc20 = models.TextField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + str(self.amount)