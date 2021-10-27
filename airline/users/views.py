from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	else:
		return render(request, "users/users.html")

		 
def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "users/login.html", {
			"message": "Invalid credentials."
			})
			
	else:
		return render(request, "users/login.html", {
			"message": "Enter credentials."
		})

def logout_view(request):
	logout(request)
	return render(request, "users/login.html" , {
		"message": "logged out."
	})