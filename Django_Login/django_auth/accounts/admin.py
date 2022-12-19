from django.contrib import admin
from .models import Profile, System_Post
from django.contrib.auth.models import User, Group

# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(System_Post)
admin.site.unregister(Group)