from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def edit(request):
    return render(request,"edit.html")

def me(request):
    return render(request,"me.html")