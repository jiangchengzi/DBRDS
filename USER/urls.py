
from django.conf.urls import url
from DBTEST import views

urlpatterns = [
    url(r'^createuser', views.showdbinstance,name='managedbinstance'),
    url(r'^$', views.index, name='index'),
    url(r'^createdbinstance',views.createdbinstance,name="createdbinstance"),
    url(r'^deletedbinstance',views.deletedbinstance,name="deletedbinstance"),
]