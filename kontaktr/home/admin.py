from django.contrib import admin

# Register your models here.
from kontaktr.home.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName", "Email", "ContactNumber")


admin.site.register(Contact, ContactAdmin)
