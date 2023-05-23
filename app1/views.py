from django.shortcuts import render
import datetime
# Create your views here.

def builtin_filters(request):
    d={'data':'nO WaY to hOmE','c':2,'date':datetime.datetime.now()}
    

    return render(request,'builtin_filters.html',d)
def usd_filters(request):
    d={'data':'hai this is filter CASE'}
    return render(request,'usd_filters.html',d)