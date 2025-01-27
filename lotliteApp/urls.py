
from django.urls import path

from .views.contactus import submit_contact
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views.certificate import CertificateView


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('courses/', views.courses, name="courses"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('practice/', views.practice, name="practice"),
    path('career/', views.career, name="career"),
    path('certificate/', CertificateView.as_view(), name="certificate"),
    

    # couse Detail page 
    path('coursedetails/<int:pk>', views.courseDetail, name="courseDetail"),

    #contactus info save
    path('contactus/', submit_contact, name="submit_contact"),

    #search
    path("search/",views.search_courses ,name="search_courses"),

    #studentMobitliy
    path('studentMobility/', views.studentMobility, name="studentMobility")
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
