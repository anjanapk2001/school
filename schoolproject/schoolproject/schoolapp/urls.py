from.import views
from django.urls import path
urlpatterns=[
    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('new_page/', views.new_page, name='new_page'),

]

