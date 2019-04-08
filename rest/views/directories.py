from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.units import UnitSerializer
from ..serializers import CountrySerializer
from ..serializers.package_info import PackageSerializer
from ..models.measure_unit import Unit
from ..models.package import Package
from ..models.shipment import Shipment
from ..models import Country
from django.db.models import Q


class UnitSearchView(APIView):

    def get(self, request):
        query = request.query_params.get('query')
        query_cap = query.capitalize()

        by_query = Q(name_full__icontains=query)
        by_cap_query = Q(name_full__icontains=query_cap)
        filtered = Unit.objects.filter(by_query | by_cap_query)

        serializer = UnitSerializer(filtered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageSearchView(APIView):

    def get(self, request):
        query = request.query_params.get('query')
        query_cap = query.capitalize()

        by_query = Q(package_name_rus__icontains=query)
        by_cap_query = Q(package_name_rus__icontains=query_cap)
        filtered = Package.objects.filter(by_query | by_cap_query)

        serializer = PackageSerializer(filtered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountriesView(APIView):

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
