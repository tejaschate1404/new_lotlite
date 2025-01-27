from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from adminUser.models.carrier import Career
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class AddCareerView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'admin/career/add_career.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        # Validate required fields
        if not all([title, description, location, category]):
            messages.error(request, "All fields except image are required.")
            return redirect('addCareer')

        # Save the Career object with the provided data
        try:
            Career.objects.create(
                title=title,
                description=description,
                location=location,
                category=category,
                image=image
            )
            messages.success(request, "Career added successfully!")
        except Exception as e:
            messages.error(request, f"Error saving career: {str(e)}")

        return redirect('addCareer')




@login_required
def viewCareer(request):
    careers = Career.objects.all()  # Fetch all careers
    paginator = Paginator(careers, 10)  # Paginate with 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin/career/view_career.html', {'page_obj': page_obj})




@login_required
def deleteCareer(request, career_id):
    career = get_object_or_404(Career, id=career_id)
    career.delete()
    messages.success(request, "Career deleted successfully!")
    return redirect('viewCareer')

