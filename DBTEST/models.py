from django.db import models
from  django.utils import timezone
class DBInstance(models.Model):
    DBInstanceId = models.CharField(max_length=20,null=True)
    DBInstanceName=models.CharField(max_length=20,null=True)
    DBInstanceCreatetime=models.DateTimeField('date published',default=timezone.now,null=True)
    DBInstancestatus=models.CharField(max_length=10,null=True)
# Create your models here.
