from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from DBTEST.models import DBInstance
from DBTEST.forms import  DbinstanceForm
from  django.utils import timezone
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
def showdbinstance(request):
    dbinstanceList=[]
    if request.method=='GET':
        for obj in DBInstance.objects.all():
            dbinstanceDict=model_to_dict(obj)
            dbinstanceList.append(dbinstanceDict)
    return render_to_response('dbinstances/dbinstances.html',{'dbinstanceList':dbinstanceList})
def deletedbinstance(request):
    return render_to_response('dbinstances/dbinstances.html',{'dbinstancedict':dbinstancedict})
def createdbinstance(request):
    if request.method == "POST":
        form=DbinstanceForm(request.POST)
        form.DBInstanceCreatetime=timezone.now()
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('showdbinstance'))

def index(request):
    return render_to_response('base.html',{})





