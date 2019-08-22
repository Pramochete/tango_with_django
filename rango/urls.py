from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('views/', views.views, name='views'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    re_path(r'^category/(?P<category_name_url>[\w\-]+)/$',views.show_category,name='show_category')
]