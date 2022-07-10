from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views_auth import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles',ProfileViewSet) #profiles is endpoint

urlpatterns = [
   path('',include(router.urls))

]       