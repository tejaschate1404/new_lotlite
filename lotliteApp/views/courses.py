
from django.shortcuts import render
from adminUser.models.category import Category
from adminUser.models.courses import Course
from django.shortcuts import render, get_object_or_404


def courses(request):
    # Fetch all categories
    categories = Category.objects.all()
    # For each category, limit the courses to the first three (optional, based on your logic)
    for category in categories:
        category.first_three_courses = category.courses.all()[:3]  # Limit to the first 3 courses for each category
    return render(request, 'client/course.html', {'categories': categories})



def courseDetail(request, pk):
    # Fetch the course with the given primary key
    course = get_object_or_404(Course, pk=pk)
    related_courses = Course.objects.filter(category=course.category).exclude(pk=course.pk)[:3]  # Limit to 
    
    print(related_courses ,"this is the courses")
    context ={'course': course,
              'related_courses':related_courses
              }

    return render(request, 'client/courseDetails.html', context)




