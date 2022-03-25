from django.shortcuts import render,HttpResponse
#from .forms import CargoForm

# Create your views here.

def inicio(request):
    return render(request, "index.html")
#vistas de Cargos
# def crearCargo(request):
#     print(request)
#     print(request.method)
#     if request.method == "POST":
#         print("entro por post")
#         cargo_form = CargoForm(request.POST)
#         if cargo_form.is_valid():
#             cargo_form.save()
#     else:
#         print("entro por get")
#     cargo_form = CargoForm()
#     cargos = Cargo.objects.all()
#     return render(request,"pages/cargo.html",{'cargoForm':cargo_form,'accion':'Crear'})

# def editarCargo(request,cod):
#     error,cargo_form = None,None
#     try:
#         cargo = Cargo.objects.get(id=cod)
#         if request.method == "GET":
#             cargo_form = CargoForm(instance=cargo)
#         else:
#             cargo_form = CargoForm(request.POST,instance=cargo)
#             if cargo_form.is_valid():
#                 cargo_form.save()
#     except Exception as e:
#         error=e
#         cargos = Cargo.objects.all()
#         return render(request,"pages/cargo.html",{'cargoForm':cargo_form,'accion':'Crear'})


#vistas de departamentos



def cargo(request):
     return render(request, "pages/cargo.html")

def departamento(request):
    return render(request,"pages/departamento.html")

def empleado(request):

    return render(request,"pages/empleado.html")



    
    


