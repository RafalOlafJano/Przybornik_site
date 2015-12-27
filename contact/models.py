from django.db import models
# -*- coding: utf-8 -*-

# Create your models here.
class Contact(models.Model):
		title = models.CharField(max_length=50)
		project_name = models.CharField(max_length=100)
		author = models.ForeignKey('auth.User')
		telephone = models.CharField(max_length=10)
		email = models.CharField(max_length=50)
		about = models.TextField()
		class Meta:
			db_table = "contact"

		def __str__(self):
			return self.title