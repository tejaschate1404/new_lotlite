from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)  # Name of the commenter
    profession = models.CharField(max_length=100, blank=False, null=False)  # Profession of the commenter
    comment = models.TextField(blank=False, null=False)  # The comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was created
    
    def __str__(self):
        return f"{self.name} ({self.profession})"
