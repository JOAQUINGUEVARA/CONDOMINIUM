from django.urls import path
from .views import HomePageView, SamplePageView,upload_image
from django.conf.urls import url, include

urlpatterns = [
    #path('', HomePageView.as_view(), name="home"),
    #path('sample/', SamplePageView.as_view(), name="sample"),
    #path('upload_image/', upload_image, name='upload_image'),
    ]