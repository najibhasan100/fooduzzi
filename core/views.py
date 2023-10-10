from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from core.models import Product, CartOrder, Category, Vandor, CartOrderItems, ProductImages, ProductReview, Wishlist, Address
from django.conf import settings
from .forms import UserRegisterForm
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

def index(request):
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, 'core/index.html')
def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)  # Remove the "or None" part here


        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }

    return render(request, "core/sign-up.html", context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'core/login.html', context)
# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#     # try:
#     #     user = User.objects.get(email=email)
#     # except User.DoesNotExist:
#     #         user = None
#         user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         messages.success(request, "You are logged in.")
#         return redirect('index')
#     else:
#         messages.warning(request, "Invalid credentials. Please try again.")
#     context = {}  # You can add context data here if needed
#     return render(request, "core/login.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("core:login")


def account(request):
    return render(request, "core/account.html")
def contact(request):
    return render(request, "core/contacts.html")

def about_us(request):
    return render(request,"core/about-us.html")
def faq(request):
    return render(request,"core/faq.html")