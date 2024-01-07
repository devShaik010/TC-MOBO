from django.shortcuts import render,redirect
from ..models import Customer
from django.contrib.auth.hashers import check_password

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


        if customer.isExist():
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer_id']= customer.id
                request.session['email']= customer.email
                request.session['phone']= customer.phone
                request.session['name']= customer.name
                request.session['location']= customer.area

                
                return redirect('home')
            else: 
                error_msg = "Incorrect Password ! try again."
                data={}
                data['error']=error_msg
                data['email']=email
                # print(customer)
                # print(email,password)
                return render(request, 'login.html' , data,)
        else:
            error_msg = "User Not exist - Create account"
            return render(request, 'login.html' , {'error' : error_msg})


