
from django.urls import path
from .views import index,test,crear_huesped,lista_huesped ,eliminar_huesped,modificar_huesped

urlpatterns= [
    path('' , index , name='index'),
    path('test/',test , name='test'),
    path('huesped/nuevo',crear_huesped, name='huesped_form'),
    path('huesped/',lista_huesped, name='huesped_list'),
    path ('huesped/<int:dni>/eliminar' , eliminar_huesped , name='eliminar_huesped'),
    path ('huesped/<int:dni>/modificar', modificar_huesped , name='modificar_huesped'),
]