from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE




from .models import *

admin.site.register(BuyProduct)
admin.site.register(ProductImage)
admin.site.register(PortfolioSection)
admin.site.register(CompanyPagePicture)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)

admin.site.register(Contact, ContactAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20})},
    }
    ordering = ('-created_at',)
admin.site.register(BlogPost, BlogPostAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(BlogCategory, BlogCategoryAdmin)