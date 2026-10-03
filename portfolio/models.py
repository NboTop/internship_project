from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=80)
    headline = models.CharField(max_length=160)
    about = models.TextField()
    location = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=120)
    degree = models.CharField(max_length=120)
    period = models.CharField(max_length=60)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "education"

    def __str__(self):
        return f"{self.degree}, {self.institution}"


class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.CharField(max_length=160, help_text="Comma-separated technologies")
    link = models.URLField(blank=True)

    def tech_list(self):
        return [t.strip() for t in self.tech.split(",") if t.strip()]

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    when = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.created:%d %b %Y})"
