from django.contrib import admin
from .models.product import Product
from .models.profile import Profile
from .models.categories import Categories
from .models.profilecat import Profilecat
from .models.book import Book
from .models.b_catogeries import B_categories
from .models.customer import Customer
from .models.order import Order
from .models.pform import Pform
from .models.contact import Contact


# Define custom admin classes with list_display
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'categories']

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'phone']

class ProfilecatAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

class BookAdmin(admin.ModelAdmin):
    list_display = ['model', 'owner_name', 'b_categories']

class BCategoriesAdmin(admin.ModelAdmin):  # Adjust class name for consistency
    list_display = ['name', 'id']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'date','product_name', 'price', 'quantity']

    def customer_name(self, obj):
        return obj.customer.name

    customer_name.short_description = 'Customer Name'

    def product_name(self, obj):
        return obj.product.name

    product_name.short_description = 'Product Name'

class Contact_display(admin.ModelAdmin):
    list_display = ['offcial_phone', 'email']


# Register your models with the custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Pform)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Profilecat, ProfilecatAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(B_categories, BCategoriesAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Contact,Contact_display)
 
admin.site.site_header = "TC ADMIN"
