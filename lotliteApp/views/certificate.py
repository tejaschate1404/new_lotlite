from django.shortcuts import render
from django.views.generic import View
from adminUser.models.cirtificateModel import Certificate
from django.core.paginator import Paginator

class CertificateView(View):
    def get(self, request):
        service = Certificate.objects.all()
        context = {
            'services':service
        }
        return render (request, 'client/certificate.html',context)

