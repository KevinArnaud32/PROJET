from django.urls import  path
from .views import list, add, update, supprimerStudent

app_name= "student"
urlpatterns = [
   path('', list, name="list"),
   path('add/', add, name="add" ),  
   path('modifierStudent/<int:id>', update, name="modifierStudent" ),
   path('supprimerStudent/<int:id>', supprimerStudent, name="supprimerStudent")
]
