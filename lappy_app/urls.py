from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('<int:category>/', landing, name='landing'),
    path('detail/<int:id>/', detail_view, name='detail'),
    path('contact/', contact_view, name='contact'),
    path('cart/', cart_view, name='cart'),
    path('review/', review_view, name='review'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='login'),
]
