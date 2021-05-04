from django.shortcuts import render
from .models import Passenger
from django.contrib import messages
from django.http import HttpResponse
from .forms import Itemforms
from django.views import View

# Create your views here.

def item_list(request):
    showall = Passenger.objects.all()
    return render(request,'index.html',{"data": showall})


def form_display(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('destination') and request.POST.get('date') and request.POST.get('price') and request.POST.get('rt_pcr'):
            saverecord = Passenger()
            saverecord.name = request.POST.get('name')
            saverecord.age = request.POST.get('age')
            saverecord.destination = request.POST.get('destination')
            saverecord.date = request.POST.get('date')
            saverecord.price = request.POST.get('price')
            saverecord.rt_pcr = request.POST.get('rt_pcr')
            saverecord.save()

            messages.success(request,'Travel details of '+saverecord.name+' has been added successfully!')
            return render(request,'form.html')

    else:
        return render(request,'form.html')

    
def Edit_item(request,id):
    Edit_item_obj = Passenger.objects.get(id=id)
    return render(request,'Edit.html',{"Passenger":Edit_item_obj})

def Update_item(request,id):
    Update_item_obj = Passenger.objects.get(id=id)
    form=Itemforms(request.POST,instance=Update_item_obj)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated successfully!')
        return render(request,'Edit.html',{"Passenger":Update_item_obj})
    

def Delete_item(request,id):
    Delete_item_obj = Passenger.objects.get(id=id)
    Delete_item_obj.delete()
    showdata = Passenger.objects.all
    return render(request,'Index.html',{"data":showdata})

