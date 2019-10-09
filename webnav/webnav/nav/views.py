from django.shortcuts import render
from django.views import View
# Create your views here.

class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'welcome.html')


class About(View):

    def get(self, request, *args, **kwargs):
        return render(request,'about.html')
    
class Test(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html')

class Testing(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'testing.html')
    
class minimize(View):
    
    def get(self,request,*args, **kwargs):
        return render(request, 'minimize.html')