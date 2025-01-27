
from django.shortcuts import render
from adminUser.models.category import Category
from adminUser.models.courses import Course


from django.shortcuts import get_object_or_404

def home(request):
    # Fetch categories with id=4 and id=5, or return 404 if not found
    category_4 = get_object_or_404(Category, id=4)
    category_5 = get_object_or_404(Category, id=5)
    
    # Limit to the first 3 courses for both categories
    category_4.first_three_courses = category_4.courses.all()[:3]
    category_5.first_three_courses = category_5.courses.all()[:3]
    
    return render(request, 'client/index.html',  {'categories': [category_4, category_5]})







# def home(request):
#     # Attempt to get the category with id=1, or return a 404 page if not found
#     category = get_object_or_404(Category, id=4)
#     category.first_three_courses = category.courses.all()[:3]  # Limit to first 3 courses
    
#     return render(request, 'client/index.html', {'categories': [category]})

