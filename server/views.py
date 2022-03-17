from rest_framework.views import APIView
from .serializers import GameSerializer
from rest_framework.response import Response
from rest_framework import status


class PostGame(APIView):
	def post(self, request):
		gameSerializer = GameSerializer(data=request.data, many=True)
		if gameSerializer.is_valid():
			gameSerializer.save()
			return Response(gameSerializer.data, status=status.HTTP_201_CREATED)
		return Response(gameSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
