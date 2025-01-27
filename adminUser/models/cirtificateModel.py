from django.db import models

class CategoryCirtificate(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='certificates/')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(CategoryCirtificate, on_delete=models.CASCADE, related_name='certificates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
