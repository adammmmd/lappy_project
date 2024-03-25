from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .form import *
from .models import *

# Create your views here.
def landing(request, category=None):
    context ={}
    if category == None:
        
        context["products"] = Products.objects.all()
        context["categories"] = Categories.objects.all()
        return render(request, "index.html", context)
    else:
        context["products"] = Products.objects.filter(category_id = category)
        context["categories"] = Categories.objects.all()
        return render(request, "index.html", context)




def detail_view(request, id):
    context ={}

    context["reviews"] = Reviews.objects.filter(product_id = id)
    context["product"] = Products.objects.get(id = id)
    related_category = context["product"].category_id
    # print(related_category)
    context["related_products"] = Products.objects.filter(category_id=related_category).exclude(id=id)
    context["categories"] = Categories.objects.all()
    return render(request, "product.html", context)

def contact_view(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    return render(request, "contact.html")

def cart_view(request):
    if request.method == "POST":
        pass
    return render(request, "cart.html")

def review_view(request):
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        
        if form.is_valid():
            form.save()
            id = request.POST.get('product_id')
            return redirect('detail', id=id)
        
def register_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, "register.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def custom_404(request, exception):
    return render(request, "404.html", status=404)


