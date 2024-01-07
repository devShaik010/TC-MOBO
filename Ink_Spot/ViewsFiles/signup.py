from django.shortcuts import render,redirect
from ..models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# For Creating User ( signup )
def sign_up(request):
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
