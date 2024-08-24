from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("post/<int:id>",views.post,name="post"),
    path("editing/<int:id>",views.edit,name="edit"),
    path("delete/<int:id>",views.delete, name="delete"),
    path("create",views.create,name="create"),
    path("signup",views.signup, name="signup")
]