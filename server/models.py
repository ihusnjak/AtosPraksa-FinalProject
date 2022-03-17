from django.db import models


class Game(models.Model):
	player1						= models.CharField(max_length=30, blank=False, null=False)
	player2						= models.CharField(max_length=30, blank=False, null=False)
	winner						= models.CharField(max_length=30, blank=False, null=False)

	def __str__(self):
		return f'{self.player1} vs {self.player2} -> {self.winner}'


class Move(models.Model):
	move_number					= models.IntegerField()
	affected_field				= models.IntegerField()
	game						= models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE, blank=False, null=False)

	def __str__(self):
		return str(f'Move: {self.move_number} on field {self.affected_filed}')
