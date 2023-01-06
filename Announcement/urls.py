from django.urls import path

from .views import AnnoucementView, CandidatesView, StagesView, AnnoucementCreate, AnnouncementUpdate, AnnouncementDelete

urlpatterns = [
    path('stages/', StagesView.as_view(), name="stages"),
    path('announcement/<int:pk>', AnnoucementView.as_view(), name="announcement"),
    path('announcementCreate/', AnnoucementCreate.as_view(), name="announcementCreate"),
    path('update/<int:pk>', AnnouncementUpdate.as_view(), name="announcementUpdate"),
    path('delete/<int:pk>', AnnouncementDelete.as_view(), name="announcementDelete"),
    path('candidates/', CandidatesView.as_view(), name="candidates"),
]