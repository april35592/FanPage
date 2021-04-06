from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WorkSerializer

from .models import Work

@api_view(['GET'])
def workOverview(request):
    api_urls = {
        'List':'/list/',
        'Detail':'/detail/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def workList(request):
    work = Work.objects.all()
    serializer = WorkSerializer(work, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def workDetail(request, pk):
    work = Work.objects.get(id=pk)
    serializer = WorkSerializer(work, many=False)
    return Response(serializer.data)