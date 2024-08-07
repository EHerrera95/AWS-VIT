from django.shortcuts import redirect, render, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CuresInputForm, CreateUserForm, v3InputForm
from .models import AllLogin, CuresInputModel, Validation, v3InputModel
from django.core.files.storage import FileSystemStorage


import xml.etree.ElementTree as ET
import os.path


# Create your views here.
def changes(request):
    return render(request, "Inputs/changes.html")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            AllLogin.objects.create(user = request.user)
            return redirect('inputsv1')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    return render(request, "Inputs/login.html")   

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, "Inputs/register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'Inputs/home.html')

@login_required(login_url='home')
def inputsv1(request):
    if request.method == 'POST':
        CuresInputModel.objects.all().delete()
        form = CuresInputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('resultsv1')
    else:
        form = CuresInputForm()
    return render(request, "Inputs/inputs-v1.html", {
        'form':form,
    })

@login_required(login_url='home')
def resultsv1(request):
    uploads = CuresInputModel.objects.all()
    crit = uploads[0].criteria

    path_string = uploads[0].filename
    text = str(path_string).lower()
    file_type = text[-4:]
    if file_type != '.xml':
        print('ERROR')
        return redirect('inputs')    #Needs alert to import correct file
    else:
        filepath = f'.//media/{uploads[0].filename}'
        validation = Validation(crit,filepath)
    
    return render(request, "Inputs/results-v1.html", {
        'uploads': uploads,
        'validation': validation,
    })

@login_required(login_url='home')
def inputsv3(request):
    if request.method == 'POST':
        v3InputModel.objects.all().delete()
        form = v3InputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('resultsv3')
    else:
        form = v3InputForm()
    return render(request, "Inputs/inputs-v3.html", {
        'form':form,
    })

@login_required(login_url='home')
def resultsv3(request):
    uploads = v3InputModel.objects.all()
    crit = uploads[0].criteria

    path_string = uploads[0].filename
    text = str(path_string).lower()
    file_type = text[-4:]
    if file_type != '.xml':
        print('ERROR')
        return redirect('inputsv3')    #Needs alert to import correct file
    else:
        filepath = f'.//media/{uploads[0].filename}'
        validation = Validation(crit,filepath)
    
    return render(request, "Inputs/results-v3.html", {
        'uploads': uploads,
        'validation': validation,
    })

# @login_required(login_url='home')
# def inputs(request):
#     if request.method == 'POST':
#         InputModel.objects.all().delete()
#         form = InputForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('results')
#     else:
#         form = InputForm()
#     return render(request, "Inputs/inputs.html", {
#         'form':form,
#     })

# @login_required(login_url='home')
# def results(request):
#     uploads = InputModel.objects.all()
#     crit = uploads[0].criteria

#     path_string = uploads[0].filename
#     text = str(path_string)
#     file_type = text[-4:]
#     if file_type != '.xml':
#         print('ERROR')
#         return redirect('inputs')    #Needs alert to import correct file
#     else:
#         filepath = f'.//media/{uploads[0].filename}'
#         validation = Validation(crit,filepath)
    
#     return render(request, "Inputs/results.html", {
#         'uploads': uploads,
#         'validation': validation,
#     })