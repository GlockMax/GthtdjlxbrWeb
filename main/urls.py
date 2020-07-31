from django.urls import path
from . import views
urlpatterns = [
    path("", views.gthtdjlxbr, name="home"),
    path("about", views.about, name="about")
]