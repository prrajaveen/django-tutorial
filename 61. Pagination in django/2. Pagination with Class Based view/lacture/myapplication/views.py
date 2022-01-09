from django.http.response import Http404
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.

class Home(ListView):
    model=Post
    template_name='myapplication/home.html'
    ordering=['id']
    paginate_by= 3
    paginate_orphans=1
######################## Exception Http404 ############################
    # def get_context_data(self,*args, **kwargs):
    #     try:
    #         return super(Home,self).get_context_data(*args,**kwargs)
    #     except Http404:
    #         self.kwargs['page']=1
    #         return super(Home,self).get_context_data(*args,**kwargs)

####################### Another Way ##########################
    def paginate_queryset(self, queryset, page_size):
        try:
            return super(Home,self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page']=1
            return super(Home,self).paginate_queryset(queryset, page_size)



class PostDetailView(DetailView):
    model=Post
    template_name='myapplication/detail.html'