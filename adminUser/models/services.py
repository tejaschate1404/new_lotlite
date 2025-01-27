from django.db import models
class CategoryServices(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title



class Services(models.Model):
    category = models.ForeignKey(CategoryServices,on_delete=models.CASCADE ,related_name='services' ,null=False,default=1)
    title = models.CharField(max_length=100, unique=True)
    primary_desc = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

