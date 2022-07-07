from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post, PostLike


class PostCreateAPIView(APIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            post = serializer.save()
            post.owner = request.user
            post.save()
            return Response({"Success": "Created."}, status=201)
        else:
            return Response(serializer.errors, status=400)


class PostLikesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        try:
            post_like = PostLike.objects.get(post=post, user=request.user)
            post_like.delete()
        except PostLike.DoesNotExist:
            PostLike.objects.create(post=post, user=request.user)
        return Response({'like': post.likes}, status=200)
