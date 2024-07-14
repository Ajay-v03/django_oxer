from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def aboutus(request):
    return render (request,"about.html")

def blog(request):
    return render(request,"blog.html")

def class_type(request):
    return render(request,"class.html")

# GET Method example
def form(request):
    full_name = ''
    try:
        first_name = request.GET['fname']
        last_name = request.GET['lname']
        full_name = first_name + ' ' + last_name
    except:
        pass
    print(full_name)
    return render(request,"form.html",{'output':full_name})