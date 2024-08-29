from django.urls import  path
from . import views

app_name="teacher"
urlpatterns = [
   path('', views.list, name="list"),
   path('add/', views.add, name='add' ),
   path('modifierTeacher/<int:id>', views.modifierTeacher, name='modifierTeacher' ),
   path('supprimerTacher/<int:id>',views.supprimerTeacher, name='supprimerTeacher')
]
