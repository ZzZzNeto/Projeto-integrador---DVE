from django.urls import path


from .views import (UserView, ForgotPasswordView,
                    RedefinePasswordView, SignUpCompanyView, SignUpExternalView, UpdateUserCompanyView, DeleteUserView, UpdateUserExternalView, UpdateUserInternalView, UpdateCoordinationUserView,
                    VerificationView, Subscribe, RemoveSubscribe, Favorite, RemoveFavorite, RemoveFavoriteProfile, ChangePassowordView  )

urlpatterns = [
    path('signin/', SignUpExternalView.as_view(), name="signin"),
    path('signincompany/', SignUpCompanyView.as_view(), name="signincompany"),
    path('forgotpassword/', ForgotPasswordView.as_view(), name="forgotpassword"),
    path('redefinepassword/', RedefinePasswordView.as_view(), name="redefinepassword"),
    path('verification/', VerificationView.as_view(), name="verification"),
    path('profile/>', UserView.as_view(), name="profile"),
    path('updateCompany/', UpdateUserCompanyView.as_view(), name="updateCompany"),
    path('updateExternal/', UpdateUserExternalView.as_view(), name="updateExternal"),
    path('updateInternal/', UpdateUserInternalView.as_view(), name="updateInternal"),
    path('updateCoordenacao/', UpdateCoordinationUserView.as_view(), name="updateCoordenacao"),
    path('deleteuser/<int:pk>', DeleteUserView.as_view(), name="deleteuser"),
    path('subscribe/<int:pk>', Subscribe, name="subscribe"),
    path('removeInscription/<int:pk>', RemoveSubscribe, name="removeInscription"),
    path('favorite/<int:pk>', Favorite, name="favorite"),
    path('removeFavorite/<int:pk>', RemoveFavorite, name="removeFavorite"),
    path('removeFavoriteProfile/<int:pk>', RemoveFavoriteProfile, name="removeFavoriteprofile"),
    path('password/', ChangePassowordView.as_view(), name='passwordChange'),
    
]