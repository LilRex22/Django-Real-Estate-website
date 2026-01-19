from django.shortcuts import render, redirect
from houses.models import House, Newsletter_Email, Category
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .services import subscribe_newsletter
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from .tokens import email_verification_token

# pagination stuff
from django.core.paginator import Paginator


# note that the form logic for the newsletter email has to be in every view for it to work from every view
def home(request):
    houses = House.objects.all()[:6]
    if request.method == 'POST':
        email = request.POST.get('newsletter_email')
        if email:
            success, message = subscribe_newsletter(request, email)
            if success:
                messages.success(request, message)
                return redirect('home')
            else:
                messages.error(request, message)
                return redirect('home')
        else:
            messages.error(request, 'Please input an email')
    return render(request, 'home.html', {'houses': houses})


def about(request):
    if request.method == 'POST':
        email = request.POST.get('newsletter_email')
        if email:
            success, message = subscribe_newsletter(request, email)
            if success:
                messages.success(request, message)
                return redirect('home')
            else:
                messages.error(request, message)
                return redirect('home')
        else:
            messages.error(request, 'Please input an email')
    return render(request, 'about.html', {})


def contact_us(request):
    
    # the newsletter email logic
    if request.method == 'POST':
        if 'newsletter' in request.POST:
            email = request.POST.get('newsletter_email')
            if email:
                success, message = subscribe_newsletter(request, email)
                if success:
                    messages.success(request, message)
                    return redirect('home')
                else:
                    messages.error(request, message)
                    return redirect('home')
            else:
                messages.error(request, 'Please input an email')
    
    # the contact email message logic
    if request.method == 'POST':
        if 'contact_mail' in request.POST:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            u_email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            
            mail_title = f'You have a new message from {fname} {lname} on your website!'
            email = EmailMessage(
                mail_title,
                message,
                # the from email in professional practices should be a real and verified email dedicated to your website.
                # smtp servers block mails from unverified emails to avoid spam
                # the from email is first authenticated before a mail is sent from it.
                # it must be an email you have access to and control.
                # it doesn't necessarily recieve the reply to the mail, you can use the reply-to to specify the email that will recieve the reply
                
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                headers={'Reply-To': u_email}
            )
            email.send(fail_silently=False)
            messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'contact_us.html', {})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        obj = Newsletter_Email.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Newsletter_Email.DoesNotExist):
        return HttpResponse('Activation link is invalid!', status=400)

    if email_verification_token.check_token(obj, token):
        obj.verified = True
        obj.save()
        return HttpResponse('Your email has been verified successfully!', status=200)
    else:
        return HttpResponse('Activation link is invalid!', status=400)


def explore(request):
    houses = House.objects.all()
    types = Category.objects.all()
    
    # the sorting logic
    sort = request.GET.get("sort", "newest")
    ordering_map = {
        "price_asc": "Price",
        "price_desc": "-Price",
        "newest": "-created_at",
    }
    order_by = ordering_map.get(sort, "-created_at")
    houses = houses.order_by(order_by)
    
    # the filtered search logic
    house_type = request.GET.get('type')
    price = request.GET.get('price')
    location = request.GET.get('location')
    
    if house_type:
        # because category itself is a queryset, we do category__name which is like doing category.name
        houses = houses.filter(category__name__iexact=house_type)
        
    if location:
        houses = houses.filter(Location__icontains=location)
        
    if price:
        price = int(price) # this converts the price string to an integer for comparison
        if price == 1000000:
            houses = houses.filter(Price__gte=1000000, Price__lte=5000000)
        elif price == 5000000:
            houses = houses.filter(Price__gte=5000000, Price__lte=10000000)
        elif price == 10000000:
            houses = houses.filter(Price__gte=10000000, Price__lte=50000000)
        elif price == 50000000:
            houses = houses.filter(Price__gte=50000000, Price__lte=100000000)
        elif price == 100000000:
            houses = houses.filter(Price__gte=100000000)

    
    # pagination stuff
    pg = Paginator(houses, 15)
    page = request.GET.get('page')
    listings = pg.get_page(page)
    
    return render(request, 'explore_properties.html', {'houses': houses, 'listings': listings, 'types': types})


def detail(request, house_id):
    house = House.objects.get(id=house_id)
    return render(request, 'details.html', {'house': house})