from django.urls import path
from django.views.decorators.cache import cache_page
from users.views import login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/',login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout')
]
