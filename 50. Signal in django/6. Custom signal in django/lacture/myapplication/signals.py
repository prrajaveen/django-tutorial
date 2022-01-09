from django.dispatch import Signal,receiver
# <======== Creating a Signal=============>
notification=Signal(providing_args=['request','user'])

# Receiver function
@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(f'{kwargs}')
    print('notification')