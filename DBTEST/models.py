from django.db import models
from  django.utils import timezone
class DBInstance(models.Model):
    '''本地数据库中包含了用户、实例信息,一个用户可以拥有多个实例,一个实例只能由一个用户进行管理'''
    DBInstanceId = models.CharField(max_length=20,null=True)
    DBInstanceName=models.CharField(max_length=20,null=True)
    DBInstanceCreatetime=models.DateTimeField('date published',default=timezone.now,null=True)
    DBInstancestatus=models.CharField(max_length=10,null=True)
    Username=models.CharField(max_length=20,null=True)


# Create your models here.
