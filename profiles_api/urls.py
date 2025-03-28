from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


# Registering the viewset to a router.
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# No need to specify a basename since the viewset uses a queryset.
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
# This is a suburl that is linked to the HelloApiView
# Whenever a ApiView call is made, like get or post, it'll
# call the specific function in the HelloApiView.
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # Enable login endpoint for DRF
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
# path('', include(router.urls)) router will create
# all the urls that we specify in the viewset for us.
# we leave '' becomes we just want to include each url into the base-url.
