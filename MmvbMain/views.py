from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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

