from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect

def home(request):
    return render(request,"index.html")

def aboutus(request):
    return render (request,"about.html")

def blog(request):
    return render(request,"blog.html")

def class_type(request):
    return render(request,"class.html")

def thanks(request):
    if request.method == "GET":
        output = request.GET.get('fullname')
    return render(request,"thanks.html",{'fullname':output})

def calculator(request):
    return render(request,"calculator.html")

def evenOdd(request):
    result = ''
    if request.method=='POST':
        number = eval(request.POST.get('number'))
        if number%2==0:
            result = "Even"
        else:
            number = "Noo"
    return render(request,"even_odd.html",{'result':result})

def marksheet(request):
    result = {}
    if request.method=='POST':
        english = eval(request.POST.get('subject1'))
        hindi = eval(request.POST.get('subject2'))
        phy = eval(request.POST.get('subject3'))
        chem = eval(request.POST.get('subject4'))
        math = eval(request.POST.get('subject5'))

        total = english+hindi+phy+chem+math
        print(total)
        percentage = int(total*100/500)
        print(percentage)
        if percentage>60:
            division = "First"
        elif percentage>48:
            division = "Second"
        elif percentage>33:
            division = "Third"
        else:
            division = "Fail"

        result['total'] = total
        result['percentage'] = percentage
        result['division'] = division
        
        return render(request,"marksheet.html",result)
    return render(request,"marksheet.html")

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
        url = "/thanks.html?fullname={}".format(full_name)
        return HttpResponseRedirect(url)
        # return redirect(url)
    except:
        pass
    print(data)
    return render(request,"form.html",data)
