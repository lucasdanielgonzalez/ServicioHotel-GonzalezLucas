from django.shortcuts import render, redirect,get_object_or_404
from .models import Huesped
from .forms import HuespedForm
from django.contrib import messages

def index(request):
    return render(request, 'hotel/index.html')


def test(request):
    return render(request, 'hotel/test.html')


def crear_huesped(request):

    if request.method == "POST":
        form = HuespedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("huesped_form") 
    
    else:
        form = HuespedForm()

    return render(request , "hotel/huesped_form.html", {'form': form})
    



def lista_huesped(request):
    query = request.GET.get('q', "")
    if len(query) > 0:
        huespedes = Huesped.objects.filter(
            nombre__icontains=query
        ).order_by('-fecha_de_nacimiento') 
    else:
        huespedes = Huesped.objects.all().order_by('-fecha_de_nacimiento') 

    return render(request, 'hotel/huesped_list.html', {'huespedes': huespedes, 'query': query})



def eliminar_huesped(request, dni):
     huespedes = get_object_or_404(Huesped, dni=dni)
     huespedes.delete()
     messages.success(request, "Huesped eliminado correctamente")
     return redirect('huesped_list')


def modificar_huesped(request ,dni):
    huespedes = get_object_or_404(Huesped , dni=dni)
    if request.method == 'POST':
        form = HuespedForm(request.POST , instance=huespedes)
        if form.is_valid():
            form.save()
            return redirect('huesped_list')
    else:
        form = HuespedForm(instance=huespedes)
    
    return render(request, 'hotel/huesped_form.html',{'form': form, 'edicion': True} )
                                                   