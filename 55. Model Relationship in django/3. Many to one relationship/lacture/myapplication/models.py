from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
# Create your models here.

class Post(models.Model):
    # user=models.ForeignKey(User,on_delete=CASCADE)
    # user=models.ForeignKey(User,on_delete=PROTECT)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title=models.CharField(max_length=80)
    post_category=models.CharField(max_length=70)
    post_publish_date=models.DateField()
