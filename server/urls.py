from django.urls import path
from .views import Games


app_name = 'games'

urlpatterns = [
	path(f'{app_name}', Games.as_view(), name='games'),
	path(f'{app_name}/<int:game_id>', Games.as_view(), name='games_by_id'),
	path(f'{app_name}/<str:user>', Games.as_view(), name='games_by_user'),
]
