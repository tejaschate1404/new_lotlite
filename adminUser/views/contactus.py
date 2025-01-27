from django.shortcuts import render
from django.views import View
from adminUser.models.contactusModel import ContactUs
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


class ContactusView(LoginRequiredMixin, View):
    def get(self, request):
        # Retrieve all contact submissions
        contact_list = ContactUs.objects.all()

        # Set up the paginator to show 10 contacts per page
        paginator = Paginator(contact_list, 10)

        # Get the page number from the request's query parameters
        page_number = request.GET.get('page')

        # Get the page object for the current page
        page_obj = paginator.get_page(page_number)

        # Render the template with the paginated contact data
        return render(request, 'admin/contactus/contactus.html', {'page_obj': page_obj})
