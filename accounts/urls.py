from django.urls import path

from . import views

#rooth path
urlpatterns = [
    path("login", views.login, name="login"),  # blank path means default folder, in this context /listings
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]