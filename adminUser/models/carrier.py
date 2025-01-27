from django.db import models

class Career(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='career_images/', blank=True, null=True)  # New Image Field
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically update on save

    def __str__(self):
        return self.title
