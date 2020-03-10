from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns=[
	path('', views.index_portal, name='index'),
    path('',views.user_logout,name='logout'),
    path('ingresar/',views.user_login,name='user_login'),
  
]