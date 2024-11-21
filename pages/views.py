from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., send an email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # Logic for handling the data (e.g., send an email)
            return HttpResponse('<h1>Thank you for contacting us!</h1>')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})