from django.shortcuts import render
from ..models import Product, Contact,Categories, Book
def home(request):
    user_profile = request.session.get('name')
    if not user_profile:
        return render(request,'signup.html')
    user_mail = request.session.get('email')
    user_phone = request.session.get('phone')
    location = request.session.get('location')
    product = Product.get_all()
    contact = Contact.objects.get()
    catogereis = Categories.all_catogaries()
    book = Book.get_all()
    
    if user_profile:
        login_button = None
    else:
        login_button = "Login"

    s_data = {
        'user': user_profile,
        'mail': user_mail,
        'phone': user_phone,
        'login': login_button,
        'products': product,
        'catogereis': catogereis,
        'books': book,
        'location': location,
        'contact': contact,
    }

    if user_profile:
        return render(request, 'index.html', s_data)

