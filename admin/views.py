from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from admin.models import SuperAdmin
from admin.models import SystemAdmin
from admin.models import OtherAdmin
from admin.models import User
from admin.models import Dispute
from admin.models import Verification
from django.utils import simplejson
from django.contrib.auth import logout

@csrf_exempt
# login page of super admin and system admin 
# do the login authtication 
def index(request):
	# the format checked before
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		admin_type = request.POST['admin_type']

		if admin_type == "0":
			# super administrator
			try:
				admin = SuperAdmin.objects.get(pk = username)
				if admin.password == password:
					response = HttpResponseRedirect('super/')
					# set cookie and session
					response.set_cookie("username", username)
					request.session['username'] = username
					return response
				else:
					message = "Wrong password"
			except SuperAdmin.DoesNotExist:
				message = "Username does not exist"
		elif admin_type == "1":
			# system administrator
			try:
				admin = SystemAdmin.objects.get(pk = username)
				if admin.password == password:
					response = HttpResponseRedirect('system/')
					# set cookie and session
					response.set_cookie("username", username)
					request.session['username'] = username
					return response
				else:
					message = "Wrong password"
			except:
				message = "Username does not exist"
		else:
			message = "Please chose the administrator type"
	else:
		return render(request, 'admin/index.html')

	# print the error message if it has
	return render(request, 'admin/index.html', {'message': message})

def admin_logout(request):
	logout(request)
	return HttpResponseRedirect('/admin/')

# super admin interface
# list the brief infomation of all system admin and the operation of view, delete, update
# can also insert and select
def super_interface(request):
	# check cookie
	if 'username' in request.COOKIES:
		if request.session['username'] == request.COOKIES["username"]:
			# has logined
			latest_admin_list = SystemAdmin.objects.all()
			context = {'latest_admin_list': latest_admin_list}
			return render(request, 'admin/super_interface.html', context)

	# back to the login page
	return HttpResponseRedirect('/admin/')


# select a system admin by username
def select_system_admin(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				username = request.POST['username']
				try:
					# get the admin from database by primary key
					admin = SystemAdmin.objects.get(pk = username)
					return render(request, 'admin/detail.html', {'admin': admin})
				except SystemAdmin.DoesNotExist:
					message = "Username does not exist"
			else:
				return render(request, 'admin/select.html')

			return render(request, 'admin/select.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


# add a system admin 
def insert_system_admin(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				username = request.POST['username']
				try:
					admin = SystemAdmin.objects.get(pk = username)
					message = "Username already exist"
					return render(request, 'admin/insert.html', {'message': message})
				except SystemAdmin.DoesNotExist:
					system_admin = SystemAdmin(username = request.POST['username'], password = request.POST['password'], 
						name = request.POST['name'], gender = request.POST['gender'], email = request.POST['email'], 
						id_card = request.POST['id_card'], note = request.POST['note'])
					system_admin.save()
					message = "Insert successfully"
			else:
				return render(request, 'admin/insert.html')

			return render(request, 'admin/insert.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


@csrf_exempt
# show the detail information of a system admin
def detail_system_admin(request, username):
	#if 'username' in request.COOKIES:
		if request.session['username'] == request.COOKIES["username"]:
			admin = get_object_or_404(SystemAdmin, pk = username)
			return render(request, 'admin/detail.html', {'admin': admin})

	#return HttpResponseRedirect('/admin/')


def delete_system_admin(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			try:
				admin = SystemAdmin.objects.get(pk = username)
				admin.delete()
				message = "Delete successfully"
			except SystemAdmin.DoesNotExist:
				message = "Delete failed"
			return render(request, 'admin/delete.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


def update_system_admin(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			admin = get_object_or_404(SystemAdmin, pk = username)
			if request.method == "POST":
				try:
					admin = SystemAdmin.objects.get(pk = username)
					admin.password = request.POST['password']
					admin.name = request.POST['name']
					admin.gender = request.POST['gender']
					admin.email = request.POST['email']
					admin.id_card = request.POST['id_card']
					admin.note = request.POST['note']
					admin.save()
					message = "Update successfully"
				except SystemAdmin.DoesNotExist:
					message = "Update failed"

				return render(request, 'admin/edit.html', {'message': message})
			else:
				return render(request, 'admin/update.html', {'admin': admin})

	#return HttpResponseRedirect('/admin/')


def edit_system_admin(request,username):
	#if 'username' in request.COOKIES:
		#if request.session['username'] == request.COOKIES["username"]:
			admin = get_object_or_404(SystemAdmin, pk = username)
			return render(request, 'admin/edit.html', {'admin': admin})

	#return HttpResponseRedirect('/admin/')


def system_interface(request):
	#if 'username' in request.COOKIES:
		#if request.session['username'] == request.COOKIES["username"]:
			return render(request, 'admin/system_interface.html')

	#return HttpResponseRedirect('/admin/')


def user_manage(request):
	# check cookie
	#if 'username' in request.COOKIES:
		#if request.session['username'] == request.COOKIES["username"]:
			# has logined
			latest_user_list = User.objects.all()
			context = {'latest_user_list': latest_user_list}
			return render(request, 'admin/user_manage.html', context)

	# back to the login page
	#return HttpResponseRedirect('/admin/')


def select_user(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				username = request.POST['username']
				try:
					# get the user from database by primary key
					user = User.objects.get(pk = username)
					return render(request, 'admin/user_detail.html', {'user': user})
				except User.DoesNotExist:
					message = "Username does not exist"
			else:
				return render(request, 'admin/user_select.html')

			return render(request, 'admin/user_select.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


def insert_user(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				username = request.POST['username']
				try:
					user = User.objects.get(pk = username)
					message = "Username already exist"
					return render(request, 'admin/user_insert.html', {'message': message})
				except User.DoesNotExist:
					user = User(username = request.POST['username'], password = request.POST['password'], 
						name = request.POST['name'], gender = request.POST['gender'], email = request.POST['email'], 
						birthday = request.POST['birthday'], phone = request.POST['phone'], address = request.POST['address'],
						id_card = request.POST['id_card'], is_VIP = request.POST['is_VIP'], is_Black = request.POST['is_Black'], 
						is_verified = request.POST['is_verified'], note = request.POST['note'])
					user.save()
					message = "Insert successfully"
			else:
				return render(request, 'admin/user_insert.html')

			return render(request, 'admin/user_insert.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


# show the detail information of a user
def detail_user(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			user = get_object_or_404(User, pk = username)
			return render(request, 'admin/user_detail.html', {'user': user})

	#return HttpResponseRedirect('/admin/')


def delete_user(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			try:
				user = User.objects.get(pk = username)
				user.delete()
				message = "Delete successfully"
			except User.DoesNotExist:
				message = "Delete failed"
			return render(request, 'admin/user_delete.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


def update_user(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			user = get_object_or_404(User, pk = username)
			if request.method == "POST":
				try:
					user = User.objects.get(pk = username)
					user.password = request.POST['password']
					user.name = request.POST['name']
					user.gender = request.POST['gender']
					user.email = request.POST['email']
					user.birthday = request.POST['birthday']
					user.phone = request.POST['phone']
					user.address = request.POST['address']
					user.id_card = request.POST['id_card']
					user.is_VIP = request.POST['is_VIP']
					user.is_Black = request.POST['is_Black']
					user.note = request.POST['note']
					user.save()
					message = "Update successfully"
				except User.DoesNotExist:
					message = "Update failed"

				return render(request, 'admin/user_edit.html', {'message': message})
			else:
				return render(request, 'admin/user_update.html', {'user': user})

	#return HttpResponseRedirect('/admin/')


def edit_user(request,username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			user = get_object_or_404(User, pk = username)
			return render(request, 'admin/user_edit.html', {'user': user})

	#return HttpResponseRedirect('/admin/')


def other_admin(request):
	# check cookie
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			# has logined
			latest_admin_list = OtherAdmin.objects.all()
			context = {'latest_admin_list': latest_admin_list}
			return render(request, 'admin/other_admin.html', context)

	# back to the login page
	#return HttpResponseRedirect('/admin/')


def select_other_admin(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				username = request.POST['username']
				try:
					# get the admin from database by primary key
					admin = OtherAdmin.objects.get(pk = username)
					return render(request, 'admin/other_detail.html', {'admin': admin})
				except OtherAdmin.DoesNotExist:
					message = "Username does not exist"
			else:
				return render(request, 'admin/other_select.html')

			return render(request, 'admin/other_select.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


# add an other admin 
def insert_other_admin(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				username = request.POST['username']
				try:
					admin = OtherAdmin.objects.get(pk = username)
					message = "Username already exist"
					return render(request, 'admin/other_insert.html', {'message': message})
				except OtherAdmin.DoesNotExist:
					other_admin = OtherAdmin(username = request.POST['username'], password = request.POST['password'], 
						name = request.POST['name'], admin_type = request.POST['admin_type'], gender = request.POST['gender'], 
						email = request.POST['email'], id_card = request.POST['id_card'], note = request.POST['note'])
					other_admin.save()
					message = "Insert successfully"
			else:
				return render(request, 'admin/other_insert.html')

			return render(request, 'admin/other_insert.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


# show the detail information of an other admin
def detail_other_admin(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			admin = get_object_or_404(OtherAdmin, pk = username)
			return render(request, 'admin/other_detail.html', {'admin': admin})

	#return HttpResponseRedirect('/admin/')


def delete_other_admin(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			try:
				admin = OtherAdmin.objects.get(pk = username)
				admin.delete()
				message = "Delete successfully"
			except OtherAdmin.DoesNotExist:
				message = "Delete failed"
			return render(request, 'admin/other_delete.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


def update_other_admin(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			admin = get_object_or_404(OtherAdmin, pk = username)
			if request.method == "POST":
				try:
					admin = OtherAdmin.objects.get(pk = username)
					admin.password = request.POST['password']
					admin.name = request.POST['name']
					admin.admin_type = request.POST['admin_type']
					admin.gender = request.POST['gender']
					admin.email = request.POST['email']
					admin.id_card = request.POST['id_card']
					admin.note = request.POST['note']
					admin.save()
					message = "Update successfully"
				except OtherAdmin.DoesNotExist:
					message = "Update failed"

				return render(request, 'admin/other_edit.html', {'message': message})
			else:
				return render(request, 'admin/other_update.html', {'admin': admin})

	#return HttpResponseRedirect('/admin/')


def edit_other_admin(request,username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			admin = get_object_or_404(OtherAdmin, pk = username)
			return render(request, 'admin/other_edit.html', {'admin': admin})

	#return HttpResponseRedirect('/admin/')


def dispute_manage(request):
	# check cookie
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				temp = simplejson.loads(request.body.decode('GBK'))
				dispute = Dispute(date = temp['date'], username = temp['username'], content = temp['content'])
				dispute.save()
				latest_dispute_list = Dispute.objects.order_by('id')
				context = {'latest_dispute_list': latest_dispute_list}
				return render(request, 'admin/dispute_manage.html', context)
			else:
				latest_dispute_list = Dispute.objects.order_by('id')
				context = {'latest_dispute_list': latest_dispute_list}
				return render(request, 'admin/dispute_manage.html', context)

	# back to the login page
	#return HttpResponseRedirect('/admin/')


# select a dispute information by id
def select_dispute(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				dispute_id = request.POST['id']
				try:
					# get the dispute from database by primary key
					dispute= Dispute.objects.get(pk = dispute_id)
					return render(request, 'admin/dispute_result.html', {'dispute': dispute})
				except Dispute.DoesNotExist:
					message = "Id does not exist"
			else:
				return render(request, 'admin/dispute_select.html')

			return render(request, 'admin/dispute_select.html', {'message': message})

	#return HttpResponseRedirect('/admin/')


def result_dispute(request, dispute_id):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				dispute = get_object_or_404(Dispute, pk = dispute_id)
				dispute.result = request.POST['result']
				dispute.save()
				return render(request, 'admin/dispute_result.html', {'dispute': dispute})
			else:
				dispute = get_object_or_404(Dispute, pk = dispute_id)
				return render(request, 'admin/dispute_result.html', {'dispute': dispute})

	#return HttpResponseRedirect('/admin/')


def verification(request):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				temp = simplejson.loads(request.body.decode('GBK'))
				verification = Verification(username = temp['username'], id_copy = temp['id_copy'])
				verification.save()
				latest_verification_list = Verification.objects.all()
				context = {'latest_verification_list': latest_verification_list}
				return render(request, 'admin/verification.html', context)
			else:
				latest_verification_list = Verification.objects.all()
				context = {'latest_verification_list': latest_verification_list}
				return render(request, 'admin/verification.html', context)

	# back to the login page
	#return HttpResponseRedirect('/admin/')


def verify(request, username):
	#if 'username' in request.COOKIES:
	#	if request.session['username'] == request.COOKIES["username"]:
			if request.method == "POST":
				user = get_object_or_404(User, pk = username)
				user.is_verified = request.POST['verify']
				user.save()
				verification.get_object_or_404(Verification, pk = username)
				verification.state = True
				verification.save()
				return render(request, 'admin/verify.html', {'verification': verification})
			else:
				verification = get_object_or_404(Verification, pk = username)
				return render(request, 'admin/verify.html', {'verification': verification})

	#return HttpResponseRedirect('/admin/')