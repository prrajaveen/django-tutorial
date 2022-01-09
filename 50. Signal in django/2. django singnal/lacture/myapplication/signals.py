from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.models.signals import pre_migrate,post_migrate
from django.db.backends.signals import connection_created
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.http.response import HttpResponse

#===> Go to app.py file and write ready() method
#===> Go to init.py file make some setting, you can set directly to your setting.py file

# <================ it run After user are Logged In ======================>
@receiver(user_logged_in,sender=User)
def at_login_in(sender,request,user,**kwargs):
    print('\n\n')
    print('<==================== Login Secussfull ======================>')
    print('Sender :',sender)
    print('Request :',request)
    print('User :',user)
    print('user pasword :',user.password)
    print(f'kwargs: {kwargs}')
    print('<==============================================>') 
    print('\n') 
# user_logged_in.connect(login_in,sender=User)
# <=========================================================================>


# <================ it Run After the User Logged Out =========================>
@receiver(user_logged_out,sender=User)
def at_login_out(sender,request,user,**kwargs):
    print('\n\n')
    print('<================== Logout Secussful =======================>')
    print('Sender :',sender)
    print('Request :',request)
    print('User :',user)
    print('user pasword :',user.password)
    print(f'kwargs: {kwargs}')
    print('<===========================================================>')
    print('\n') 
# user_logged_out.connect(login_out,sender=User)
# ==============================================================================>


# <================ It run When User Failed to login =========================>
@receiver(user_login_failed)
def at_login_failed(sender,request,credentials,**kwargs):
    print('\n\n')
    print('<==================== Login Failed ======================>')
    print('Sender :',sender)
    print('Request :',request)
    print('credentials:',credentials)
    print(f'kwargs: {kwargs}')
    print('<=======================================================>')
    print('\n') 
# user_login_failed=(login_failed)
# <==============================================================================>



# <=============== It will run before save method call =============================>
@receiver(pre_save,sender=User)
def at_pre_save(sender,instance,**kwargs):
    print('\n\n')
    print('<==================== Detail Save (Pre save signal) ======================>')
    print('Sender :',sender)
    print('instance:',instance)
    print(f'kwargs: {kwargs}')
    print('<=========================================================================>')
    print('\n') 
#<====================================================================================>



#<===================== It will run after save method call ==============================>
@receiver(post_save,sender=User)
def at_post_save(sender,instance,created,**kwargs):
    if created:
        print('\n\n')
        print('<==================== New record create (post save signal) ======================>')
        print('Sender :',sender)
        print('instance:',instance)
        print('created :',created)
        print(f'kwargs: {kwargs}')
        print('<================================================================================>')
        print('\n') 
    else:
        print('\n\n')
        print('<==================== Update record (Post save signal) ======================>')
        print('Sender :',sender)
        print('instance:',instance)
        print('created :',created)
        print(f'kwargs: {kwargs}')
        print('<===========================================================================>')
        print('\n') 

#<=======================================================================================>




# <=============== It will run before delete method call =============================>
@receiver(pre_delete,sender=User)
def at_pre_delete(sender,instance,**kwargs):
    print('\n\n')
    print('<==================== Detail Deleted (pre delete signal) ======================>')
    print('Sender :',sender)
    print('instance:',instance)
    print(f'kwargs: {kwargs}')
    print('<=================================================>')
    print('\n') 
#<====================================================================================>


# <=============== It will run after delete method call =============================>
@receiver(post_delete,sender=User)
def at_post_delete(sender,instance,**kwargs):
    print('\n\n')
    print('<==================== Detail Deleted (Post delete signal) ======================>')
    print('Sender :',sender)
    print('instance:',instance)
    print(f'kwargs: {kwargs}')
    print('<================================================================================>')
    print('\n') 
#<====================================================================================>



# <=============== It will run when the program save in vscode(django model instansiate) =============================>
@receiver(pre_init,sender=User)
def at_pre_init(sender,*args,**kwargs):
    print('\n\n')
    print('<==================== at the very first refresh (pre init signal) ======================>')
    print('Sender :',sender)
    print('args :',args)
    print(f'kwargs: {kwargs}')
    print('<========================================================================================>')
    print('\n') 
#<====================================================================================>



# <=============== It will run when the program save in vscode(django model instansiate) =============================>
@receiver(post_init,sender=User)
def at_post_init(sender,*args,**kwargs):
    print('\n\n')
    print('<==================== at the very first refresh (Post init signal) ======================>')
    print('Sender :',sender)
    print('args :',args)
    print(f'kwargs: {kwargs}')
    print('<========================================================================================>')
    print('\n') 
#<====================================================================================>




# <=============== It will run whe your doing request =============================>
@receiver(request_started)
def at_request_started(sender,environ,**kwargs):
    print('\n\n')
    print('<==================== when the clint request (request started signal) ======================>')
    print('Sender :',sender)
    print('environ :',environ)
    print(f'kwargs: {kwargs}')
    print('<===========================================================================================>')
    print('\n') 
#<====================================================================================>


# <=============== It will run when the request finished (means when the clint respoce received) =============================>
@receiver(request_finished)
def at_request_finished(sender,**kwargs):
    print('\n\n')
    print('<==================== when the clint receive response (Post init signal) ======================>')
    print('Sender :',sender)
    print(f'kwargs: {kwargs}')
    print('<==============================================================================================>')
    print('\n') 
#<====================================================================================>


# <=============== It will run when the request finished (means when the clint respoce received) =============================>
@receiver(got_request_exception)
def at_got_request_exception(sender,request,**kwargs):
    print('\n\n')
    print('<==================== when throw any exception (got request exception signal) ======================>')
    print('Sender :',sender)
    print('request :',request)
    print(f'kwargs: {kwargs}')
    print('<====================================================================================================>')
    print('\n') 
#<==============================================================================================================================>




# <=============== It will run when migrate command is run (means when the clint respoce received) =============================>
@receiver(pre_migrate)
def at_pre_migrate(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('\n\n')
    print('<==================== It will run when migrate command is run (Pre migrate signal) ======================>')
    print('Sender :',sender)
    print('app config :',app_config)
    print('Verbosity :',verbosity)
    print('Using :',using)
    print('plan :',plan)
    print('apps :',apps)
    print(f'kwargs: {kwargs}')
    print('<==================================================================================================================>')
    print('\n') 
#<==============================================================================================================================>



# <=============== It will run when migrate command is run (means when the clint respoce received) =============================>
@receiver(post_migrate)
def at_post_migrate(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('\n\n')
    print('<==================== It will run when migrate command is run (Post migrate signal) ======================>')
    print('Sender :',sender)
    print('app config :',app_config)
    print('Verbosity :',verbosity)
    print('Using :',using)
    print('plan :',plan)
    print('apps :',apps)
    print(f'kwargs: {kwargs}')
    print('<==================================================================================================================>')
    print('\n') 
#<==============================================================================================================================>



# <=============== It will run when the request finished (means when the clint respoce received) =============================>
@receiver(connection_created)
def at_connection_created(sender,connection,**kwargs):
    print('\n\n')
    print('<==================== when connection of database ======================>')
    print('Sender :',sender)
    print('connection :',connection)
    print(f'kwargs: {kwargs}')
    print('<====================================================================================================>')
    print('\n') 
#<==============================================================================================================================>