from django.urls import path 

from .views_auth import ProfileList

urlpatterns = [
    path('profiles/', ProfileList.as_view()),

]