from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import *


def index(request):
    context = {
        "notes" : Note.objects.all()
    }
    return render(request,"index.html",context)

def post_new_note(request):
    body = request.POST['new_note']
    Note.objects.create(body=body)
    return redirect('/') 