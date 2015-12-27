# coding=UTF-8
from django.shortcuts import render
from .models import Contact
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):

	#user = get_user_model()
	user = User.objects.get(username= u'Rafał-admin')
	query = Contact.objects.filter( author= user)
	return render(request, 'contact/post_list.html', {'query': query})