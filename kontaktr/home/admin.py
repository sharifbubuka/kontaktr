from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName", "Email", "Telephone")


admin.site.register(Contact, ContactAdmin)
