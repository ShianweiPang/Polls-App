from django.contrib import admin
from .models import Participant, Poll, Location


# You can change how the admin site displays
class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "date", "location")

    # filter capabilites
    list_filter = ("location", "date")

    # automated-generated slug, as we mentioned the SlugField in Model
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Poll, PollAdmin)
admin.site.register(Location)
admin.site.register(Participant)
