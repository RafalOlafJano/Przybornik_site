from django.shortcuts import render

# Create your views here.
def post_login(request):

	return render(request, 'registration/login.html', {})

#def post_loggedout(request):
#
#	return render(request, 'registration/logged_out.html', {})