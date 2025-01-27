from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from adminUser.models.contactusModel import ContactUs
from adminUser.models.courses import Course
from adminUser.models.cirtificateModel import Certificate
from adminUser.models.carrier import Career
from django.utils.timezone import now, timedelta


@login_required
def indexAdmin(request):
    today = now().date()
    yesterday = today - timedelta(days=1)

    #contact us
    today_count = ContactUs.objects.filter(created_at__date=today).count()
    yesterday_count = ContactUs.objects.filter(created_at__date=yesterday).count()
    contact_count = ContactUs.objects.count()
    today_contacts = ContactUs.objects.filter(created_at__date__in=[today, yesterday])
    

    #courses
    today_course_count = Course.objects.filter(created_at__date=today).count()  # Filter by today's date
    yesterday_course_count = Course.objects.filter(created_at__date=yesterday).count()  # Filter by yeste
    total_course_count = Course.objects.count()  # Get total count

    #cirtificate
    today_certificate_count = Certificate.objects.filter(created_at__date=today).count()
    yesterday_certificate_count = Certificate.objects.filter(created_at__date=yesterday).count()
    total_cirtificate_count = Certificate.objects.count()

    #career
    today_career_count = Career.objects.filter(created_at__date=today).count()
    yesterday_career_count = Career.objects.filter(created_at__date=yesterday).count()
    total_career_count = Career.objects.count()


    print(today_count, yesterday_count)
    

    context = { 
                #contact
                'today_count':today_count,
               'yesterday_count':yesterday_count,
               'contact_count': contact_count,
               'today_contacts':today_contacts,
               #course
               'today_course_count':today_course_count,
               'yesterday_course_count':yesterday_course_count,
               'total_course_count':total_course_count,
               #certificate
               'today_certificate_count':today_certificate_count,
               'yesterday_certificate_count':yesterday_certificate_count,
               'total_cirtificate_count':total_cirtificate_count,
               #certificate
               'today_career_count':today_career_count,
               'yesterday_career_count':yesterday_career_count,
               'total_career_count':total_career_count,


               }

    return render (request, 'admin/indexAdmin.html',context)
