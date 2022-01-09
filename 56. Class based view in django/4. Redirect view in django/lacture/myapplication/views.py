from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.

class RajaRedirectView(RedirectView):
    url='/'

class PraveenRedirectView(RedirectView):
    pattern_name='root'
    permanent=True
    # query_string=False
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)


