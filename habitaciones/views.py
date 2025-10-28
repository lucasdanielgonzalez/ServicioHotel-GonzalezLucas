from habitaciones.forms import HabitacionForm
from habitaciones.models import Habitacion
from django.urls import reverse_lazy
from django.views.generic import  ListView,CreateView,UpdateView,DeleteView,DetailView


class HabitacionListView(ListView):
    model = Habitacion
    template_name = 'habitaciones/habitacion_list.html'
    context_object_name = 'habitaciones'

    def get_queryset(self):
        query = self.request.GET.get('q','')
        if query:
            return Habitacion.objects.filter(numero=query).order_by('-max_huespedes')
        return Habitacion.objects.all()

class HabitacionCreateView(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'habitaciones/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')


class HabitacionUpdateView(UpdateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'habitaciones/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')
    slug_field = 'hotel'
    slug_url_kwarg = 'hotel'


class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'habitaciones/habitacion_confirm_delete.html'
    success_url = reverse_lazy('habitacion_list')
    slug_field = 'precio_noche'
    slug_url_kwarg = 'precio_noche'
    


class HabitacionDetailView(DetailView):
    model = Habitacion
    template_name = 'habitaciones/habitacion_detail.html'
    context_object_name = 'habitacion'
    slug_field = 'hotel'
    slug_url_kwarg = 'hotel'
    