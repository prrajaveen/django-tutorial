from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("------- Login Signal ---------")
    print("------------------------------")
    ip=request.META.get('REMOTE_ADDR')
    print('clint_ip',ip)
    request.session['ip']=ip