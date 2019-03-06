from einvoice_app.einvoice.serializers import HelloSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import detail_route, list_route
import requests

class HelloViewSet(viewsets.ModelViewSet):
	queryset = ''
	serializer_class = HelloSerializer

	@list_route(methods=['GET'])
	def query_list(self, request):
		url = 'https://api.einvoice.nat.gov.tw/PB2CAPIVAN/invapp/InvApp'
		payload = dict(version='0.2', action='QryWinningList', invTerm='10712', UUID='1', appID='EINV2201902206541')
		response = requests.post(url, data=payload)
		result = response.json()
		return Response(result, status=status.HTTP_200_OK)
