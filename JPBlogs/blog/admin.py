from django.contrib import admin
from .models import Post, Category


# Register your models here.

# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','add_date')
    search_fields = ('title',)

# for configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','cat',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
