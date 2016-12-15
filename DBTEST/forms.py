#添加表单类
from django import forms
from DBTEST.models import DBInstance
class DbinstanceForm(forms.ModelForm):
    class Meta:
        model=DBInstance
        # fields=["DBInstanceId"]
        fields=["DBInstanceId", "DBInstanceName", "DBInstancestatus"]