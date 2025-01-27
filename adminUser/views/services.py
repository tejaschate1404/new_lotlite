from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from adminUser.models.services import CategoryServices
from adminUser.models.services import Services
from django.views import View

from django.core.paginator import Paginator
from django.shortcuts import  get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



#services
from adminUser.models.services import CategoryServices





@login_required
def addServicesCategory(request):
    if request.method == 'POST':
        category_title = request.POST.get('category_name')

        # Check if category already exists
        if CategoryServices.objects.filter(title=category_title).exists():
            messages.error(request, "Category already exists!")
        else:
            # Save the category
            CategoryServices.objects.create(title=category_title)
            messages.success(request, "Category added successfully!")

        return redirect('addServicesCategory')  # Redirect after processing

    return render(request, 'admin/services/add_service_category.html')




class ServicesView(LoginRequiredMixin,View):
    template_name = 'admin/services/add_services.html'  # Template to render the form

    def get(self, request, *args, **kwargs):
        # Fetch all categories for the dropdown
        categories = CategoryServices.objects.all()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request, *args, **kwargs):
        # Extract form data from POST request
        category_id = request.POST.get('category')
        image = request.FILES.get('image')  # For file upload
        title = request.POST.get('title')
        primary_desc = request.POST.get('primary_desc')
        description = request.POST.get('description')
    
        # Validate the category
        try:
            category = CategoryServices.objects.get(id=category_id)
        except CategoryServices.DoesNotExist:
            return HttpResponse("Invalid category selected.", status=400)

        # Create and save the course object
        course = Services(
            category=category,
            image=image,
            title=title,
            description=description,
            primary_desc=primary_desc,
        )
        course.save()  # Save to database
        messages.success(request, "Services added successfully!")

        # Redirect to the same page or a course list page
        return redirect('viewServices')  # Adjust to your course list URL name










@login_required
def viewServices(request):
    service = Services.objects.all().order_by('-id')  # Fetch all courses, newest first
    paginator = Paginator(service, 10)  # Show 10 courses per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin/services/view_services.html', {'page_obj': page_obj})


@login_required
def deleteServices(request, services_id):
    # Get the course object or return 404 if not found
    service = get_object_or_404(Services, id=services_id)
    
    if request.method == "GET":
        service.delete()  # Delete the course from the database
        messages.success(request, "Course deleted successfully!")
    
    return redirect('viewServices')  # Redirect to the courses view page
