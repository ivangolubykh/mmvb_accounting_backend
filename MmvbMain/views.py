from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from .models import Regions
from .serializers import RegionsSerializer


class GetSessionData(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def current(self, request, format=None):
        if format != 'json':
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        user = request.user
        context = dict(
            pk=user.pk,
            first_name=request.user.first_name,
            last_name=request.user.last_name,
        )
        return Response(context)


class RegionView(ViewSetMixin, RetrieveModelMixin, UpdateModelMixin, ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
