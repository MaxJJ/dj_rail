from ..kps_service import doLogin
from ..kps_service.classifiers import findStation, findUnits
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..kps_service.kps_login import KPS


class KpsLogin(APIView):

    def get(self, request):
        data = doLogin()
        data['test'] = str(findStation(''))
        return Response(data, status=status.HTTP_201_CREATED)


class KpsFindStation(APIView):

    def get(self, request):
        qry = request.query_params['qry']

        result = findStation(qry)
        return Response(result, status=status.HTTP_200_OK)
