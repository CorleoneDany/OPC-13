import views as letting_views
from django.urls import path

from lettings import urls as lettings_urls
from profiles import urls as profiles_urls

urlpatterns = [
    path('lettings/', letting_views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting_views.letting, name='letting'),
] + lettings_urls.urlpatterns + profiles_urls.urlpatterns
