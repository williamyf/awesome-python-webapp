# coding=utf-8
# 高阶函数(Higher-order function)
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 一个最简单大高阶函数：

def add (x,y,f):
	return f(x) + f(y)

x = -5
y = 6
f = abs
print add(-5,6,f)

def f(x):
	return x*x

arr = [1,2,3,4,5,6,7,8,9]
r = map(f,arr)
print r
print list(r)
print map(str,arr)

def fn(x,y):
	return x*10 + y

print reduce(fn,[1,3,5,7,9])

def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))

print str2int('23434')

def normalize(name):
	l = name[:1]
	r = name[1:]
	return l.upper()+r.lower()
print map(normalize,['adam','LISA','barT'])


def prod(ls):
	return reduce(lambda x,y : x*y, ls);

print prod([1,2,3,4])

print prod;
print prod.__name__

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper
@log
def now():
	print '2016-07-18'

now()






