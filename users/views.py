from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success': True, 'message': '회원가입이 완료되었습니다.', 'redirect': '/users/signin/'})
        else:
            return Response({'success': False, 'message': '회원가입에 실패했습니다.', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        return render(request, 'signup.html')
    
@csrf_exempt
@api_view(['POST', 'GET'])
def signin(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response({'result': True, 'redirect': '/users/signin/'})
        else:
            return Response({'result': False, 'message': '이메일 또는 비밀번호가 잘못되었습니다.'})

    elif request.method == 'GET':
        return render(request, 'signin.html')

@api_view(["GET", "PATCH"])
@login_required(login_url="/users/signin/")
def profile(request):
    user = request.user
    if request.method == "GET":
        serializer = UserSerializer(user)
        return render(request, "profile.html", {"user": serializer.data})
    elif request.method == "PATCH":
        serializer = UserSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            for field in request.data.keys():
                if field != "password":
                    setattr(user, field, request.data[field])
                else:
                    user.set_password(request.data[field])
            user.save()
            return Response({"result": True, "statusCode": 200, "message": "회원 정보 수정이 완료되었습니다."})
        else:
            return Response({"result": False, "statusCode": 400, "message": "에러가 발생했습니다."})

@api_view(["DELETE"])
@login_required(login_url="/users/signin/")
def delete_user(request):
    user = request.user
    user.delete()
    logout(request)
    return Response({"message": "회원 탈퇴가 완료되었습니다."})


@api_view(["POST"])
def signout(request):
    if request.method == 'POST':
        logout(request)
        return Response({'result': True, 'redirect': '/users/signin/'})
    else:
        return Response({'result': False, 'message': '잘못된 요청입니다.'})
