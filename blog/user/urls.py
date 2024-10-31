# django
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import path
# from book.views import Myview1, Myview2, BookListView,Myview3,ContactFormView,BookCreateView
from .views import register, my_model_view, LogoutView

# rest_framework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   path('login/', auth_views.LoginView.as_view(template_name='login_view.html'), name="login"),
   path('logout/', auth_views.LogoutView.as_view(), name="logout"),
   path('register/', register, name='register'),
   path('mymodelview/',my_model_view , name='register'),
   path('token/', TokenObtainPairView.as_view(),  name="token_obtain"),
   path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
   path('token/logout', LogoutView.as_view(), name="token_logout"),
]
