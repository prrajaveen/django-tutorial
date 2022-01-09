from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name='myapplication/home.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Sonam'
        context['roll']=101
        # <----if your pass context in the form of dictionary then extra context cannt pass through url.py----->
        # context={'name':'sonam','roll':101}
        # <------------- kwargs contain dynamic url value in the form of dictionary --------------->
        print(kwargs)
        print(context)
        return context
        