from models import User
from coroweb import get, post


@get('/')
def index(request):
	users = yield from User.findAll()
	return {
		'__template__' : 'test.html',
		'users' : users
	}

@get('/blog/{id}')
def get_blog(id):
	pass





















		