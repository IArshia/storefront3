from django.shortcuts import render
from  rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recevied the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httbin is ofline')
        return render(request, 'hello.html', {'name': 'Arshia'})
