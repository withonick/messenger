from django.contrib import admin

from messenger.models import Post

from messenger.models import Category


# Register your models here.


admin.site.register(Post)
admin.site.register(Category)