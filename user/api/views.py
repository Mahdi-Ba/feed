import hashlib
import time


from .userservice import JWTSimpleUserService
from django.utils.translation import gettext as _
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class LoginRigisterRateThrottle(UserRateThrottle):
    rate = '4/minute'





@permission_classes((AllowAny,))
class UserRegister(APIView):
    throttle_classes = [LoginRigisterRateThrottle]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            jwt_simple = JWTSimpleUserService().create_user(request.data['username'], request.data['password'],
                                                            request.data)
            return Response({
                'success': True,
                'data': {
                    'token': jwt_simple.get_token(),
                    'user_info': UserSerializer(jwt_simple.user).data

                },
                'message': _('welcome to Digi_Cloud'),
                'dev_message': 'token generate'

            })
        else:
            return Response(
                {'success': False, 'message': _('something is wrong'), 'data': {'messages': serializer.errors}},
                status.HTTP_400_BAD_REQUEST)



@permission_classes((AllowAny,))
class StaticLogin(APIView):
    throttle_classes = [LoginRigisterRateThrottle]

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            return Response({"success": False, 'dev_message': 'wrong functionality'
                                , "message": _('your information is not correct'),
                             'data': {'messages': login_serializer.errors}},
                            status=status.HTTP_400_BAD_REQUEST)
        jwt_simple = JWTSimpleUserService().check_user_authenticate(request.data['username'], request.data['password'])
        if jwt_simple.user:
            return Response({
                'success': True,
                'data': {
                    'token': jwt_simple.get_token(),
                    'user_info': UserSerializer(jwt_simple.user).data

                },
                'message': _('welcome to Digi_Cloud'),
                'dev_message': 'token generate'

            })
        else:
            return Response({
                'success': False,
                'message': _("Incorrect Info"),
                'dev_message': 'mistake user and pass'
            }, status=status.HTTP_401_UNAUTHORIZED)
