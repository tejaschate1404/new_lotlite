from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.contrib import messages
from adminUser.models.cirtificateModel import CategoryCirtificate
from adminUser.models.cirtificateModel import Certificate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




class Cirtificate(LoginRequiredMixin, View):
    def get(self, request):
        category = CategoryCirtificate.objects.all()
        certificate = Certificate.objects.all()

        print(category, certificate)


        context = {
            'category':category,
            'certificate':certificate

        }
        return render(request, 'admin/cirtificate/add_cirtificate.html',context)
    
    def post(self, request):
        category_id = request.POST.get("category")  # Assuming category is a ForeignKey field
        image = request.FILES.get("image")  # Use FILES for handling file uploads
        title = request.POST.get("title")  # Corrected 'titile' to 'title'
        description = request.POST.get("description")

        # Ensure category is fetched properly
        try:
            category = CategoryCirtificate.objects.get(id=category_id)
        except CategoryCirtificate.DoesNotExist:
            return redirect('Cirtificate')
        # Create the Certificate object
        certi = Certificate(
            category=category,
            image=image,
            title=title,
            description=description
        )
        certi.save()

        print(category, image, title, description)
        return redirect('viewCirtificate')

        
        



@login_required
def viewCirtificate(request):

    cirti = Certificate.objects.all()
    paginator = Paginator(cirti, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj

    }
    return render(request, 'admin/cirtificate/view_cirtificate.html',context)


@login_required
def deleteCirtificate(request, certificate_id):
    # Get the course object or return 404 if not found
    course = get_object_or_404(Certificate, id=certificate_id)
    
    if request.method == "GET":
        course.delete()  # Delete the course from the database
        messages.success(request, "Certificate deleted successfully!")
    
    return redirect('viewCirtificate')  # Redirect to the courses view page





# def addCirtificateCategory(request):
 #   categories = CategoryCirtificate.objects.all()   Fetch categories to show in the dropdown
    # print(categories)
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     description = request.POST.get('description')
    #     category_id = request.POST.get('category')
    #     image = request.FILES.get('image')  # Handling image upload

    #     # Validate that a category is selected
    #     if category_id:
    #         category = CategoryCirtificate.objects.get(id=category_id)
    #     else:
    #         category = None

    #     # Create certificate
    #     if title and category:
    #         Certificate.objects.create(
    #             title=title,
    #             description=description,
    #             image=image,
    #             category=category
    #         )
    #         messages.success(request, 'Certificate added successfully!')
    #     else:
    #         messages.error(request, 'Please fill out all required fields.')

    #     return redirect('addCertificate')  # Redirect to the same form page after submission

    # return render(request, 'admin/cirtificate/addCirtificateCategory.html', {'categoryCirtificate': categories})

@login_required
def addCirtificateCategory(request):
    categoryCirtificate = CategoryCirtificate.objects.all()
    if request.method == "POST":
        # Handle form submission here
        pass
    return render(request, 'admin/cirtificate/addCirtificateCategory.html', {'categoryCirtificate': categoryCirtificate})




@login_required
def addCirtificateCategory(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            CategoryCirtificate.objects.create(title=title, description=description)
            messages.success(request, 'Category added successfully!')
        else:
            messages.error(request, 'Please fill out all fields.')

        return redirect('addCategory')
    return render(request, 'admin/cirtificate/addCirtificateCategory.html')




# def deleteCirtificate(request):
#     return render(request, 'admin/cirtificate/view_cirtificate.html')