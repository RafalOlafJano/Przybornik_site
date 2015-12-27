from django.db import models
from django.utils import timezone

#from django.contrib.auth.models.User import AnonymousUser
from django.contrib.auth.models import User

# -*- coding: utf-8 -*-

# Create your models here.
class WypelnionaAnkieta(models.Model):
    odp1 = models.BooleanField()
    odp2 = models.BooleanField()
    odp3 = models.BooleanField()
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField( default = timezone.now )
    published_date = models.DateTimeField( blank = True, null=True )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Meta:
    db_table = "pollster"