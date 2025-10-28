from django.urls import path
from .views import *


urlpatterns = [
    path('listado/', HabitacionListView.as_view(), name='habitacion_list'), 
    path('nueva/', HabitacionCreateView.as_view(), name='habitacion_create'),
    path('<int:pk>/detalle/', HabitacionDetailView.as_view(), name='habitacion_detail'), 
    path('<int:pk>/editar/', HabitacionUpdateView.as_view(), name='habitacion_update'), 
    path('<int:pk>/eliminar/', HabitacionDeleteView.as_view(), name='confirm_delete'),
]