from django.shortcuts import render
from .models import Contact
from django.views.decorators.csrf import csrf_protect



def home(request):
    # return HttpResponse('home page')
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html")


def contact(request):
    return render(request, "contact.html")


def experience(request):
    return render(request, "experience.html")


def success(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact_info = Contact(name=name, email=email, phone=phone, desc=desc)
        contact_info.save()
        print("The data has been written to the DB")
    return render(request, "success.html")
