from django.urls import path

from ads.apps import AdsConfig
from rest_framework.routers import DefaultRouter

from ads.views import AdViewSet, CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = AdsConfig.name

router = DefaultRouter()
router.register('', AdViewSet, basename='ads')

urlpatterns = [
    path('<int:ad_id>/comments/create/', CommentCreateAPIView.as_view(), name='create-comment'),
    path('<int:ad_id>/comments/', CommentListAPIView.as_view(), name='list-comments'),
    path('<int:ad_id>/comments/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='update-comment'),
    path('<int:ad_id>/comments/delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='destroy-comment')
] + router.urls
