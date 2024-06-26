from django.contrib import admin
from .models import Post, Contact

# Register your models here.
admin.site.register(Contact)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}