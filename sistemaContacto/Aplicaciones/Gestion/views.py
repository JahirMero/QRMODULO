from django.shortcuts import render

# Create your views here.
def formularioContacto(request):
    return render(request, "formularioContacto.html")

def login(request):
    return render(request, "login.html")