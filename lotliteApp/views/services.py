from django.shortcuts import render ,redirect, get_object_or_404
from adminUser.models.services import Services
from adminUser.models.services import CategoryServices

def services(request):
    service = Services.objects.all()
    context = {
        'services':service
    }
    return render (request, 'client/services.html',context)


        
def studentMobility(request):
    return render (request, 'client/studentMobility.html')
