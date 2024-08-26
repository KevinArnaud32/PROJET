from django.urls import  path
from . import views

app_name="user"
urlpatterns = [
   path('', views.index, name="index"),
   path('ajouterUser/', views.ajouterUser, name='ajouterUser' ),
   path('modifierUser/', views.ajouterUser, name='modifierUser' ),
]
