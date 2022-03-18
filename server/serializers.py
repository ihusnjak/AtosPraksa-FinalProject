from rest_framework import serializers
from server.models import Game, Move


class MoveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Move
		fields = ["move_number", "affected_field"]


class GameSerializer(serializers.ModelSerializer):
	moves = MoveSerializer(many=True)

	class Meta:
		model = Game
		fields = '__all__'

	def create(self, validated_data):
		moves = validated_data.pop('moves')
		game = Game.objects.create(**validated_data)
		for move in moves:
			Move.objects.create(game_id=game.id, **move)
		return game
