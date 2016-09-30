from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def plot_graph(request):
    return render(request, "templates/Main.html", {})

def index(request):
    return HttpResponse("Hello world, start of the Django")
