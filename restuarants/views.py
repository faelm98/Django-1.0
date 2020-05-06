from django.shortcuts import render
from django.http import HttpResponse
import random

from django.views import View
from django.views.generic import TemplateView
# Create your views here.
#function based view

# def home_old(request):
#     html_var = 'f string'
#     html_ = f"""
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Django</title>
# </head>
# <body>
#    <h1> Hello world !</h1>
#    <p>This is {html_var} coming through</p>
# </body>
# </html>"""
#     return HttpResponse(html_)

# def home(request):
#     num = None
#     some_list = [
#         random.randint(0,10000000),
#         random.randint(0,10000000),
#         random.randint(0,10000000)
#     ]
#     condition_bool_item = False
#     if condition_bool_item :
#         num = random.randint(0,10000000)
#     context = {
#         'num' : num,
#         'some_list': some_list
#     }
#     return render(request,'home.html',context)

# def about(request):
#     context = {
#     }
#     return render(request,'about.html',context)

# def contact(request):
#     context = {
#     }
#     return render(request,'contact.html',context)



# class ContactView(View) :
#     def get(self,request, *args, ** kwargs):
#         context = {
#         }
#         return render(request,'contact.html',context)
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,*args,**kwargs):
        context = super(HomeView,self).get_context_data(*args,**kwargs)
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
        return context

# class AboutView(TemplateView):
#     template_name = 'about.html'
# class ContactView(TemplateView):
#     template_name = 'contact.html'