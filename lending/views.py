from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.mail import send_form_data
from .serializers import FormDataSerializer
from .models import Page


class IndexView(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'public/index.html'

    def get(self, request):
        qs = self.get_queryset()
        return Response({'context': qs})

    def post(self, request, *args, **kwargs):
        serializer = FormDataSerializer(data=request.data)
        if serializer.is_valid():
            send_form_data(serializer.data)
        else:
            pass

        qs = self.get_queryset()
        return Response({'context': qs})
    
    def get_queryset(self):
        qs = Page.objects.get(name='index')
        return qs
