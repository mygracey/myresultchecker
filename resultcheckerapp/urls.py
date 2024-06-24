from django.urls import path 
from . import views



urlpatterns = [
    path('',views.indexPage,name='index'),
    path('<str:studentname>/',views.resultPage,name='results'),
    path('checkview',views.checkview,name='checkview'),
    path('logout/',views.logoutPage,name="logout"),
]
