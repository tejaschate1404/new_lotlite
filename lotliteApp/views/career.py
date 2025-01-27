from django.shortcuts import render

from adminUser.models.carrier import Career



def career(request):
    items = Career.objects.all() 
    return render(request, 'client/career.html', {'items': items})