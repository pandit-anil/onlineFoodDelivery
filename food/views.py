from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# class Index(View):
#     def get(self,request):
#         return render(request,'about.html')


class Index(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Book(TemplateView):
    template_name = 'book.html'

class Menu(TemplateView):
    template_name = 'menu.html'
