from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# import io
# from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



@csrf_exempt
@api_view(['GET','POST', 'PUT', 'DELETE'])
def student_api(request, pk=None):
    if request.method=="GET":
        # json_data= request.body
        # stream= io.BytesIO(json_data)
        # pythondata= JSONParser().parse(stream)
        id= pk
        if id is not None:
            stu= Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        
        stu= Student.objects.all()
        serializer= StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method=="POST":
        
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({'msg': 'data posted'})
        
        return Response(serializer.errors)

    if request.method=="PUT":
        
        id= pk
        stu= Student.objects.get(id=id)
        serializer= StudentSerializer(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({'masg': 'data updated'})

        return Response(serializer.error)

    if request.method=="DELETE":
        
        id= pk
        stu= Student.objects.get(id=id)

        stu.delete()
        res= {'msg': "data deleted"}
        return Response({'msg': 'data deleted'})




   # ***********************if we use decorators=(@api_view) then all data can be fetched by simply  using 'request.data'********         




        
# def single_stu(request, pk):
#     stu= Student.objects.get(id=pk)
#     serializer= StudentSerializer(stu)
#     # json_data= JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data)
#     return JsonResponse(serializer.data)

# def all_stu(request):
#     stu= Student.objects.all()
#     serializer= StudentSerializer(stu, many=True)
#     # json_data= JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data)
#     return JsonResponse(serializer.data, safe=False)

