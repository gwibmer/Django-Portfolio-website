from django.shortcuts import render, get_object_or_404
from .models import (
    Contact,
    HeroSection,
    AboutSection,
    SkillsSection,
    Skill,
    ResumeSummary,
    Education,
    Experience,
    ProjectsSection,
    Project,
    ContactSection,
)


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

    context = {
        'hero': HeroSection.objects.first(),
        'about': AboutSection.objects.first(),
        'skills_section': SkillsSection.objects.first(),
        'skills': Skill.objects.all(),
        'resume': ResumeSummary.objects.first(),
        'education': Education.objects.all(),
        'experience': Experience.objects.all(),
        'projects_section': ProjectsSection.objects.first(),
        'projects': Project.objects.all(),
        'contact_section': ContactSection.objects.first(),
    }
    return render(request, 'home.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, 'home.html')
