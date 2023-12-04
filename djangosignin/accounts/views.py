from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')


# class LoginView(View):
#     def get(self, request):
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('index'))
#
#                 else:
#                     return HttpResponse("Account not active")
#             else:
#                 print("Someone tried to login and failed")
#                 print("username: {} and password {}".format(username, password))
#                 return HttpResponse("Invalid login details supplied")
#         else:
#             return render(request, 'accounts_auth/login.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts_auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('home')
