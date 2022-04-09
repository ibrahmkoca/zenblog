from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    #path(route,view,opt(kısayol_ismi))
    path('about/' , views.about, name= "about"),
    path("contact/", views.contact ,name = "contact"),
    path("post/", views.post , name = "post"),
]