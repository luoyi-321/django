from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Person

all_person = Person.objects.all()
# Create your views here.
def index(request):
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")

def person(request,person_id):
    one_person = None
    try:
        one_person = [p for p in all_person if p.id ==person_id][0]
    except IndexError:
        pass    
    context={"person":one_person}
    return render(request,'person.html',context)