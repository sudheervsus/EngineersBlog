from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from accounts import forms
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.views.generic import CreateView
# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return redirect('blog:topic_list')

class UserSignUpView(CreateView):
    model = User
    form_class = forms.UserSignUPForm
    success_url = reverse_lazy('accounts:login')
    template_view = 'accounts/signup.html'

def user_login(request):

    if request.method == 'POST':
        # print("---------------In POST")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # print("---------------Authenticated")
            if user.is_active:
                # print("---------------Active")
                login(request, user)
                return redirect('blog:topic_list')
            else:
                return HttpResponseBadRequest('Account Not Activated.')
        else:
            return HttpResponse('Invalid Login Details')
    return render(request, 'accounts/login.html')
