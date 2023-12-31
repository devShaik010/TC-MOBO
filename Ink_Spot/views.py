from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from .models import Product, Contact, Profile, Categories, Profilecat, Book, B_categories, Customer, Order, Pform
import razorpay
def payment(amount, user_profile):
    key_id = "rzp_test_YlYtdLrSGniSFi"
    key_secret = "1WYuR9tuqgVA9kHcTIG2PwoA"
    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        "amount": float(amount) * 100,
        "currency": "INR",
        "receipt": user_profile,
        "notes": {
            "name": user_profile,
            "Payment_for": "New order",
        }
    }
    
    order = client.order.create(data=data)
    order_id = order["id"]
    name = order['receipt']

    get_order = {
        'id': order_id,
        'receipt': name,
    }
    return get_order

# def index(request):
#     product = Product.get_all()
#     contact = Contact.objects.get()
#     catogereis = Categories.all_catogaries()
#     book = Book.get_all()
#     user_profile = request.session.get('name')
#     user_mail = request.session.get('email')
#     user_phone = request.session.get('phone')
#     location = request.session.get('location')
    
#     if user_profile:
#         login_button = None
#     else:
#         login_button = "Login"

#     s_data = {
#         'user': user_profile,
#         'mail': user_mail,
#         'phone': user_phone,
#         'login': login_button,
#         'products': product,
#         'catogereis': catogereis,
#         'books': book,
#         'location': location,
#         'contact': contact,
#     }

#     if user_profile:
#         return render(request, 'index.html', s_data)
#     else:
#         return render(request, 'signup.html')


# # For Creating User ( signup )
# def sign_up(request):
    if request.method == 'GET':
        user_name = ""
        user_check = {}
        user_check['user'] = user_name
        return render(request, "signup.html",user_check)
    else:
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phone')
        area = postData.get('area')
        password = postData.get('password')
        rpassword = postData.get('rpassword')

        error_msg = None
        customer = Customer(name = name,email = email, phone = phone,password = password,area=area)
 
        value = {
            'name': name,
            'email': email,
            'phone': phone,
            'area':area,
            'password': password,
            'rpassword':rpassword
         }

        if customer.isname():
            error_msg = "User name is Alredy taken"

        elif name == "" or email =="" or phone == "" or password =="":
            error_msg = "Fill The all fields"

        elif customer.isExist():
            error_msg = "Email Is Alredy Exist try to Login"

        elif len(phone)!=10:
            error_msg = "Enter Valid Phone Number"
            
        elif customer.isnumber():
            error_msg = "Number is Alredy register try to login"   

        elif password != rpassword:
            error_msg = "Password does not macth"
        
        if error_msg:
              data = {
                'error': error_msg,
                'values': value
              }
              return render(request, "signup.html" ,data)


        else:     
           User.objects.create_user(username=name,
                                  email=email,
                                  password=password,)
           
           customer.password = make_password(customer.password)
           customer.register()
           
           return redirect('login')

# For Login 
def login(request):
    request.session.clear()
    if request.method == "GET":
        user_name = ""
        user_check = {}
        user_check['user'] = user_name
        return render(request, 'login.html',user_check)
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer(email = email , password = password)
        if customer.isExist():
            customer = Customer.get_cutomer_by_email(email)
        else:
            error_msg = "Invalid"
        error_msg = None


        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer_id']= customer.id
                request.session['email']= customer.email
                request.session['phone']= customer.phone
                request.session['name']= customer.name
                request.session['location']= customer.area

                
                return redirect('home')
            else:
                error_msg = "Email & password is Invalid"
                # print(customer)
                # print(email,password)
                return render(request, 'login.html' , {'error' : error_msg})
       

# for Books
def book(request):
    book = Book.get_all()
    book = None
    bcat = B_categories.all_catogaries()
    categoryID = request.GET.get('categories')
    if categoryID:
        book = Book.get_all_filter(categoryID )
    else:
        book = Book.get_all()
    
    customer_id = request.session.get('customer_id')
    customer = Customer.objects.get(id=customer_id)
    user_profile = customer.name
    user_location = customer.area

    login_button = None
    if user_profile:
        login_button = ''
    else:
        login_button = "Login"  


    bdata = {} 
    bdata['book'] = book 
    bdata['b_catogereis'] = bcat
    bdata['user'] = user_profile
    bdata['login']= login_button 
    bdata['location'] = user_location

    return render(request, 'book.html',bdata)

  # for product _ stationary items

# For Products
def product(request):
    if request.method == 'POST':
        pr_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(pr_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(pr_id)
                    else:    
                        cart[pr_id] = quantity-1
                else:
                    cart[pr_id] = quantity+1

            else:
                cart[pr_id] = 1
        else:
            cart = {}
            cart[pr_id] = 1

        request.session['cart'] = cart         
        # print(request.session['cart'])

    if request.method == "GET":
        cart = request.POST.get('cart')
        if cart:
            request.session.get('cart').clear()

        

    # returning empty cart if cart not exixts
    cart = request.session.get('cart')
    if not cart:
        request.session.cart = {}
    
    product = None
    cat = Categories.all_catogaries()
    categoryID = request.GET.get('categories')
    
    if categoryID:
        product = Product.get_all_filter(categoryID) 
    else:
        product = Product.get_all() 

    user_id = request.session.get('customer_id')
    customer = Customer.objects.get(id=user_id)
    user_profile = customer.name
    user_location = customer.area

    login_button = None
    if user_profile:
        login_button = None
    else:
        login_button = "Login"  
    

    data = {} 
    data['product'] = product
    data['catogereis'] = cat
    data['user'] = user_profile
    data['login']= login_button 
    data['location'] = user_location
    return render(request, 'product.html',data)


# Cart Page 
def cart(request):
    user_id = request.session.get("customer_id")
    customer = Customer.objects.get(id=user_id)
    user_profile = customer.name
    
    is_empty = request.session.get('cart')
    if is_empty == None:
        return redirect("product")
    else:
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        # print(products)
   
        data = {} 
        data['user'] = user_profile
        data['location'] = customer.area
        data['products'] = products
        data['address'] = customer.address
        data['number'] = customer.phone
        return render(request, 'cart.html',data)
    
# Check Out 
def check_out(request):
    if request.method == "POST":
        # user_profile = (request.session.get('name'))
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        zone = request.POST.get('zone')
        customer = request.session.get('customer_id')
        # print(customer)
        cart  = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        
        
        for product in products:
            order = Order(customer= Customer(id = customer),
                          product = product,
                          price = product.discount,
                          quantity = cart.get(str(product.id)),
                          address = address,
                          phone = phone,
                          zone = zone)

            order.placeOrder()
        user_profile = (request.session.get('name'))
        
        total = request.POST.get('total')
        print(total)
        user_profile = (request.session.get('name'))
        
        order_get = payment(total,user_profile)


        data = {}
        data['id'] =order_get['id']
        data['receipt'] = order_get['receipt']
        data['total'] = total
        data['user'] = user_profile


        return render(request, 'payment.html',data)   

    # if request.method == "GET":
    #     return HttpResponse("Your payament is success")
    

def orders(request):
    request.session['cart'] = {}

    user_profile = (request.session.get('name'))
    if request.method == "GET" or request.method == "post":
        customer = request.session.get('customer_id')
        customer_name = Customer.objects.get(id=customer)
        order = Order.get_orders_by_customer(customer)
        
        orders = {}
        orders['orders'] = order
        orders['user'] = customer_name.name
        orders['location'] = customer_name.area
        return render(request, 'order.html',orders)
    
def payment_page(request):
    request.session['cart'] = {}
    if request.method =="POST":
        order_id = request.POST.get('data-order_id')
        print(order_id)
     

        return redirect('orders')


    

def searchBar(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(desc__icontains=query)
        user_id = request.session.get('customer_id')
        customer = Customer.objects.get(id=user_id)
        data = {}
        data['user'] = customer.name
        data['location'] = customer.area
        data['products'] = products
        if not products:
            return render(request, 'testing.html', {'alert': True})
        else:
            return render(request, 'testing.html', data)



    product = Product.get_all()
    data = {}
    data['products'] = product
    # data['empty']
    # Handle the case where the query is empty
    return render(request, 'testing.html',data)

def searchBar2(request):
    query = request.GET.get('query')
    if query:
        products = Book.objects.filter(about__icontains=query)
        user_id = request.session.get('customer_id')
        customer = Customer.objects.get(id=user_id)
        data = {}
        data['user'] = customer.name
        data['location'] = customer.area
        data['book'] = products
        if not products:
            return render(request, 'testing2.html', {'alert': True})
        else:
            return render(request, 'testing2.html', data)



    product = Book.get_all()
    data = {}
    data['book'] = product
    # data['empty']
    # Handle the case where the query is empty
    return render(request, 'testing2.html',data)


def phone_form(request):
    return render(request, 'mobile.html')

def profile(request):
    profile = Profile.get_all()
    profile = None
    pcat = Profilecat.all_catogaries()
    categoryID = request.GET.get('categories')
    if categoryID:
        profile = Profile.get_all_filter(categoryID )
    else:
        profile = Profile.get_all()
        
    user_id = request.session.get('customer_id')
    customer = Customer.objects.get(id=user_id)   

    login_button = None
    if customer.name:
        login_button = ''
    else:
        login_button = "Login"  


    pdata = {} 
    pdata['profile'] = profile
    pdata['profilecat'] = pcat
    pdata['user'] = customer.name
    pdata['login']= login_button 
    pdata['location']=customer.area

    return render(request, 'profile.html',pdata)


def rqs(request):
    user_id = request.session.get('customer_id')
    customer = Customer.objects.get(id=user_id)
    contact = Contact.objects.get()

    url = Pform.get_all()

    user={}
    user['phone'] = customer.phone
    user['mail'] = customer.email
    user['user'] = customer.name
    user['url'] = url
    user['contact']=contact.offcial_phone
    user['location'] = customer.area



    return render(request, 'rqs.html',user)

def rqs2(request):
    user_id = request.session.get('customer_id')
    customer = Customer.objects.get(id=user_id)
    contact = Contact.objects.get()



    url = Pform.get_all()
    user={}
    user['phone'] = customer.phone
    user['mail'] = customer.email
    user['user'] = customer.name
    user['url'] = url
    user['contact']=contact.offcial_phone
    user['location'] = customer.area



    return render(request, 'rqs2.html',user)


def updates_profile(request):
    if request.method == 'GET':
        user_id = request.session.get('customer_id')
        customer = Customer.objects.get(id=user_id)

     
        user={}
        user['user'] = customer.name
        user['email']=customer.email
        user['phone'] = customer.phone
        user['location'] = customer.area
        return render(request, "update_profile.html",user)
    else:
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phone')
        area = postData.get('area')   
        user_id = request.session.get('customer_id')


        try:
            customer = Customer.objects.get(id=user_id)
            customer.name = name
            customer.email = email
            customer.phone = phone
            customer.location = area
            customer.register()

        except Customer.DoesNotExist:
            return render(request, "update_profile.html")



        user={}
        user['user'] = name
        user['email']=email
        user['phone'] = phone
        user['location'] = area
        return render(request, "update_profile.html",user)


def request_history(request):
    id_ = request.session.get('customer_id')
    customer = Customer.objects.get(id=id_)
    contact = Contact.objects.get()

    data = {}
    data['name']=customer.name
    data['phone'] = customer.phone
    data['location'] = customer.area
    data['contact']=contact.offcial_phone


    return render(request, 'bookings.html',data)

def settings(request):
    return render(request, 'base2.html')
