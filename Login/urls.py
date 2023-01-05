from django.urls import path

from .views import (UserView, ForgotPasswordView,
                    RedefinePasswordView, SignUpCompanyView, SignUpExternalView, UpdateUserCompanyView, UpdateUserExternalView,
                    VerificationView)

urlpatterns = [
    path('signin/', SignUpExternalView.as_view(), name="signin"),
    path('signincompany/', SignUpCompanyView.as_view(), name="signincompany"),
    path('forgotpassword/', ForgotPasswordView.as_view(), name="forgotpassword"),
    path('redefinepassword/', RedefinePasswordView.as_view(), name="redefinepassword"),
    path('verification/', VerificationView.as_view(), name="verification"),
    path('profile/', UserView.as_view(), name="profile"),
    path('updateCompany/', UpdateUserCompanyView.as_view(), name="updateCompany"),
    path('updateExternal/', UpdateUserExternalView.as_view(), name="updateExternal"),
]