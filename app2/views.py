from django.shortcuts import render

# Create your views here.
def Sthird(request):
    d={'name':'Guddu'}
    return render(request, 'Sthird.html',d)