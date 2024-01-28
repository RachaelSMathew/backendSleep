from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404, JsonResponse
from .models import DailyDream
from .serializers import DreamSerializer
# Create your views here.

class DreamView(APIView):

    def post(self, request):
        data = request.data
        serializer = DreamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Dream Added Successfully", safe=False)
        return JsonResponse("Failed to Add Dream", safe=False)
    
    def get(self, request, pk=None):
        data = DailyDream.objects.filter(
            userNameAddS__exact=request.GET.get('username', '')
        )
        serializer = DreamSerializer(data, many=True)
        return Response(serializer.data)
    

    ##UPDATE
    def put(self, request, pk=None):
        dream_update = DailyDream.objects.get(dreamId=pk)
        serializer = DreamSerializer(instance=dream_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student updated Successfully", safe=False)
        return JsonResponse("Failed To Update Student")
    

    ##delete
    def delete(self, request, pk):
        dream_to_delete = DailyDream.objects.get(dreamId=pk)
        dream_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)