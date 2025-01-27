from django.db import models
from .category import Category


class Course(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # Delete courses if the category is deleted
        related_name='courses',   # Enables reverse lookup (e.g., category.courses.all())
        blank=False, 
        null=False,default=1
    )
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    what_you_learn = models.TextField(blank=False, null=False)
    courses_included = models.TextField(blank=False, null=False)
    course_contents = models.TextField(blank=False, null=False)
    detailed_description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Automatically add timestamp
    updated_at = models.DateTimeField(auto_now=True)      # Automatically update timestamp

    def __str__(self):
        return self.title


