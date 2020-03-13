from django.urls import path
from website_app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('collection.html',views.collection,name="collection"),
]
