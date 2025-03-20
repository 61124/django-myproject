from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form submission (e.g., save to DB, send email)
            return render(request, "success.html", {'name': form.cleaned_data['name']})
    return render(request, "contact.html", {"form": form})
