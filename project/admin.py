from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')


admin.site.register(Category)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(NewsFeedModel)
admin.site.register(ProfileModel, ProfileAdmin)
