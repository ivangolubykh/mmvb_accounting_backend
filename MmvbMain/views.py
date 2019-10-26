from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from .models import BrokerageAccounts
from .models import Issuers
from .models import Regions
from .models import SecuritiesTypes
from .serializers import BrokerageAccountsSerializer
from .serializers import IssuersSerializer
from .serializers import RegionsSerializer
from .serializers import RegionsNameListSerializer
from .serializers import SecuritiesTypesSerializer


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


class AbstractMmvbView(ViewSetMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        if 'destroy_model_instance' in request.data and request.data['destroy_model_instance'] == 'true':
            return self.destroy(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)


class BrokerageAccountsView(AbstractMmvbView):
    permission_classes = (IsAuthenticated,)
    queryset = BrokerageAccounts.objects.all().order_by('name')
    serializer_class = BrokerageAccountsSerializer


class IssuerView(AbstractMmvbView):
    permission_classes = (IsAuthenticated,)
    queryset = Issuers.objects.all().select_related('regions').order_by('name')
    serializer_class = IssuersSerializer


class RegionView(AbstractMmvbView):
    permission_classes = (IsAuthenticated,)
    queryset = Regions.objects.order_by('munitipal_name')

    def get_serializer_class(self):
        if 'only_name' in self.request.query_params and self.request.query_params['only_name'] == 'true':
            return RegionsNameListSerializer
        return RegionsSerializer


class SecuritiesTypesView(AbstractMmvbView):
    permission_classes = (IsAuthenticated,)
    queryset = SecuritiesTypes.objects.order_by('name')
    serializer_class = SecuritiesTypesSerializer
