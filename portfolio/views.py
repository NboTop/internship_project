from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Achievement, Education, Profile, Project, Skill


def home(request):
    context = {
        "p": Profile.objects.first(),
        "education": Education.objects.all(),
        "skills": Skill.objects.order_by("category", "name"),
        "projects": Project.objects.all(),
        "achievements": Achievement.objects.all(),
        "form": ContactForm(),
    }
    return render(request, "portfolio/home.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent. Thank you for getting in touch.")
        else:
            messages.error(request, "Enter your name, a valid email address and a message.")
    return redirect("/#contact")
