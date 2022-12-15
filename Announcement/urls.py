from django.urls import path

from .views import StagesView

urlpatterns = [
    path('stages/', StagesView.as_view(), name="stages"),
]