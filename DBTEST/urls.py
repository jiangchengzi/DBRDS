
from django.conf.urls import url
from DBTEST import views

urlpatterns = [
    url(r'^managedbinstance', views.showdbinstance,name='managedbinstance'),
    url(r'^$', views.index, name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^createdbinstance',views.createdbinstance,name="createdbinstance"),
    url(r'^deletedbinstance',views.deletedbinstance,name="deletedbinstance"),
]