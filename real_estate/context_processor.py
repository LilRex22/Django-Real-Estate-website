from houses.models import Newsletter_Email

def newsletter_status(request):
    email = request.session.get("newsletter_email")

    verified = False
    if email:
        verified = Newsletter_Email.objects.filter(
            email=email,
            verified=True
        ).exists()

    return {
        "newsletter_verified": verified
    }