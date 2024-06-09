# backend/api/views.py

from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer

class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'message': 'Account Does Not Exist'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            code = random.randint(100000, 999999)
            user.profile.reset_code = code
            user.profile.save()
            send_mail(
                'Password Reset Code',
                f'Your password reset code is {code}',
                'noreply@kobracoding.tech',  # Your verified email address
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset code sent to email'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)

class VerifyResetCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        try:
            user = User.objects.get(email=email)
            if user.profile.reset_code == code:
                return Response({'message': 'Code verified successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid reset code'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        new_password = request.data.get('new_password')
        try:
            user = User.objects.get(email=email)
            if user.profile.reset_code == code:
                user.set_password(new_password)
                user.save()
                user.profile.reset_code = None
                user.profile.save()
                return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid reset code'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)
