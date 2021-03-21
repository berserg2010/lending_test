from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

from django.http.response import HttpResponseRedirect
from django.contrib.auth import login

from .serializers import CustomerSerializer, UserSerializer
from .models import Customer


class CustomerCreate(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    permission_classes = (AllowAny, )
    template_name = 'common/register.html'

    def get(self, request):
        return Response({'site_header': 'ГАМБИТ'})

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                login(request, user)
                return HttpResponseRedirect(redirect_to='/customers/')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer, )

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'content': response.data}, template_name='private/customers.html')
        return response
