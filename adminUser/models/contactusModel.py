from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False,default="None")
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically update the timestamp when saved

    def __str__(self):
        return f"{self.name} - {self.subject}"
