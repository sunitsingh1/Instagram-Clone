from django.urls import path

from Instaclone.views import index

urlpatterns = [
    path('',index,name='home'),
]