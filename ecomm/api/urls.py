from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('service/', views.service, name='service'),
    path('samsungrepairs/', views.samsungrepairs, name='samsungrepairs'),
    path('iphonerepairs/', views.iphonerepairs, name='iphonerepairs'),
    path('opporepairs/', views.opporepairs, name='opporepairs'),
    path('xiomirepairs/', views.xiomirepairs, name='xiomirepairs'),
    path('realmerepairs/', views.realmerepairs, name='realmerepairs'),
    path('infinixrepairs/', views.infinixrepairs, name='infinixrepairs'),
    path('tecnorepairs/', views.tecnorepairs, name='tecnorepairs'),
    path('redmirepairs/', views.redmirepairs, name='redmirepairs'),
    
]

