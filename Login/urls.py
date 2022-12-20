from django.urls import path

from .views import (CompanyUserView, ForgotPasswordView, LoginView,
                    RedefinePasswordView, SignInCompanyView, SignInView,
                    VerificationView)

urlpatterns = [
    path('signin/', SignInView.as_view(), name="signin"),
    path('signincompany/', SignInCompanyView.as_view(), name="signincompany"),
    path('forgotpassword/', ForgotPasswordView.as_view(), name="forgotpassword"),
    path('redefinepassword/', RedefinePasswordView.as_view(), name="redefinepassword"),
    path('verification/', VerificationView.as_view(), name="verification"),
    path('profile/', CompanyUserView.as_view(), name="profile"),
    path('login/', LoginView.as_view(), name="login"),
]