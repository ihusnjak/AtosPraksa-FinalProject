from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Game
from .serializers import GameSerializer


client = Client()


class GetAllGamesTest(TestCase):

	def setUp(self):
		Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer2')
		Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer1')
		Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer1')
		Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer2')

	def test_get_all_games(self):
		response = client.get(reverse('games:games'))
		games = Game.objects.all()
		serializer = GameSerializer(games, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleGameTest(TestCase):

	def setUp(self):
		self.game1 = Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer2')
		self.game2 = Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer1')
		self.game3 = Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer1')
		self.game4 = Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer2')

	def test_get_valid_single_game(self):
		response = client.get(
			reverse('games:games_by_id', kwargs={'game_id':self.game2.pk}))
		game = Game.objects.get(pk=self.game2.pk)
		serializer = GameSerializer(game)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_single_game(self):
		response = client.get(
			reverse('games:games_by_id', kwargs={'game_id':30}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateNewGame(TestCase):

	def setUp(self):
		json_create_valid_data = open('server/test/create_valid.json')
		self.valid_payload = json.load(json_create_valid_data)
		json_create_invalid_data = open('server/test/create_invalid.json')
		self.invalid_payload = json.load(json_create_invalid_data)

	def test_create_valid_game(self):
		response = client.post(
			reverse('games:games'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_game(self):
		response = client.post(
			reverse('games:games'),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleGameByIDTest(TestCase):

	def setUp(self):
		self.game1 = Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer2')
		self.game2 = Game.objects.create(
			player1='TestPlayer1', player2='TestPlayer2', winner='TestPlayer1')

	def test_valid_delete_game(self):
		response = client.delete(
			reverse('games:games_by_id', kwargs={'game_id': self.game1.pk}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_delete_game(self):
		response = client.delete(
			reverse('games:games_by_id', kwargs={'game_id': 30}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
