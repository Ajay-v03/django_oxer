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

# GET/POST Method example
def form(request):
    data = {}
    try:
        # first_name = request.GET['fname']
        # last_name = request.GET['lname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        full_name = first_name + ' ' + last_name
        data = {
            'fname':first_name,
            'lname':last_name,
            'fullname':full_name
        }
    except:
        pass
    print(data)
    return render(request,"form.html",data)
