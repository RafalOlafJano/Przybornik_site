# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class TimeTable(models.Model):

	day = models.CharField(max_length=15)
	month = models.CharField(max_length=25)
	year = models.CharField(max_length=4)

	hour = models.CharField(max_length=2)
	minute = models.CharField(max_length=2)

	text = models.TextField()

	created_date = models.DateTimeField( default = timezone.now )
	published_date = models.DateTimeField( blank = True, null=True )

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Meta:
    db_table = "timetable"