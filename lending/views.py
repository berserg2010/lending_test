from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Page


class IndexView(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'public/index.html'

    def get(self, request):
        context = Page.objects.get(name='index')
        return Response({'context': context})
