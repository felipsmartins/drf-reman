# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .models import Customer, Release, AppPublishing
from .serializers import CustomerSerializer, ReleaseSerializer, AppPublishingSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AppPublishingViewSet(viewsets.ModelViewSet):
    queryset = AppPublishing.objects.all()
    serializer_class = AppPublishingSerializer

    def get_queryset(self):
        """Modifica o queryset padrão para filtrar registros por:
        - parte do nome do cliente/empresa/usuário;
        - código da versão;
        - data em que o cliente recebeu essa atualização/versão;
        """

        customer = self.request.query_params.get('customer')
        version = self.request.query_params.get('version')
        pub_date = self.request.query_params.get('pub_date')
        queryset = self.queryset  # type: django.db.models.query.QuerySet

        if customer is not None:
            queryset = queryset.filter(customer__name__icontains=customer)

        if version is not None:
            queryset = queryset.filter(release__version__startswith=version)

        if pub_date is not None:
            queryset = queryset.filter(pub_date__gte=pub_date)

        return queryset
