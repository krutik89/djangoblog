from . import views
from django.urls import path,include

urlpatterns = [
    path('blogComment',views.blogComment,name='blogComment'),
    path('',views.blog,name='blog'),
    path('trend',views.trending,name='trend'),
    #path('create',views.create_post,name='create_post'),
    path('<str:slug>',views.blogpost,name='blogpost'),

]