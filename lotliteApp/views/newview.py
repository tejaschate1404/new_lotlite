from django.shortcuts import render




def about(request):
    return render (request, 'client/about.html')

def contact(request):
    return render (request, 'client/contact.html')

def practice(request):
    return render (request, 'client/practice.html')


