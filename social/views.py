import base64
import clearbit
from.utils import ehunter
from django.conf import settings
from .models import Post,Like,UserProfile
from .serializers import PostsSerializer, UserRegisterSerializer,UserLoginSerializer, TokenSerializer, LikeSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics , permissions , status, viewsets
from rest_framework_jwt.settings import api_settings

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        post = Post.objects.create(
            author_id=request.user.id,
            title=request.data["title"],
            text=request.data["text"]
        )
        return Response(
            data=PostsSerializer(post).data,
            status=status.HTTP_201_CREATED
        )

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        post = self.get_object()

        like, created = Like.objects.get_or_create(post=post, user=request.user)

        # Notify about an already existing like
        if not created:
            return Response({'error': 'Like already placed.'}, status=status.HTTP_409_CONFLICT)

        serializer = LikeSerializer(like, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['DELETE'], detail=True)
    def unlike(self, request, pk=None):
        post = self.get_object()

        result = Like.objects.filter(post=post, user=request.user).delete()

        return Response(result)


class RegisterUsers(generics.CreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        """
        Check if email provider is real. 
        Unfortunately since I've reached my limit of Api calls I had to comment this line of code.
        """

        # ehunter_response = ehunter.email_verifier(request.data.get("email"))
        # if ehunter_response['result'] == 'undeliverable':
            # return Response('Email provider does not exist!', status=status.HTTP_400_BAD_REQUEST)

        """
        Same goes here for clearbit.  
        
        """
        # clearbit_response = clearbit.Enrichment.find(email=request.data["email"], stream=True)

        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )

        # enrichment_data = clearbit_response["company"]["category"]["industry"]
        # UserProfile.objects.create(user=new_user, enrichment_data=enrichment_data)

        return Response(
            data=UserRegisterSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_token
            })
            login(request, user)
            serializer.is_valid()
            return Response({"token": jwt_token})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
