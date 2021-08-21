from django.shortcuts import render
from django.contrib.auth import get_user
from .models import ProfModel
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfSerializers
from rest_framework.response import Response
from django.http import JsonResponse

# Create your viws here.
#@permission_classes((IsAuthenticated))
#@authentication_classes((JWTAuthentication,))

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([ JWTAuthentication])
@permission_classes([IsAuthenticated])
def myProf(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'GET':
                print(request.user.id)
                print(request.user.username)
                id = request.user.id
                print(id)

                print(True)
                pm = ProfModel.objects.get(user=id)
                print(pm.mob)
                print(pm.add)
                ps = ProfSerializers(pm)
                print(ps.data)
                return JsonResponse(ps.data)

            if request.method == 'POST':
                print(request.user.id)
                print(request.user.username)
                id = request.user.id
                print(id)

                print(True)
                #pm = ProfModel.objects.get(user=id)
                #print(pm.mob)
                #print(pm.add)
                pm=request.data
                ps = ProfSerializers(data=pm)
                if ps.is_valid():
                    ps.save()
                    print(ps.data)
                    return JsonResponse({"message":"Data created"})
                else:
                    return JsonResponse({'message':ps.errors})

            if request.method == 'PUT':
                id = request.data.get('id')
                pm = ProfModel.objects.get(pk=id)
                ps = ProfSerializers(pm, data=request.data, partial=True)
                if ps.is_valid():
                    ps.save()
                    return Response({"msg": "Data is updated"})
                return Response(ps.errors)

            if request.method == "DELETE":
                id = request.data.get('id')
                pm = ProfModel.objects.get(pk=id)
                pm.delete()
                return Response({'msg': "Data Deleted"})




    except:

        return JsonResponse({'message': 'Not authenticated'})

    # if request.method=='POST':
    #     try:
    #         if request.user.is_authenticated:
    #             print(request.user.id)
    #             print(request.user.username)
    #             id = request.user.id
    #             print(id)
    #
    #             print(True)
    #             # pm = ProfModel.objects.get(user=id)
    #             # print(pm.mob)
    #             # print(pm.add)
    #             pm=request.data
    #             ps = ProfSerializers(pm)
    #             print(ps.data)
    #             return JsonResponse({"message":"Data created"})
    #
    #     except:
    #
    #         return JsonResponse({'message': 'Not authenticated'})
    #
    #


















