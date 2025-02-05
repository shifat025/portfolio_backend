from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Contact

@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        html_message = render_to_string('contact_email.html', {'contact': instance})
        plain_message = strip_tags(html_message)
        send_mail(
            subject=f'New Contact Form Submission from Portfolio by {instance.name}',
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['shifat58201@gmail.com'],
            html_message=html_message,
            fail_silently=False,
        )
