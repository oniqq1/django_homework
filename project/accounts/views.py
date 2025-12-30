from django.http import HttpRequest , HttpResponse
from django.shortcuts import render, redirect
from .forms import UserCreatingForm , AuthForm
from django.contrib.auth import login , authenticate


def sign_up(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreatingForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index' )
        else:
            pass
    form = UserCreatingForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

def log_in(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')

            form.add_error(None , "Invalid username or password")
            return render(request, 'accounts/log_in.html', {'form': form})

        else:
            pass

    form = AuthForm()
    return render(request, 'accounts/log_in.html', {'form': form})