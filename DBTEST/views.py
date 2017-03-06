from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from DBTEST.models import DBInstance
from DBTEST.forms import  DbinstanceForm
from  django.utils import timezone
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from .ClientRequest import ClientRequest

def showdbinstance(request,url=''):
    dbinstanceList=[]
    if request.method=='GET':
        for obj in DBInstance.objects.all():
            dbinstanceDict=model_to_dict(obj)
            dbinstanceList.append(dbinstanceDict)
    return render_to_response('dbinstances/dbinstances.html',{'dbinstanceList':dbinstanceList})

def deletedbinstance(request):
    dbinstanceid=request.GET.get('DBInstanceId')
    deldbinstanceObj=DBInstance.objects.filter(DBInstanceId=dbinstanceid).delete()
    return HttpResponse('删除成功')


def createdbinstance(request):
    if request.method == "POST":
        form=DbinstanceForm(request.POST)
        form.DBInstanceCreatetime=timezone.now()
        if form.is_valid():
            form.save()
    client=ClientRequest(request)
    print(client.do_action())
    return HttpResponseRedirect(reverse('managedbinstance'))

def index(request):
    return render_to_response('../templates/base.html',{})



def Login(request):
    """登录界面"""
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'GET':
        return render_to_response('login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # c = {}
                    # c.update(csrf(request))
                    # request.session['csrf_token'] = str(c.get('csrf_token'))
        # user_filter = User.objects.filter(username=username)
        # if user_filter:
        #     user = user_filter[0]
        #     if PyCrypt.md5_crypt(password) == user.password:
        #         request.session['user_id'] = user.id
        #         user_filter.update(last_login=datetime.datetime.now())
                    if user.role == 'SU':
                        request.session['role_id'] = 2
                    elif user.role == 'GA':
                        request.session['role_id'] = 1
                    else:
                        request.session['role_id'] = 0
                    return HttpResponseRedirect(request.session.get('pre_url', '/'))
                # response.set_cookie('username', username, expires=604800)
                # response.set_cookie('seed', PyCrypt.md5_crypt(password), expires=604800)
                # return response
                else:
                    error = '用户未激活'
            else:
                error = '用户名或密码错误'
        else:
            error = '用户名或密码错误'
    return render_to_response('login.html', {'error': error})
