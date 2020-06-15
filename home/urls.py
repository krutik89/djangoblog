from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('search',views.seach,name='search'),
    path('signup',views.signup,name='signup'),
    path('handlelogin',views.handlelogin,name='login'),
    path('handlelogout',views.handlelogout,name='logout'),
    path('create',views.create_post,name='create_post')

]