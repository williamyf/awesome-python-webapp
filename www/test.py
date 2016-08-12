import asyncio, orm, sys
from models import User, Blog, Comment

def test(loop):
	yield from orm.create_pool(loop=loop, user='root', password='123456', db='awesome')

	# 对象里的属性可以任意指定，不必非要与数据库中字段对应，只不过若不对应，则会采用默认值
	u = User(name='Test1', email='example5', passwd='1234567890', image='about:blank')
	yield from u.save()

if __name__ == '__main__':

	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	#loop.run_forever()  # 进程不会退出
	loop.close()
	if loop.is_closed():
		sys.exit(0)