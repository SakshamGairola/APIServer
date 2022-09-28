from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from APIServer.models import Banks, Branches
from APIServer.serializers import BanksSerializers, BranchesSerializers


# def apiendpoint(request):
#     if request.method == 'GET':
#         banks = Banks.objects.all()
#         banks_serializers = BanksSerializers(banks, many=True)
#         return JsonResponse(banks_serializers.data, safe=False)


def apiRestEndpoint(request, branch):
    if request.method == 'GET':
        branch = Branches.objects.filter(branch=branch)
        branches_serializers = BranchesSerializers(branch, many=True)
        return JsonResponse(branches_serializers.data, safe=False)
    elif request.method == 'POST':
        getBranch = JSONParser().parse(request).get("branch")
        branch = Branches.objects.filter(branch=getBranch)
        branches_serializers = BranchesSerializers(branch, many=True)
        return JsonResponse(branches_serializers.data, safe=False)
