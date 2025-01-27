from django.shortcuts import render, redirect
from adminUser.models.courses import Course
from django.shortcuts import render, get_object_or_404

def search_courses(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
    if query:
        # Search by title or description
        courses = Course.objects.filter(
            title__icontains=query
        ) | Course.objects.filter(
            description__icontains=query
        )
    else:
        courses = Course.objects.none()
    
    context = {
        'query': query,
        'courses': courses,
    }
    return render(request, 'client/search.html', context)



def courseDetail(request, pk):
    # Fetch the course with the given primary key
    course = get_object_or_404(Course, pk=pk)
    related_courses = Course.objects.filter(category=course.category).exclude(pk=course.pk)[:3]  # Limit to 
    
    print(related_courses ,"this is the courses")
    context ={'course': course,
              'related_courses':related_courses
              }

    return render(request, 'client/courseDetails.html', context)