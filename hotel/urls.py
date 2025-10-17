from django.urls import path
from .views import index,test,crear_huesped,lista_huesped

urlpatterns= [
    path('' , index , name='index'),
    path('test/',test , name='test'),
    path('huesped/nuevo',crear_huesped,name='huesped_form'),
    path('huesped/',lista_huesped,name='huesped_list'),
]