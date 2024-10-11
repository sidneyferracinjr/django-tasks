from django.shortcuts import render
from django.http import HttpResponse

# o usuario faz chamada por link e chega aqui
def home(request):
    return render(request, 'todos/home.html') # jeito correto de chamar a pagina html de templates