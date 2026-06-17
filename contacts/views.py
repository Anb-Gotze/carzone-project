from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message_body = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
            if has_contacted.exists():
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message_body,
        )

        # FIX: Safely pull all superuser emails into a list using filter() instead of get()
        admin_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))

        # Fallback email in case no admin emails exist in your database
        if not admin_emails:
            admin_emails = ["abakwumegodwin1@gmail.com"]

        # Compose email body
        message_text = f"You have a new inquiry for the car {car_title}. Please login to your admin panel for more info."

        # Send the email to the full list of admin emails found
        send_mail(
            subject="New Car Inquiry",
            message=message_text,
            from_email="abakwumegodwin1@gmail.com",
            recipient_list=admin_emails, 
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/' + car_id)

    return redirect('/')