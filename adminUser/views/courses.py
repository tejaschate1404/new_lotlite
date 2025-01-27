from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from adminUser.models.category import Category
from adminUser.models.courses import Course
from django.views import View

from django.core.paginator import Paginator
from django.shortcuts import  get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required





@login_required
def addCategory(request):
    if request.method == 'POST':
        category_title = request.POST.get('category_name')

        # Check if category already exists
        if Category.objects.filter(title=category_title).exists():
            messages.error(request, "Category already exists!")
        else:
            # Save the category
            Category.objects.create(title=category_title)
            messages.success(request, "Category added successfully!")

        return redirect('addCategory')  # Redirect after processing

    return render(request, 'admin/courses/add_category.html')




class AddCourseView(LoginRequiredMixin,View):
    template_name = 'admin/courses/add_courses.html'  # Template to render the form

    def get(self, request, *args, **kwargs):
        # Fetch all categories for the dropdown
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request, *args, **kwargs):
        # Extract form data from POST request
        category_id = request.POST.get('category')
        image = request.FILES.get('image')  # For file upload
        title = request.POST.get('title')
        description = request.POST.get('description')
        what_you_learn = request.POST.get('what_you_learn')
        courses_included = request.POST.get('courses_included')
        course_contents = request.POST.get('course_contents')
        detailed_description = request.POST.get('detailed_description')

        # Validate the category
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return HttpResponse("Invalid category selected.", status=400)

        # Create and save the course object
        course = Course(
            category=category,
            image=image,
            title=title,
            description=description,
            what_you_learn=what_you_learn,
            courses_included=courses_included,
            course_contents=course_contents,
            detailed_description=detailed_description,
        )
        course.save()  # Save to database
        messages.success(request, "Course added successfully!")

        # Redirect to the same page or a course list page
        return redirect('addCourses')  # Adjust to your course list URL name


# def viewCourses(request):
#     return render (request, 'admin/courses/add_courses.html')





@login_required
def viewCourses(request):
    courses = Course.objects.all().order_by('-created_at')  # Fetch all courses, newest first
    paginator = Paginator(courses, 10)  # Show 10 courses per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin/courses/view_courses.html', {'page_obj': page_obj})


@login_required
def delete_course(request, course_id):
    # Get the course object or return 404 if not found
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == "GET":
        course.delete()  # Delete the course from the database
        messages.success(request, "Course deleted successfully!")
    
    return redirect('viewCourses')  # Redirect to the courses view page