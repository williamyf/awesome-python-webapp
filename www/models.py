import time, uuid
from orm import Model, StringField, IntegerField, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
	"""用户表"""
	__table__ = 'users'
	# 此处字段需与数据库表中字段一一对应，否则将会出现“找不到指定列”的错误❌
	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	email = StringField(ddl='varchar(50)')
	passwd = StringField(ddl='varchar(50)')
	name = StringField(ddl='varchar(50)')
	image = StringField(ddl='varchar(500)')
	admin = BooleanField()
	created_at = FloatField(default=time.time)

class Blog(Model):
	'博客'
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	user_id = StringField(ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	created_at = FloatField(default=time.time)

class Comment(Model):
	"""评论"""
	__table__ = 'comments'


	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	blog_id = StringField(ddl='varchar(50)')
	user_id = StringField(ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	blog_image = StringField(ddl='varchar(500)')
	content = TextField()
	created_at = FloatField(default=time.time)















