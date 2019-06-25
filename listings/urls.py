from django.urls import path

from . import views

#rooth path
urlpatterns = [
    path("", views.index, name="listings"),  # blank path means default folder, in this context /listings
    path("<int:listing_id>", views.listing, name="listing"),
    path("search", views.search, name="search"),
]