from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addPost',views.addPost,name="Add Post"),
    path('login',views.userLogin,name="Login"),
    path('register',views.userRegister,name="register"),
    path('viewPost/<str:id>',views.viewPost,name="view Post"),
    path('Profile',views.viewProfile,name="view profile"),
]