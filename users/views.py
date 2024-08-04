from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from users.services import set_role


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        set_role(user)
        user.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        user = serializer.save()
        password = self.request.data.get('password')
        if password:
            user.set_password(password)
        set_role(user)
        user.save()


class UserResetPassword(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"{settings.BASE_URL}/users/reset_password_confirm/{uid}/{token}"

            send_mail(
                subject='Сброс пароля',
                message=f'{user.first_name}, перейдите по этой ссылке {reset_url} для сброса пароля\n\n'
                        f'Если это были не вы, пожалуйста, проигнорируйте это письмо!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            return Response({
                "message": "Password reset link has been sent to your email"},
                status=status.HTTP_200_OK)

        return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserResetPasswordConfirm(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(pk=uid).first()

            if user and default_token_generator.check_token(user, token):
                new_password = request.data.get('new_password')
                if not new_password:
                    return Response({"error": "New password not provided"}, status=status.HTTP_400_BAD_REQUEST)

                user.set_password(new_password)
                user.save()
                return Response({"message": "Password has been reset successfully"}, status=status.HTTP_200_OK)

        except (TypeError, ValueError, OverflowError):

            return Response({"error": "Invalid token or user ID"}, status=status.HTTP_400_BAD_REQUEST)
