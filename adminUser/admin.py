from django.contrib import admin
from .models.courses import Course
from .models.category import Category
from .models.carrier import Career
from .models.contactusModel import ContactUs
from .models.cirtificateModel import CategoryCirtificate
from .models.cirtificateModel import Certificate
# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Career)
admin.site.register(ContactUs)
admin.site.register(CategoryCirtificate)
admin.site.register(Certificate)