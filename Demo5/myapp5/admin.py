from django.contrib import admin
from .models import *

class ImagesTablerinline(admin.TabularInline):
    model = Images
    
class TagTablerinline(admin.TabularInline):
    model = Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTablerinline,TagTablerinline]
    
class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerinline]
    list_display = [
        'firstname','phone','email','payment_id','paid','date'
    ]
    search_fields = ['firstname','email','payment_id']
    


admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(registration)
admin.site.register(login)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Sub_category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Review)



