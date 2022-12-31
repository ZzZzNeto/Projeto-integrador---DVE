from django.urls import path

from .views import (CompanyUserView, ForgotPasswordView, LoginView,
                    RedefinePasswordView, SignUpCompanyView, SignUpExternalView,
                    VerificationView)

urlpatterns = [
    path('signin/', SignUpExternalView.as_view(), name="signin"),
    path('signincompany/', SignUpCompanyView.as_view(), name="signincompany"),
    path('forgotpassword/', ForgotPasswordView.as_view(), name="forgotpassword"),
    path('redefinepassword/', RedefinePasswordView.as_view(), name="redefinepassword"),
    path('verification/', VerificationView.as_view(), name="verification"),
    path('profile/', CompanyUserView.as_view(), name="profile"),
]