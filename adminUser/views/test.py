from django.shortcuts import render
from adminUser.models.contactusModel import ContactUs
from django.core.paginator import Paginator
from adminUser.models.category import Category

def test(request):
    hello = request.POST.get("name")
    # categories = Category.objects.filter(name = hello)
    categories = Category.objects.all()
    return render(request, 'admin/test/test.html',{'categories':categories})
    
def test(request):
    hello = request.POST.get("name")  # Retrieve the category name from POST data
    categories = Category.objects.filter(name=hello)  # Filter categories based on the name
    return render(request, 'admin/test/test.html', {'categories': categories})  # Correct variable name