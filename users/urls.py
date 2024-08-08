from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserResetPassword, UserResetPasswordConfirm

app_name = UsersConfig.name

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('reset_password/', UserResetPassword.as_view(), name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', UserResetPasswordConfirm.as_view(), name='reset_password_confirm')
] + router.urls
