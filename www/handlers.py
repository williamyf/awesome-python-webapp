import time
from models import User, Blog
from coroweb import get, post


@get('/')
def index(request):
    summary='''Shit, The problem is just here! I got a run error when I started the app. It confuse me for a long time.
    Eventually, I found it out by using a tool named "Beyond.Compare_2.4.3.243_SC-special.exe". With the tool I found a
    hidden tab char. It cause the indentation error!'''
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
	# users = yield from User.findAll()
	# return {
	# 	'__template__' : 'test.html',
	# 	'users' : users
	# }

@get('/blog/{id}')
def get_blog(id):
	pass





















		