from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from ads.models import Ad, Comment
from ads.permissions import IsOwner
from ads.serializers import AdSerializer, CommentSerializer


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner | IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_id')
        ad = get_object_or_404(Ad, pk=ad_id)
        serializer.save(author=self.request.user, ad=ad)


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        return Comment.objects.filter(ad=ad_id)


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwner | IsAdminUser]

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        return Comment.objects.filter(ad=ad_id)


class CommentDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner | IsAdminUser]

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_id')
        return Comment.objects.filter(ad=ad_id)
