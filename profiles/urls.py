from . import views as profile_views
from django.urls import path

app_name = 'profiles'

urlpatterns = [
    path('', profile_views.index, name='index'),
    path('<str:username>/', profile_views.profile, name='profile'),
]
