from django.urls import path
from blogapp import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.home,name='home'),
    path('addblog',views.addblog,name='addblog'),
    path('viewblogs',views.viewblogs,name='viewblogs'),
    path('addtodb',views.addtodb,name='addtodb'),
]