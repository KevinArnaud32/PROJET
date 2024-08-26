from django.urls import  path
from . import views

app_name="teacher"
urlpatterns = [
   path('', views.index, name="index"),
   path('ajouterTeacher/', views.ajouterTeacher, name='ajouterTeacher' ),
   path('modifierTeacher/', views.modifierTeacher, name='modifierTeacher' ),
]
