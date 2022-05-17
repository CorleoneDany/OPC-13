import views as profile_views
from django.urls import path


urlpatterns = [
    path('profiles/', profile_views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile_views.profile, name='profile'),
]
