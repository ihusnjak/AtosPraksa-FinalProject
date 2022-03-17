from rest_framework.views import APIView
from .serializers import GameSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Game


class PostGame(APIView):
	def post(self, request):
		gameSerializer = GameSerializer(data=request.data, many=True)
		if gameSerializer.is_valid():
			gameSerializer.save()
			return Response(gameSerializer.data, status=status.HTTP_201_CREATED)
		return Response(gameSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetGames(request, game_id=None, user=None):
	content = {}
	if user:
		try:
			games = None
			serializer = None
			filter_param = (Q(player1=user) | Q(player2=user))
			try:
				games = Game.objects.filter(filter_param).get()
				serializer = GameSerializer(games, many=False)
				return Response(serializer.data, status=status.HTTP_200_OK)
			except Game.MultipleObjectsReturned:
				games = Game.objects.filter(filter_param).all()
				serializer = GameSerializer(games, many=True)
				return Response(serializer.data, status=status.HTTP_200_OK)
		except Game.DoesNotExist:
			content['no_games'] = f'User {user} has no played games.'
			return Response(content, status=status.HTTP_204_NO_CONTENT)
	elif game_id:
		try:
			game = Game.objects.filter(id=game_id).get()
			serializer = GameSerializer(game, many=False)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except Game.DoesNotExist:
			content['no_games'] = f'Game with id {game_id} does not exist.'
			return Response(content, status=status.HTTP_204_NO_CONTENT)
	else:
		games = Game.objects.all()
		if games.count() <= 0:
			content['no_games'] = f'No games in the database.'
			return Response(content, status=status.HTTP_204_NO_CONTENT)
		serializer = GameSerializer(games, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
