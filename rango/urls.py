from django.urls import path
from . import views

app_name = 'rango'
urlpatterns = [
     path('', views.index, name='index'),
     path('views/', views.views, name='views'),
     path('about/', views.about, name='about'),
     path('add_category/', views.add_category, name='add_category'),
     path('category/<slug:category_name_url>/add_page/', views.add_page, name='add_page'),
     path('category/<slug:category_name_url>/', views.show_category, name='show_category'),
     path('register/',
         views.register,
         name='register'), # New pattern
     path('login/', 
         views.user_login,
         name = 'login'),
     path('restricted/', 
         views.restricted,
         name='restricted'),
     path('logout/', 
          views.user_logout,
          name='logout'),
]