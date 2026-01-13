# Email verification stuff
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import email_verification_token


from houses.models import Newsletter_Email


def subscribe_newsletter(request, email):
    # here we make sure that the email does not already exist by filtering the database
    if not Newsletter_Email.objects.filter(email=email).exists():
        obj = Newsletter_Email.objects.create(email=email)
        obj.save()
        subject = 'Please verify your email'
        current_site = get_current_site(request)
        message = render_to_string('email_verification.html', {
            'email': email,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
            'token': email_verification_token.make_token(obj),
            })
        EmailMessage(subject, message, to=[email]).send(fail_silently=False)    

        # we stored the email in the session to be used later for the footer
        request.session["newsletter_email"] = email
        return True, 'We Just sent you an email to verify your newsletter subscription. Please check your inbox.'

    else:
        return False, 'The email already exist. Please input a new email'