from django.db import models

class SuperAdmin(models.Model):
	username = models.CharField(max_length = 10, primary_key = True)
	password = models.CharField(max_length = 16)

	def __unicode__(self):
		return self.username

class SystemAdmin(models.Model):
	username = models.CharField(max_length = 10, primary_key = True)
	password = models.CharField(max_length = 16)
	name = models.CharField(max_length = 12)
	gender = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 40)
	id_card = models.CharField(max_length = 18)
	note = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.username

class OtherAdmin(models.Model):
	username = models.CharField(max_length = 10, primary_key = True)
	password = models.CharField(max_length = 16)
	name = models.CharField(max_length = 12)
	admin_tyep = models.CharField(max_length = 10)
	gender = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 40)
	id_card = models.CharField(max_length = 18)
	note = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.username

class User(models.Model):
	# birthday type, is_Vip, is_Black, is_verified type
	username = models.CharField(max_length = 10, primary_key = True)
	password = models.CharField(max_length = 16)
	name = models.CharField(max_length = 12)
	gender = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 40)
	birthday = models.CharField(max_length = 20)
	phone = models.CharField(max_length = 11)
	address = models.CharField(max_length = 40)
	id_card = models.CharField(max_length = 18)
	is_VIP = models.CharField(max_length = 10)
	is_Black = models.CharField(max_length = 10)
	is_verified = models.CharField(max_length = 10)
	note = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.username

class Dispute(models.Model):
	# date type, state type
	date = models.CharField(max_length = 100)
	username = models.CharField(max_length = 10)
	content = models.CharField(max_length = 200)
	state = models.CharField(max_length = 10)
	result = models.CharField(max_length = 200, null = True)
	def __init__(self):
		self.state = False

class Verification(models.Model):
	# state type
	username = models.CharField(max_length = 10, primary_key = True)
	id_copy = models.ImageField(upload_to = '/home/xczhu/ops/')
	state = models.CharField(max_length = 10)
	def __init__(self):
		self.state = False

	def __unicode__(self):
		return self.username