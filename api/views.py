from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id= pythondata.get('id', None)
        if id is not None:
            stu= Student.objects.get(id=pk)
            serializer= StudentSerializer(stu)
            return JsonResponse(serializer.data)
        
        stu= Student.objects.all()
        serializer= StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method=="POST":
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'data created'}
            # json_data= JSONRenderer().render(res)
            # return HttpResponse(json_data)
            return JsonResponse(serializer.data, safe=False)
        # json_data= JSONRenderer().render(serializer.error)
        # return HttpResponse(json_data)
        return JsonResponse(serializer.errors, safe=False)

    if request.method=="PUT":
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id= pythondata.get('id')
        stu= Student.objects.get(id=id)
        serializer= StudentSerializer(stu, data= pythondata)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'data updated!!!'}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.error, safe=False)

    if request.method=="DELETE":
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id= pythondata.get('id')
        stu= Student.objects.get(id=id)

        stu.delete()
        res= {'msg': "data deleted"}
        return JsonResponse(res, safe= False)




            




        
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

