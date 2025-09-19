from django.shortcuts import render
from .models import Information
from .forms import ContactUsForm

# Create your views here.


def contactus(request):
    information = Information.objects.all()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['message'])
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', context={'form':form, 'information':information})



