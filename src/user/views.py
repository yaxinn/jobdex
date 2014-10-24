from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from card.models import *
from user.models import *
from django.core import serializers

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        if not username or not password or not confirm_password or not email:
            error_message = "Please fill in all fields."
        elif password and password != confirm_password:
            error_message = "Passwords don't match"
        elif UserProfile.objects.filter(user=username).exists():
            error_message = "User already exsits"
        else:
            user_form = UserForm(data=request.POST)
                if user_form.is_valid():
                    user = user_form.save()
                    user.set_password(user.password)
                    user.save()
                    u = authenticate(username=username, password=password)
                    login(request, u)
                    username_output = serializers.serialize("json", user.username)
                    return JsonResponse(username_output, safe=False)
                    #return HttpResponseRedirect('/')
                else:
                    error_message = user_form.errors.items()[0][1]
    else:
        error_message = None
    context = {'error_message': error_message}
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None and user.is_active:
            login(request, user)
        return redirect('home')
    else:
        return redirect('home')

@login_required
def logout_view(request):
    logout(request)
        return redirect('home')
