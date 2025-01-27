from django.shortcuts import render, redirect
from django.contrib import messages
from adminUser.models.contactusModel import ContactUs

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate fields
        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return redirect('home')

        # Save the data
        ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Your message has been submitted successfully!")
        return redirect('home')

    return redirect('home')
