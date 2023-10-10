# from django import views
from django.urls import path
from core.views import index
from core import views
from . import views

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("sign-up/", views.register_view, name="sign-up"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("contacts/",views.contact,name="contacts"),
    path("account/", views.account,name="account"),
    path("about-us/", views.about_us,name="about-us"),
    path("faq/", views.faq,name="faq"),
    
]
