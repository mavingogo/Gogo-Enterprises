from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'gogo_enterprise/index.html')

