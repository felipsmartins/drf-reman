# -*- coding: utf-8 -*-
import typing
from rest_framework import serializers

from api.models import Customer, Release, AppPublishing


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('uuid', 'name',)


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Release
        fields = ('uuid', 'version', 'codename', 'release_date')


class AppPublishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPublishing
        fields = ('uuid', 'customer', 'release', 'pub_date')

    def validate(self, data):
        # type: (typing.Dict[str, typing.Union[Customer,Release]]) -> dict

        customer = data['customer']  # type: Customer
        release = data['release']  # type: Release
        last_release_applied_to_customer = AppPublishing.objects.filter(customer=customer).order_by('-pub_date')[:1]

        # first time receiving a version, just leave it alone!
        if len(last_release_applied_to_customer) < 1:
            return data

        # customer has received updates/releases before
        published = last_release_applied_to_customer[0]  # type: AppPublishing
        customer_release = published.release

        # cannot get an oldest version. version check based on release date
        if customer_release.release_date > release.release_date:
            raise serializers.ValidationError('A versão sendo aplicada é mais antiga que a que o cliente possui.')

        # cannot get the same version
        if customer_release.version == release.version:
            raise serializers.ValidationError('Cliente já possui esta versão.')

        return data
