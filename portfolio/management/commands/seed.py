from django.core.management.base import BaseCommand

from portfolio.models import Achievement, Education, Profile, Project, Skill


class Command(BaseCommand):
    help = "Load starter portfolio content (safe to run more than once)."

    def handle(self, *args, **opts):
        Profile.objects.get_or_create(name="Neel Menghani", defaults=dict(
            headline="Computer Engineering student building web applications with Python and Django",
            about=("I am a seventh-semester Computer Engineering student at SAL Engineering and Technical "
                   "Institute, affiliated to Gujarat Technological University, Ahmedabad. In July 2026 I "
                   "completed a Python internship at Sparks To Ideas, where I worked from Python basics "
                   "through object-oriented programming to Django, and built this site."),
            location="Ahmedabad, Gujarat"))
        Education.objects.get_or_create(institution="SAL Engineering and Technical Institute (SETI)", defaults=dict(
            degree="Bachelor of Engineering, Computer Engineering", period="7th semester, academic year 2026-27",
            details="Affiliated to Gujarat Technological University, Ahmedabad."))
        for cat, names in {"Backend": ["Python", "Django", "Django ORM"], "Frontend": ["HTML", "CSS", "JavaScript"],
                           "Database": ["SQLite"], "Tools": ["Git", "GitHub", "VS Code"]}.items():
            for n in names:
                Skill.objects.get_or_create(name=n, category=cat)
        Project.objects.get_or_create(title="Portfolio Website", defaults=dict(
            description=("This site. A Django application that presents a profile, education, skills, projects, "
                         "achievements and a contact form. Content lives in SQLite and is managed through the Django admin."),
            tech="Python, Django, HTML, CSS, JavaScript, SQLite"))
        Achievement.objects.get_or_create(title="Python Internship completed", defaults=dict(
            description="Completed the Python internship programme at Sparks To Ideas, Ahmedabad.",
            when="6 to 20 July 2026"))
        self.stdout.write(self.style.SUCCESS("Starter content loaded."))
