from django.shortcuts import render
from django.views import View
from .forms import ContactForm
# Create your views here.


class Home(View):
    def get(self, request):
        context = {'msg': 'This is my Home Page'}
        return render(request, 'myapplication/home.html', context)


class About(View):
    def get(self, request):
        context = {'msg': 'This is my about page'}
        return render(request, 'myapplication/about.html', context)


class Contact(View):
    def get(self, request):
        fm = ContactForm()
        context = {'msg': 'Contact Form', 'form': fm}
        return render(request, 'myapplication/contact.html', context)

    def post(self, request):
        fm = ContactForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            print(name)
            context = {'msg': 'your form has been submitted', 'form': fm}
            return render(request, 'myapplication/contact.html', context)

###############################################################################


class NewsClassView(View):
    def get(self, request):
        context = {'info': 'mazfit is offering great deals and discounts on some of its smartwatches, if you are looking for a budget smartwatch, you can check out the deals. Amazfit has announced that its budget smartwatches including the popular Amazfit GTS 2 Mini, Bip U Pro and BIP U are available with deals and discounts. The smartwatches are available at discounted prices on Amazon, Flipkart and the official website of Amazfit.'}
        return render(request,'myapplication/news.html',context)