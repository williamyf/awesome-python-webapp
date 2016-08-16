from datetime import datetime
import time, functools

def log(param):
	if callable(param):
		@functools.wraps(param)
		def wrapper(*args, **kw):
			print('begin call %s():' % param.__name__)
			r = param(*args, **kw)
			print('end call %s():' % param.__name__)
			return r
		return wrapper
	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('begin %s %s():' % (param, func.__name__))
				r = func(*args, **kw)
				print('end %s %s():' % (param, func.__name__))
				return r
			return wrapper
		return decorator

@log
def now():
	print(datetime.fromtimestamp(time.time()))

@log('execute')
def printany(*args, **kw):
	print(args)
	print(kw)

print(now.__name__)
now()

print(printany.__name__)
printany(1,2,a=1,b=2)

