from django.contrib import admin
from .models import House, Newsletter_Email

# Register your models here.
admin.site.register(House)
@admin.register(Newsletter_Email)
class NewsletterEmailAdmin(admin.ModelAdmin):
    list_display = ['email', 'verified',]