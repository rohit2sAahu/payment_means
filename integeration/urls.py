from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('sign/',views.sign_up,name="sign_up"),
    path('success/',views.success,name="success"),
    path('login_up/',views.login_up,name="login_up"),
    path('profile/',views.user_profile,name="profile"),
    path('payment/',views.payment,name="payment"),
    path('success/',views.success,name="success"),
]
