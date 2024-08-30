from django.urls import path
from .views import sign_in, sign_up, log_out


app_name = 'connexion'
urlpatterns = [
    path('',sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('log_out/', log_out, name='log_out')
]