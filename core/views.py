from django.shortcuts import render

def index(request):
  context = {
    'key' : 'value'
  }
  return render(request, 'Core/Home.html', context)

# Create your views here.
