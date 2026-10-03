from django.contrib import admin

from .models import Achievement, ContactMessage, Education, Profile, Project, Skill

for model in (Profile, Education, Skill, Project, Achievement):
    admin.site.register(model)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created")
    readonly_fields = ("created",)
