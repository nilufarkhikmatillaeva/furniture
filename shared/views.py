from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from shared.forms import ContactForm

from shared.models import Staff


def page_404(request):
    return render(request, 'shared/404.html')

def about_us(request):
    context = {
        'staff' : Staff.objects.all(),
    }
    return render(
        request, 'shared/about-us.html',
        context
    )

def home(request):
    return render(request, 'shared/home.html')


def contact(request):
    if request.method == "GET":
        return render(request, 'shared/contact.html')
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            text = _("Successfully sent to the admin, thanks for your attention.")
            messages.success(request, text)
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")

            error_text = " | ".join(errors)
            messages.error(request, error_text)
        return render(request, 'shared/contact.html')

