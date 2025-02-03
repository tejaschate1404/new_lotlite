
from django.urls import path 
from . import views
from .views.courses import AddCourseView
from .views.career import AddCareerView
from .views.contactus import ContactusView
from .views.cirtificate import Cirtificate
from .views.services import ServicesView

urlpatterns = [
    path('',views.indexAdmin ,name='indexAdmin'),


    #courses
    path('add-courses/', AddCourseView.as_view() ,name='addCourses'),
    path('view-courses/',views.viewCourses ,name='viewCourses'),
    path('add-category/',views.addCategory ,name='addCategory'),
    path('delete-course/<int:course_id>/', views.delete_course, name='deleteCourse'),


    #carrier 
    path('add-career/', AddCareerView.as_view() ,name='addCareer'),
    path('view-career/',views.viewCareer ,name='viewCareer'),
    path('delete-career/<int:career_id>/', views.deleteCareer, name='deleteCareer'),


    #contact 
    path('contactus/', ContactusView.as_view() ,name='ContactusView'),


    #services
    path('add-services/', ServicesView.as_view() ,name='ServicesAdd'),
    path('view-services/', views.viewServices ,name='viewServices'),
    path('add-services-category/', views.addServicesCategory ,name='addServicesCategory'),
    path('delete-services/<int:services_id>/', views.deleteServices, name='deleteServices'),


    #cirtificate 
    path('add-cirtificate/', Cirtificate.as_view() ,name='Cirtificate'),
    path('view-cirtificate/', views.viewCirtificate ,name='viewCirtificate'),
    path('add-cirtificate-category/', views.addCirtificateCategory ,name='addCirtificateCategory'),
    path('delete-cirtificate/<int:certificate_id>/', views.deleteCirtificate, name='deleteCirtificate'),


    #test 
    path('test/', views.test ,name='test'),


    #Auth
    path('signup/',views.signup_view , name="signupAdmin"),
    path('login/',views.login_view , name="loginAdmin"),
    path('logout/',views.logout_view , name="logoutAdmin"),

    #exan
    path('add-questions/', views.add_questions, name='addQuestions'),
    path('show-questions/', views.show_questions, name='showQuestions'),
    path('show-result/', views.show_result, name='showResult'),
    path('delete-mcq/<int:question_id>/', views.delete_mcq, name='delete_mcq'),



]
