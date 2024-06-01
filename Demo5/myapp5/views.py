from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myapp5.models import Product,Categories,Sub_category,Filter_Price,Color,Brand,Contact,Review
#cart
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import razorpay
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRECT))

# from myapp5.models import Sub_category

def index(request):
        
        product = Product.objects.filter(status = 'Publish')
        subcategory = Sub_category.objects.all()
        categories  = Categories.objects.all()
        
        CATID = request.GET.get('categories')
        
        if CATID:
                product = Product.objects.filter(categories = CATID,status = 'Publish')
        
        else:
                product = Product.objects.filter(status = 'Publish')
        
        
            
        context = {
                'product':product,
                'subcategory':subcategory,
                'categories' :categories,
        }
    
        return render(request, "index.html",context)

   
def registration_Details(request):
        if request.method == "POST":
                username = request.POST.get('username')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                pass1 = request.POST.get('pass1')
                pass2 = request.POST.get('pass2')
                try:
                        uid = registration.objects.get(email=email)
                        if uid:
                                contaxt={
                                        "msg":"User email already exixt"
                                }
                                return render(request,"registration.html",contaxt)
                except:
                        if pass1==pass2:
                                
                                customer = User.objects.create_user(username,email,pass1)
                                customer.pass2 = pass2
                                customer.first_name = first_name
                                customer.last_name = last_name
                                customer.save()
                                return redirect('handlelogin')
                        else:
                                contaxt={
                                        "msg":"Password & Confirm Password Not Matched"
                                }
                                
                                return render(request, "registration.html",contaxt)
        else:
                return render(request,"registration.html")
        
        
        

def handlelogin(request):
        if "username" in request.session:
                return redirect('index')
        else:
                if request.method == "POST":
                        username = request.POST.get("username")
                        password = request.POST.get("password")
                        
                        try:
                                user = authenticate(username= username, password = password)
                                if user is not None:
                                        login(request,user)
                                        return redirect('index')
                                else:             
                                        return render(request,'handlelogin.html')
                        except:
                                return render(request,"handlelogin.html")
                else:
                        context = {
                                "mssg": "Invalid Username or Password"
                        }
                        return render(request,"handlelogin.html",context)
       
        
        # return render(request, "handlelogin.html")
    
def handlelogout(request):
        
        logout(request)
        
        return redirect('index')

    
def shop(request):
        product = Product.objects.filter(status = 'Publish')
        sub_category = Sub_category.objects.all()
        categories  = Categories.objects.all()
        filter_price = Filter_Price.objects.all()
        color = Color.objects.all()
        brand = Brand.objects.all()
        
        CATID = request.GET.get('categories')
        PRICE_FILTER_ID = request.GET.get('filter_price')
        BRANDID = request.GET.get('brand')
        
        print(PRICE_FILTER_ID)
        if CATID:
                product = Product.objects.filter(categories = CATID,status = 'Publish')
        elif PRICE_FILTER_ID:
                product = Product.objects.filter(filter_price = PRICE_FILTER_ID, status = 'Publish')
        elif BRANDID:
                product = Product.objects.filter(brand = BRANDID, status = 'Publish')
        else:
                product = Product.objects.filter(status = 'Publish')
        
        
        
        context = {
                'product':product,
                'sub_category':sub_category,
                'categories' :categories,
                'filter_price' :filter_price,
                'color' :color,
                'brand' :brand,
        }
   
        return render(request, "shop.html",context)

        
        
def cart(request):
        
   
        return render(request, "cart.html")


@login_required(login_url="handlelogin")   
def contact(request):
        if request.method == "POST":
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                
                contact = Contact(
                        name = name,
                        email = email,
                        subject = subject,
                        message = message,
                        
                )
                
                subject = subject
                message = message
                email_from = settings.EMAIL_HOST_USER
                try:
                        send_mail(subject,message,email_from,['fashion.q994@gmail.com'])
                        contact.save()
                        return redirect('index')
                except:
                        return redirect('contact')
                        
   
        return render(request, "contact.html")



def privacy(request):
   
        return render(request, "privacy.html")

def salesreturn(request):
   
        return render(request, "salesreturn.html")
    
def shopdetail(request):
   
        return render(request, "shopdetail.html")
    
    
    
def terms(request):
   
        return render(request, "terms.html")
    
def layout_footer(request):
   
        return render(request, "layout_footer.html")
    
def block_hf(request):
   
        return render(request, "block_hf.html")
    
def error(request):
   
        return render(request, "error.html")
    
def hello(request):
   
        return render(request, "hello.html")
    
        
def sea(request):
        query = request.GET.get('query')
        product = Product.objects.filter(name__icontains= query)
        
        context = {
                'product' :product,
        }
        
        return render(request, "sea.html",context)

def singleproduct(request,id):
        prod = Product.objects.filter(id = id).first()
        
        context = {
                'prod' :prod,
        }
        
        return render(request, "singleproduct.html",context)
def single(request):
        
        if request.method == "POST":
                name=request.POST.get('name')
                email=request.POST.get('email')
                review=request.POST.get('review')
                description=request.POST.get('description')
                
                single = Review(
                        name = name,
                        email=email,
                        review = review,
                        description = description,
                        
                )
                single.save()
        return render(request,"shop.html")
        
        
@login_required(login_url="handlelogin")
def userdetails(request):
       
        return render(request, "userdetails.html")




####CART...

# def cart(request):
#         return render(request, "cart.html")

@login_required(login_url="handlelogin")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("Cart/cart_details")


@login_required(login_url="handlelogin")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("Cart/cart_details")


@login_required(login_url="handlelogin")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("Cart/cart_details")


@login_required(login_url="handlelogin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("Cart/cart_details")


@login_required(login_url="handlelogin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("Cart/cart_details")


@login_required(login_url="handlelogin")
def cart_details(request):
    return render(request, 'Cart/cart_details.html')

@login_required(login_url="handlelogin")
def checkout(request):
        amount_str = request.POST.get('amount')
        amount_float = float(amount_str)
        amount = int(amount_float)
        # amount = int(amount_str)
        # print(type(amount))
        payment = client.order.create({
                "amount":amount*100,
                "currency": "INR",
                "payment_capture":"1"
        }
               
        )
        
        order_id = payment['id']
        context = {
                'order_id' : order_id,
                'payment'  : payment,
        }
        # print(order_id)
        return render(request, "Cart/checkout.html",context)

def PLACE_ORDER(request):
        if request.method == "POST":
                uid = request.session.get('_auth_user_id')
                user = User.objects.get(id=uid)
                cart = request.session.get('cart')
                # print(cart)
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                country = request.POST.get('country')
                address = request.POST.get('address')
                city = request.POST.get('city')
                state = request.POST.get('state')
                postcode = request.POST.get('postcode')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                amount = request.POST.get('amount')
                
                
                
                order_id = request.POST.get('order_id')
                payment = request.POST.get('payment')
                
                context = {
                        'order_id':order_id,
                }
                
                order = Order(
                        user = user,
                        firstname = firstname,
                        lastname = lastname,
                        country = country,
                        address = address,
                        city = city,
                        state = state,
                        postcode = postcode,
                        phone = phone,
                        email = email,
                        payment_id = order_id,
                        amount = amount,    
                          
                        
                )
                order.save()
                
                for i in cart:
                        
                        a = (int(cart[i]['price']))
                        b = cart[i]['quantity']
                        

                        total = a * b
                        
                        
                        
                        item = OrderItem(
                                user = user,
                                order = order,
                                product = cart[i]['name'],
                                image = cart[i]['image'],
                                quantity = cart[i]['quantity'],
                                price = cart[i]['price'],
                                total = total 
                        )
                        
                        item.save()
                
        return render(request,'Cart/placeorder.html', context)

@csrf_exempt
def success(request):
        if request.method == "POST":
                a = request.POST
                order_id = ""
                for key, val in a.items():
                        if key == 'razorpay_order_id':
                                order_id = val
                                break
                        
                        
                user = Order.objects.filter(payment_id = order_id).first()
                user.paid = True
                user.save()
        return render(request, 'Cart/thankyou.html')

def yourorder(request):
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        
        order = OrderItem.objects.filter(user = user)
        context = {
                'order': order,
        }
        return render(request,'yourorder.html',context)