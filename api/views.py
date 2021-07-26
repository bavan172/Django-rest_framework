from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view #for api view decorator
from rest_framework.response import Response 
from .serializers import *
from .models import Task

# Create your views here.
@api_view(['GET'])  
def apiOverview(request):
    api_urls = {
        'List':"hello"
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer =  TaskSerializer(tasks, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def taskDetail(request, pk): #displaying a single task
    task = Task.objects.get(id=pk)
    serializer =  TaskSerializer(task, many=False) # return one object
    return Response(serializer.data)   
    

@api_view(['POST'])    
def taskCreate(request): #displaying a single task
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   
    

@api_view(['POST'])
def taskUpdate(request, pk): #displaying a single task
    task = Task.objects.get(id=pk)
    serializer =  TaskSerializer(instance=task, data=request.data) # update particular object and post data
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   

@api_view(['DELETE'])
def taskDelete(request, pk): #displaying a single task
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully deleted")   