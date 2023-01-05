from django.urls import path

from .views import AnnoucementView, CandidatesView, StagesView, AnnoucementCreate

urlpatterns = [
    path('stages/', StagesView.as_view(), name="stages"),
    path('announcement/', AnnoucementView.as_view(), name="announcement"),
    path('announcementCreate/', AnnoucementCreate.as_view(), name="announcementCreate"),
    path('candidates/', CandidatesView.as_view(), name="candidates"),
]