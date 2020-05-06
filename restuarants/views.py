from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
#function based view

def home_old(request):
    html_var = 'f string'
    html_ = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
</head>
<body>
   <h1> Hello world !</h1>
   <p>This is {html_var} coming through</p>
</body>
</html>"""
    return HttpResponse(html_)

def home(request):
    num = None
    some_list = [
        random.randint(0,10000000),
        random.randint(0,10000000),
        random.randint(0,10000000)
    ]
    condition_bool_item = False
    if condition_bool_item :
        num = random.randint(0,10000000)
    context = {
        'num' : num,
        'some_list': some_list
    }
    return render(request,'home.html',context)

def about(request):
    context = {
    }
    return render(request,'about.html',context)

def contact(request):
    context = {
    }
    return render(request,'contact.html',context)

