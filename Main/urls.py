from django.urls import path

from .views import AboutUsView, FaqView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('faq/', FaqView.as_view(), name="faq"),  
    path('aboutus/', AboutUsView.as_view(), name="aboutUs"),
]
