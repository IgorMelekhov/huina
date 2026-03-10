from django.urls import path

urlpatterns = [
    path('get_xcsrf/', get_xcsrf, name='get_xcsrf'),
    path('users/', users, name='users'),
    path('auth/', auth, name='auth'),
]
