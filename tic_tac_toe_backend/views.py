from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def IndexView(request):
	content = {
		'message': f'Hello World from {request.method} method.',
		'data': 'We have no data for you...'
	}
	if request.method == 'POST':
		content = {
			'message': 'Got some data!',
			'data': request.data
		}
		return Response(content)
	return Response(content)
