from django.contrib import admin


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

