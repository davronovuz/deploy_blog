from django.contrib import admin
from .models import Blog,Contact



class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","created_at"]


class ContactAdmin(admin.ModelAdmin):
    list_display = ["full_name","phone_number","created_at"]



admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact,ContactAdmin)