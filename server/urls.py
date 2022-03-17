from django.urls import path
from .views import (
	PostGame,
	GetGames,
	DeleteGames,
)


app_name = 'games'

urlpatterns = [
	path(f'{app_name}/post_json_game', PostGame.as_view(), name='post_game'),
	path(f'{app_name}/get_games', GetGames, name='get_all_games'),
	path(f'{app_name}/get_games/<int:game_id>', GetGames, name='get_game_by_id'),
	path(f'{app_name}/get_games/<str:user>', GetGames, name='get_games_by_user'),
	path(f'{app_name}/delete_games', DeleteGames, name='delete_all_games'),
	path(f'{app_name}/delete_games/<int:game_id>', DeleteGames, name='delete_game_by_id'),
	path(f'{app_name}/delete_games/<str:user>', DeleteGames, name='delete_games_by_user'),
]
