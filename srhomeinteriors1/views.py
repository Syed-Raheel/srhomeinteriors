from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def quote_request(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        
        # Retrieve selected dropdown values
        residence_type = request.POST.get('residence_type')
        bedrooms = request.POST.get('bedrooms')
        
        if name == '' or email == '' or number == '' or residence_type=='' or bedrooms=='':
            context['errmsg'] = 'Fields cannot be empty'
            return render(request, 'home.html', context)
        
        # Construct email message
        subject = 'Budget Friendly Quote Request'
        email_message = f'Name: {name}\nEmail: {email}\nPhone Number: {number}\nResidence Type: {residence_type}\nBedrooms: {bedrooms}'

        # Send email
        send_mail(
            'New Quote Request',
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            ['raheelliet@gmail.com'],  # Replace with the host's email address
            fail_silently=False,
        )

        user_email_message = 'Thank you for contacting us. We will get back to you soon.'
        send_mail(
            'Thank you for contacting us',
            user_email_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return HttpResponse("Your response has been submitted")  # Redirect to success page

    return render(request, 'home.html')
