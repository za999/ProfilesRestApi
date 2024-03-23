from django.urls import path
from profiles_api import views


# This is a suburl that is linked to the HelloApiView
# Whenever a ApiView call is made, like get or post, it'll
# call the specific function in the HelloApiView.
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
