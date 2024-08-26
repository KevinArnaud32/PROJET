from django.urls import  path
from .views import index, ajoutStudent, updateStudent

app_name= "student"
urlpatterns = [
   path('', index, name="index"),
   path('ajouterStudent/', ajoutStudent, name="ajouterStudent" ),  
   path('updateStudent/', updateStudent, name="modifierStudent" ),
]
