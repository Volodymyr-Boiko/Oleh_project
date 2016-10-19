from django.shortcuts import render
from django.http import HttpResponse

def user_info(request):
    return HttpResponse('<h1>Hello User</h1>')
