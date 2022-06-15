from asyncio.log import logger
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, FormView, TemplateView, CreateView
from .forms import NewUserForm, AddDate
# , AddCart
from . import models
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")




class GaghaparListView(ListView):
    template_name = 'home.html'

    def get(self,request):
        tours = models.Gaghapar.objects.all()
        HomeBG_list = models.HomeBG.objects.all()
        return render(request, self.template_name, {'tours' : tours, 'HomeBG_list':HomeBG_list})

class GaghaparDetailView(DetailView):
    template_name = 'home_detail.html'

    def get(self,request, id):
        tour = models.Gaghapar.objects.get(pk=id)
        return render(request, self.template_name, {'tour' : tour})


def add_post(request):
	form = AddDate()
	if request.method == 'POST':
		form = AddDate(request.POST)
		if form.is_valid():
			form.save()
			context = {'form':form}
			return redirect('post_detail')
		else:
			form = AddDate()
			context = {'form':form}
	else:
		form = AddDate()
		context = {'form':form}
	return render(request, 'home.html', context)

def post_detail(request):
	dates = models.Date1.objects.all()
	return render(request, 'post_detail.html', {'dates':dates})


# def add_post(request):
# 	form = AddCart()
# 	if request.method == 'POST':
# 		form = AddCart(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			context = {'form':form}
# 			return redirect('post_detail')
# 		else:
# 			form = AddCart()
# 			context = {'form':form}
# 	else:
# 		form = AddCart()
# 		context = {'form':form}
# 	return render(request, 'add_post.html', context)

# def post_detail(request):
# 	carts = UserCarts.objects.all()
# 	return render(request, 'post_detail.html', {'carts':carts})


# class UserPageListView(ListView):
#     template_name = 'userpage.html'

#     def get(self, request):
#         users = NewUserForm(request.POST)

#         return render(request, self.template_name, {'users':users, 'form':form})








