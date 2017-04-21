import json
import datetime
from django.test import TestCase
from django.core.mail import send_mail
from django.http import HttpResponse, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User, Permission
from django.contrib.auth.hashers import make_password, MD5PasswordHasher
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
#from django.core.context_processors import csrf
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from decimal import Decimal, ROUND_UP
from .models import DIM_GST, DIM_Unit, DIM_Contact_Type, Contact_Info, Tax, Customer, Supplier, Inventory, Price, Review, Purchase, Purchase_Det, Sales,  Sales_Det, DIM_Promotion, State, DocNo, DIM_Category, WebTemplate, DIM_SubCategory
from .forms import Contact_InfoForm, CustomerForm, SupplierForm, InventoryForm, DIM_UnitForm, TaxForm, Contact_TypeForm, DIM_GSTForm, DIM_PromotionForm, SalesForm, PurchaseForm, Sales_DetForm, Purchase_DetForm, StateForm, DocNoForm, PriceForm, UserForm, UserProfileForm, RegistrationForm, DIM_CategoryForm, WebTemplateForm, DIM_SubCategoryForm
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import DIM_GSTSerializer
from django.template import RequestContext 

cartAmt=0
# Create your views here.

# Authenticate user
def authUser(request):
	if request.user.is_authenticated():
		return true
	else:
		raise Http404('User not authorised')

#index
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	list = Inventory.objects.all()
	print(str(list))
	context = {'list': list, 'title':'Home'}
	return render(request, 'retail/index.html', context)

def index(request):
	list = Inventory.objects.values('id', 'code', 'description', 'imgFile', 'remark', 'dim_unit__code', 'price__inventory', 'price__unit_price').all()
	print(str(list))
	# data2 = serializers.serialize('json', [sales_det])

	context = {'list': list, 'title':'Home'}
	return render(request, 'retail/index.html', context)

def about(request):
	list = {} #Inventory.objects.values('id', 'code', 'description', 'imgFile', 'remark', 'dim_unit__code', 'price__inventory', 'price__unit_price').all()
	print(str(list))
	# data2 = serializers.serialize('json', [sales_det])

	context = {'list': list, 'title':'About Us'}
	return render(request, 'retail/about.html', context)

def contact(request):
	
	context = {}
	return render(request, 'retail/contact.html', context)

def dashboard(request):
	list = Inventory.objects.values('id', 'code', 'description', 'imgFile', 'remark', 'dim_unit__code', 'price__inventory', 'price__unit_price').all()
	print(str(list))
	# data2 = serializers.serialize('json', [sales_det])

	context = {'list': list, 'title':'Dashboard'}
	return render(request, 'dashboard/index.html', context)

def login(request):

	form = UserForm()
	context = {"form":form}
	return render(request, 'retail/login.html', context)


#GST
def gst_list(request):
	list = DIM_GST.objects.all()
	context = {'list': list, 'title':'GST List1', 'object_name':'DIM_GST'}
	#return Response(gst.code for gst in list)
	return render(request, 'retail/gst_list.html', context)
	
def gst_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			gst=DIM_GST.objects.get(pk=pk)

		else:
			gst=DIM_GST()

		form = DIM_GSTForm(request.POST, instance=gst)
		
		if form.is_valid():
			gst=form.save(commit=False)
			gst.updated_datetime=timezone.now()
			gst.save()
			
			return redirect('gst_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			gst=DIM_GST.objects.get(pk=pk)
			title = 'New GST'
		else:
			gst=DIM_GST()
			title = 'Edit GST'

	form = DIM_GSTForm(instance=gst)
			
		
	context = {'form': form, 'title':title, 'back_url':'gst_list'} 
	
	return render(request, 'retail/gst_edit.html', context)

def gst_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	gst=DIM_GST.objects.get(pk=pk)

	if request.method == 'POST':
	
		gst.delete()
	
	else:

		context = {'gst': gst, 'title':'Delete GS', 'back_url':'gst_list'} 
	
		return render(request, 'retail/gst_delete.html', context)
		
				
	return redirect('gst_list')

#DocNo
def docno_list(request):
	list = DocNo.objects.all()
	context = {'list': list, 'title':'Document No List', 'object_name':'DocNo'}
	return render(request, 'retail/docno_list.html', context)
	
def docno_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			docno=DocNo.objects.get(pk=pk)

		else:
			docno=DocNo()

		form = DocNoForm(request.POST, instance=docno)
		
		if form.is_valid():
			docno=form.save(commit=False)
			docno.updated_datetime=timezone.now()
			docno.save()
			
			return redirect('docno_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			docno=DocNo.objects.get(pk=pk)
			title = 'New Document No'
		else:
			docno=DocNo()
			title = 'Edit Document No'

	form = DocNoForm(instance=docno)
			
		
	context = {'form': form, 'title':title, 'back_url':'docno_list'} 
	
	return render(request, 'retail/docno_edit.html', context)

def docno_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	docno=DocNo.objects.get(pk=pk)

	if request.method == 'POST':
	
		docno.delete()
	
	else:

		context = {'docno': docno, 'title':'Delete Document No', 'back_url':'docno_list'} 
	
		return render(request, 'retail/docno_delete.html', context)
		
				
	return redirect('docno_list')

#State
def state_list(request):
	list = DIM_GST.objects.all()
	context = {'list': list, 'title':'GST List', 'object_name':'DIM_GST'}
	return render(request, 'retail/gst_list.html', context)
	
def state_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			gst=DIM_GST.objects.get(pk=pk)

		else:
			gst=DIM_GST()

		form = DIM_GSTForm(request.POST, instance=gst)
		
		if form.is_valid():
			gst=form.save(commit=False)
			gst.updated_datetime=timezone.now()
			gst.save()
			
			return redirect('gst_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			gst=DIM_GST.objects.get(pk=pk)
			title = 'New GST'
		else:
			gst=DIM_GST()
			title = 'Edit GST'

	form = DIM_GSTForm(instance=gst)
			
		
	context = {'form': form, 'title':title, 'back_url':'gst_list'} 
	
	return render(request, 'retail/gst_edit.html', context)

def state_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	gst=DIM_GST.objects.get(pk=pk)

	if request.method == 'POST':
	
		gst.delete()
	
	else:

		context = {'gst': gst, 'title':'Delete GS', 'back_url':'gst_list'} 
	
		return render(request, 'retail/gst_delete.html', context)
		
				
	return redirect('gst_list')
	
#DIM_Unit
def unit_list(request):
	list = DIM_Unit.objects.all()
	context = {'list': list, 'title':'Unit List', 'object_name':'DIM_Unit'}
	return render(request, 'retail/unit_list.html', context)
	
def unit_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			unit=DIM_Unit.objects.get(pk=pk)

		else:
			unit=DIM_Unit()

		form = DIM_UnitForm(request.POST, instance=unit)
		
		if form.is_valid():
			unit=form.save(commit=False)
			unit.updated_datetime=timezone.now()
			unit.save()
			
			return redirect('unit_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			unit=DIM_Unit.objects.get(pk=pk)
			title = 'New Unit'
		else:
			unit=DIM_Unit()
			title = 'Edit Unit'

	form = DIM_UnitForm(instance=unit)
			
		
	context = {'form': form, 'title':title, 'back_url':'unit_list'} 
	
	return render(request, 'retail/unit_edit.html', context)

def unit_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	unit=DIM_Unit.objects.get(pk=pk)

	if request.method == 'POST':
	
		unit.delete()
	
	else:

		context = {'unit': unit, 'title':'Delete Unit', 'back_url':'unit_list'} 
	
		return render(request, 'retail/unit_delete.html', context)
		
				
	return redirect('unit_list')

#DIM_Category
def category_list(request):
	list = DIM_Category.objects.all()
	context = {'list': list, 'title':'Category List', 'object_name':'DIM_Category'}
	return render(request, 'retail/category_list.html', context)
	
def category_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			category=DIM_Category.objects.get(pk=pk)

		else:
			category=DIM_Category()

		form = DIM_CategoryForm(request.POST, instance=category)
		
		if form.is_valid():
			category.save()
			
			return redirect('category_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			category=DIM_Category.objects.get(pk=pk)
			title = 'New Category'
		else:
			category=DIM_Category()
			title = 'Edit Category'

	form = DIM_CategoryForm(instance=category)
			
		
	context = {'form': form, 'title':title, 'back_url':'category_list'} 
	
	return render(request, 'retail/category_edit.html', context)

def category_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	category=DIM_Category.objects.get(pk=pk)

	if request.method == 'POST':
	
		category.delete()
	
	else:

		context = {'category': category, 'title':'Delete Category', 'back_url':'category_list'} 
	
		return render(request, 'retail/category_delete.html', context)
		
				
	return redirect('category_list')

#DIM_SubCategory
def subcategory_list(request):
	list = DIM_SubCategory.objects.all()
	context = {'list': list, 'title':'Sub Category List', 'object_name':'DIM_SubCategory'}
	return render(request, 'retail/subcategory_list.html', context)
	
def subcategory_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			subcategory=DIM_SubCategory.objects.get(pk=pk)

		else:
			subcategory=DIM_SubCategory()

		form = DIM_SubCategoryForm(request.POST, instance=subcategory)
		
		if form.is_valid():
			subcategory.save()
			
			return redirect('subcategory_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			subcategory=DIM_SubCategory.objects.get(pk=pk)
			title = 'New Sub-Category'
		else:
			subcategory=DIM_SubCategory()
			title = 'Edit Sub-Category'

	form = DIM_SubCategoryForm(instance=subcategory)
			
		
	context = {'form': form, 'title':title, 'back_url':'subcategory_list'} 
	
	return render(request, 'retail/subcategory_edit.html', context)

def subcategory_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	subcategory=DIM_SubCategory.objects.get(pk=pk)

	if request.method == 'POST':
	
		subcategory.delete()
	
	else:

		context = {'subcategory': subcategory, 'title':'Delete Sub-Category', 'back_url':'subcategory_list'} 
	
		return render(request, 'retail/subcategory_delete.html', context)
		
				
	return redirect('subcategory_list')
	
#TAX
def tax_list(request):
	list = Tax.objects.all()
	context = {'list': list, 'title':'Tax List', 'object_name':'Tax'}
	return render(request, 'retail/tax_list.html', context)
	
def tax_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			tax=Tax.objects.get(pk=pk)

		else:
			tax=Tax()

		form = TaxForm(request.POST, instance=tax)
		
		if form.is_valid():
			tax=form.save(commit=False)
			tax.updated_datetime=timezone.now()
			tax.save()
			
			return redirect('tax_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			tax=Tax.objects.get(pk=pk)
			title = 'New Tax'
		else:
			tax=Tax()
			title = 'Edit Tax'

	form = TaxForm(instance=tax)
			
		
	context = {'form': form, 'title':title, 'back_url':'tax_list'} 
	
	return render(request, 'retail/tax_edit.html', context)

def tax_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	tax=Tax.objects.get(pk=pk)

	if request.method == 'POST':
	
		tax.delete()
	
	else:

		context = {'tax': tax, 'title':'Delete Tax', 'back_url':'tax_list'} 
	
		return render(request, 'retail/tax_delete.html', context)
		
				
	return redirect('tax_list')

#DIM_Contact_Type
def contacttype_list(request):
	list = DIM_Contact_Type.objects.all()
	context = {'list': list, 'title':'Contact Type List', 'object_name':'contact_type'}
	return render(request, 'retail/contact_type_list.html', context)
	
def contacttype_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			ct=DIM_Contact_Type.objects.get(pk=pk)

		else:
			ct=DIM_Contact_Type()

		form = Contact_TypeForm(request.POST, instance=ct)
		
		if form.is_valid():
			ct=form.save(commit=False)
			ct.updated_datetime=timezone.now()
			ct.save()
			
			return redirect('contact_type_list')
		else:
			return HttpResponse('Save Error')
	
	else:

	
		if pk is not None:
			ct=DIM_Contact_Type.objects.get(pk=pk)
		else:
			ct=DIM_Contact_Type()

	form = Contact_TypeForm(instance=ct)
			
		
	context = {'form': form, 'title':'New Contact Type', 'back_url':'contact_type_list'} 
	
	return render(request, 'retail/contact_type_edit.html', context)

def contacttype_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	ct = DIM_Contact_Type.objects.get(pk=pk)

	if request.method == 'POST':
	
		ct.delete()
	
	else:

		context = {'ct': ct, 'title':'Delete Contact Type', 'back_url':'contact_type_list'} 
	
		return render(request, 'retail/contact_type_delete.html', context)
		
				
	return redirect('contact_type_list')
		

#DIM_Promotion
def promotion_list(request):
	list = DIM_Promotion.objects.all()
	context = {'list': list, 'title':'Promotion List', 'object_name':'DIM_Promotion'}
	return render(request, 'retail/promotion_list.html', context)
	
def promotion_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			promotion=DIM_Promotion.objects.get(pk=pk)

		else:
			promotion=DIM_Promotion()

		form = DIM_PromotionForm(request.POST, instance=promotion)
		
		if form.is_valid():
			promotion=form.save(commit=False)
			promotion.updated_datetime=timezone.now()
			promotion.save()
			
			return redirect('promotion_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			promotion=DIM_Promotion.objects.get(pk=pk)
			title = 'New Promotion'
		else:
			promotion=DIM_Promotion()
			title = 'Edit Promotion'

	form = DIM_PromotionForm(instance=promotion)
			
		
	context = {'form': form, 'title':title, 'back_url':'promotion_list'} 
	
	return render(request, 'retail/promotion_edit.html', context)

def promotion_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	promotion=DIM_Promotion.objects.get(pk=pk)

	if request.method == 'POST':
	
		promotion.delete()
	
	else:

		context = {'promotion': promotion, 'title':'Delete Promotion', 'back_url':'promotion_list'} 
	
		return render(request, 'retail/promotion_delete.html', context)
		
				
	return redirect('promotion_list')

# Contact_Info
def contactinfo_list(request):
	list = Contact_Info.objects.all()
	context = {'list': list, 'title':'Contact Info List', 'object_name':'contact_info'}
	return render(request, 'retail/contact_info_list.html', context)
	
def contactinfo_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			ci=Contact_Info.objects.get(pk=pk)

		else:
			ci=Contact_Info()

		form = Contact_InfoForm(request.POST, instance=ci)
		
		if form.is_valid():
			ci=form.save(commit=False)
			ci.updated_datetime=timezone.now()
			ci.save()
			
			return redirect('contact_info_list')
		else:
			return HttpResponse('Save Error')
	
	else:

		#print(request.user.is_authenticated)
		#usr=request.user
		#ci=Contact_Info.objects.get(pk=pk)
		#form = Contact_InfoForm(instance=ci, initial={'user':usr})
		
		usr=User.objects.get(username='fai')

		if pk is not None:
			ci=Contact_Info.objects.get(pk=pk)
		else:
			ci=Contact_Info()

	form = Contact_InfoForm(instance=ci, initial={'user':usr})
			
		
	context = {'form': form, 'title':'New Contact Info', 'back_url':'contact_info_list'} 
	
	return render(request, 'retail/contact_info_edit.html', context)

def contactinfo_delete(request, pk=None):
	print('reached')
	if pk is None:
		print('reached1')
		return HttpResponse('Save Error')
	
	print('reached2')
	
	ci=Contact_Info.objects.get(pk=pk)

	if request.method == 'POST':
		print('reached3')
	
		ci.delete()
	
	else:

		context = {'ci': ci, 'title':'Delete Contact Info', 'back_url':'contact_info_list'} 
	
		return render(request, 'retail/contact_info_delete.html', context)
		
	print('reached4')
				
	return redirect('contact_info_list')
	
# Customer
def customer_list(request):
	list = Customer.objects.all()
	context = {'list': list, 'title':'Customer List', 'object_name':'customer'}
	return render(request, 'retail/customer_list.html', context)
	
def customer_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			customer=Customer.objects.get(pk=pk)

		else:
			customer=Customer()

		form = CustomerForm(request.POST, instance=customer)
		
		if form.is_valid():
			customer=form.save(commit=False)
			customer.updated_datetime=timezone.now()
			customer.save()
			return redirect('customer_view', customer.pk)

			#return redirect('customer_list')
		else:
			return HttpResponse('Save Error')
	
	else:


		price_list=Price.objects.none()
		
		if pk is not None:
			customer=Customer.objects.get(pk=pk)
			
			price_list=Price.objects.filter(customer_id=pk)
			
			if request.resolver_match.url_name=='customer_view' and request.resolver_match.kwargs.get('pk')==pk:
				title="View Customer" 
			else:
				title="Edit Customer" 
			
			
		else:
			customer=Customer()
			title="New Customer"

	form = CustomerForm(instance=customer)
			
	print(customer.id)	
	context = {'form': form, 'title':title, 'back_url':'customer_list', 'price_list':price_list, 'customer_id':customer.id } 
	
	return render(request, 'retail/customer_edit.html', context)

def customer_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	customer = Customer.objects.get(pk=pk)

	if request.method == 'POST':
		customer.delete()
	else:

		context = {'customer': customer, 'title':'Delete Customer', 'back_url':'customer_list'} 
	
		return render(request, 'retail/customer_delete.html', context)
		
				
	return redirect('customer_list')

# Supplier
def supplier_list(request):
	list = Supplier.objects.all()
	context = {'list': list, 'title':'Supplier List', 'object_name':'supplier'}
	return render(request, 'retail/supplier_list.html', context)
	
def supplier_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			supplier=Supplier.objects.get(pk=pk)

		else:
			supplier=Supplier()

		form = SupplierForm(request.POST, instance=supplier)
		
		if form.is_valid():
			supplier=form.save(commit=False)
			supplier.updated_datetime=timezone.now()
			supplier.save()
			
			return redirect('supplier_list')
		else:
			return HttpResponse('Save Error')
	
	else:


		if pk is not None:
			supplier=Supplier.objects.get(pk=pk)
			title="Edit Supplier"
			
		else:
			supplier=Supplier()
			title="New Supplier"

	form = SupplierForm(instance=supplier)
			
		
	context = {'form': form, 'title':title, 'back_url':'supplier_list'} 
	
	return render(request, 'retail/supplier_edit.html', context)

def supplier_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	supplier = Supplier.objects.get(pk=pk)

	if request.method == 'POST':
		supplier.delete()
	else:

		context = {'supplier': supplier, 'title':'Delete Supplier', 'back_url':'supplier_list'} 
	
		return render(request, 'retail/supplier_delete.html', context)
		
				
	return redirect('supplier_list')

# Inventory
def inventory_list(request):
	list = Inventory.objects.all()
	context = {'list': list, 'title':'Inventory List', 'object_name':'Inventory'}
	return render(request, 'retail/inventory_list.html', context)
	
def inventory_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			print('edit inv')
			inventory=Inventory.objects.get(pk=pk)

		else:
			print('new inv')
			
			inventory=Inventory()
			print('new inv2')

		#print(inventory.imgFile)	
		form = InventoryForm(request.POST, request.FILES, instance=inventory)
		
		if form.is_valid():
			print('valid')
			
			print(request.POST)
			#inventory=Inventory(imgFile=request.FILES['imgFile'])
			# inventory=form.save(commit=False)
			# inventory.updated_datetime=timezone.now()
			inventory=form.instance
			inventory.save()
			#del request.session['form_data']
			return redirect('inventory_view', inventory.pk)
			
		else:
			#request.session['form_data'] = request.POST
			context = {'form': form} 
			return render(request, 'retail/inventory_edit.html', context)
	
	else:

		price_list = Price.objects.none()
		
		if pk is not None:
			inventory=Inventory.objects.get(pk=pk)
			price_list = Price.objects.filter(inventory_id = pk)
			
			if request.resolver_match.url_name=='inventory_view' and request.resolver_match.kwargs.get('pk')==pk:
				title="View Inventory" 
			else:
				title="Edit Inventory" 

			
		else:
			inventory=Inventory()
			title="New Inventory"
			
	#form_data = request.session.get('form_data', None)
	
	form = InventoryForm(instance=inventory)

	# if form_data:
		# form = InventoryForm(initial=form_data)
	
			
		
	context = {'form': form, 'title':title, 'back_url':'inventory_list', 'inventory_id': inventory.id, 'price_list':price_list } 
	
	return render(request, 'retail/inventory_edit.html', context)

def inventory_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	inventory = Inventory.objects.get(pk=pk)

	if request.method == 'POST':
		inventory.delete()
	else:

		context = {'inventory': inventory, 'title':'Delete Inventory', 'back_url':'inventory_list'} 
	
		return render(request, 'retail/inventory_delete.html', context)
		
				
	return redirect('inventory_list')

	
#Inventory Web View
def inventory_web_view(request, pk=None, v='c'):

	sales=request.session.get('sales')
	salesItemList=request.session.get('salesItemList')
	salesDet=None
	if salesItemList:
		for sales_det in salesItemList:
		
			if sales_det.inventory_id == str(pk):
				salesDet=sales_det
			
	inventory=Inventory.objects.values('id', 'code', 'description', 'remark', 'imgFile', 'dim_unit__code', 'price__unit_price', 'review__description').get_or_create(pk=pk)[0]
	print(connection.queries)
	context = {'inventory': inventory, 'sales': sales, 'salesDet':salesDet} 
	
	return render(request, 'retail/inventory_customer_view.html', context)

#Stationery
def inventory_stationery_view(request, type='ST'):
	list = Inventory.objects.values('id', 'code', 'description', 'imgFile', 'remark', 'dim_unit__code', 'price__inventory', 'price__unit_price', 'dim_category__code', 'dim_category__description').filter(dim_category__code=type)
	print(str(list))
	print('ok')
	# data2 = serializers.serialize('json', [sales_det])

	context = {'list': list, 'title':'Index1'}
	return render(request, 'retail/products.html', context)

#REVIEW
class ListReviewView(TemplateView):

	title = "Review List"
	
	template_name = 'retail/review_list.html'

	def Reviews(self):
		return Review.objects.all()
	
class CreateReviewView(CreateView):
	model = Review
	fields = ['id', 'description', 'inventory']
	template_name = 'retail/edit.html'

	success_url = 'review_list'
	title = "New Review"
	
	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreateReviewView, self).get_context_data(**kwargs)
		context['action'] = reverse('review_new')
	
		return context
		
class UpdateReviewView(UpdateView):
	model = Review
	title = "Edit Review"
	fields = ['id', 'description', 'inventory']
	template_name = 'retail/edit.html'
	
	success_url = 'review_list'
	title = "Edit Review"

		
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateReviewView, self).get_context_data(**kwargs)
		context['action'] = reverse('review_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteReviewView(DeleteView):

	model = Review
	fields = ['id', 'description', 'inventory']
	template_name = 'retail/review_delete.html'
	success_url = 'review_list'
	title = "Delete Review"

	def get_success_url(self):
		return reverse(self.success_url)
		
#PRICE
class ListPriceView(TemplateView):

	title = "Price List"
	
	template_name = 'retail/price_list.html'

	def Prices(self):
		return Price.objects.all()
	
class CreatePriceView(CreateView):
	model = Price
	fields = ['id', 'code','unit_price', 'eff_datetime', 'exp_datetime', 'inventory']
	template_name = 'retail/edit.html'
	
	def get_success_url(self):
		return reverse('price_list')
		
	def get_context_data(self, **kwargs):
		context = super(CreatePriceView, self).get_context_data(**kwargs)
		context['action'] = reverse('price_new')
	
		return context
		
class UpdatePriceView(UpdateView):
	model = Price
	title = "Edit Price"
	fields = ['id', 'code','unit_price', 'eff_datetime', 'exp_datetime', 'inventory']
	template_name = 'retail/edit.html'
	
	success_url = 'price_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdatePriceView, self).get_context_data(**kwargs)
		context['action'] = reverse('price_edit', kwargs={'pk': self.get_object().id})

		return context

class DeletePriceView(DeleteView):

	model = Price
	fields = ['id', 'code','unit_price', 'eff_date', 'exp_date', 'inventory']
	template_name = 'retail/price_delete.html'
	success_url = 'price_list'

	def get_success_url(self):
		return reverse(self.success_url)

#WebTemplate
def post_list(request):
	list = WebTemplate.objects.all()
	context = {'list': list, 'title':'Post'}
	return render(request, 'retail/webtemplate_list.html', context)
	
def post_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			webtemplate = WebTemplate.objects.get(pk=pk)

		else:
			webtemplate = WebTemplate()

		form = WebTemplateForm(request.POST, instance = webtemplate)
		
		if form.is_valid():
			webtemplate = form.save(commit=False)
			webtemplate.updated_datetime=timezone.now()
			webtemplate.save()
			
			return redirect('post_edit', webtemplate.pk)
		else:
			return HttpResponse('Save Error')
	
	else:


		if pk is not None:
			webtemplate = WebTemplate.objects.get(pk = pk)
			
			title="Edit Post"
			
		else:
			webtemplate = WebTemplate()
			#sales.id=201
			title="New Post"

	# if pk is not None:
		# purchase_det_list = Purchase_Det.objects.filter(purchase_id=pk)
	# else:
		# purchase_det_list = Purchase_Det.objects.none()
		
	form = WebTemplateForm(instance = webtemplate)
	request.session['webtemplate']=webtemplate.id
	
	context = {'form': form, 'title':title, 'back_url':'webtemplate_list', 'webtemplate_det_list': purchase_det_list, 'purchase_id': purchase.id} 
	return render(request, 'retail/purchase_edit.html', context)

def post_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	purchase = Purchase.objects.get(pk = pk)

	if request.method == 'POST':
		purchase.delete()
	else:

		context = {'purchase': purchase, 'title':'Delete purchase', 'back_url':'purchase_list'} 
	
		return render(request, 'retail/purchase_delete.html', context)
		
				
	return redirect('purchase_list')

#PURCHASES
def purchase_list(request):

	list = Purchase.objects.all()
	context = {'list': list, 'title':'Purchase List', 'object_name':'Purchase'}
	return render(request, 'retail/purchase_list.html', context)
	
def purchase_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			purchase = Purchase.objects.get(pk=pk)

		else:
			purchase = Purchase()

		form = PurchaseForm(request.POST, instance = purchase)
		
		if form.is_valid():
			purchase = form.save(commit=False)
			purchase.updated_datetime=timezone.now()
			purchase.save()
			
			return redirect('purchase_edit', purchase.pk)
		else:
			return HttpResponse('Save Error')
	
	else:


		if pk is not None:
			purchase = Purchase.objects.get(pk = pk)
			
			title="Edit Purchase"
			
		else:
			purchase = Purchase()
			#sales.id=201
			title="New Purchase"

	if pk is not None:
		purchase_det_list = Purchase_Det.objects.filter(purchase_id=pk)
	else:
		purchase_det_list = Purchase_Det.objects.none()
		
	form = PurchaseForm(instance = purchase)
	request.session['purchase']=purchase.id
	
	context = {'form': form, 'title':title, 'back_url':'purchase_list', 'purchase_det_list': purchase_det_list, 'purchase_id': purchase.id} 
	return render(request, 'retail/purchase_edit.html', context)

def purchase_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	purchase = Purchase.objects.get(pk = pk)

	if request.method == 'POST':
		purchase.delete()
	else:

		context = {'purchase': purchase, 'title':'Delete purchase', 'back_url':'purchase_list'} 
	
		return render(request, 'retail/purchase_delete.html', context)
		
				
	return redirect('purchase_list')

#PURCHASE_DET
def purchase_det_list(request):
	list = Purchase_Det.objects.all()
	context = {'list': list, 'title':'Purchase Detail List', 'object_name':'Purchase_Det'}
	return render(request, 'retail/purchase_det_list.html', context)

def purchase_det_new(request):
	
	if request.method == 'POST':

		purchase_det = Purchase_Det()

		form = Purchase_DetForm(request.POST, instance = purchase_det)
		
		
		if form.is_valid():
			purchase_det = form.save(commit=False)
			purchase_det.updated_datetime=timezone.now()
			purchase_det.save()
			return redirect('purchase_edit', purchase_det.purchase_id)
		else:
			return HttpResponse('Save Error')
	
	else:


		purchase_det = Purchase_Det()
		purchase_det.purchase_id=request.session['purchase']
		#sales_det.sales_id=sales_uid
		
		pk=request.session['purchase']
		title="New Purchase Detail"

	form = Purchase_DetForm(instance = purchase_det)
			
	context = {'form': form, 'title':title, 'back_url':'purchase_det_list', 'pk':pk} 
	
	return render(request, 'retail/purchase_det_new.html', context)

def purchase_det_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			purchase_det = Purchase_Det.objects.get(pk=pk)

		else:
			purchase_det = Purchase_Det()

		form = Purchase_DetForm(request.POST, instance = purchase_det)
		
		if form.is_valid():
			purchase_det = form.save(commit=False)
			purchase_det.updated_datetime=timezone.now()
			purchase_det.save()
			
			return redirect('purchase_edit', purchase_det.purchase_id)
		else:
			return HttpResponse('Save Error')
	
	else:


		if pk is not None:
			purchase_det = Purchase_Det.objects.get(pk=pk)
			title="Edit Purchase Detail"
			
		else:
			purchase_det = Purchase_Det()
			title="New Purchase Detail"

	form = Purchase_DetForm(instance = purchase_det)
			
	pk=request.session['purchase']
	context = {'form': form, 'title':title, 'back_url':'purchase_det_list', 'purchase_det_list': purchase_det_list, 'pk':pk} 
	
	return render(request, 'retail/purchase_det_edit.html', context)

def purchase_det_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
		
	purchase_det = Purchase_Det.objects.get(pk=pk)
	pk=request.session['purchase']

	if request.method == 'POST':
		purchase_det.delete()
		
		return redirect('purchase_edit', pk)

	else:

		context = {'purchase_det': purchase_det, 'title':'Delete Purchase Detail', 'back_url':purchase_list, 'pk':pk} 
		return render(request, 'retail/purchase_det_delete.html', context)
		
				
	return redirect('purchase_list')

#SALES
def sales_list(request):

	list = Sales.objects.all()
	context = {'list': list, 'title':'Sales List', 'object_name':'Sales'}
	return render(request, 'retail/sales_list.html', context)
	
def sales_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			sales = Sales.objects.get(pk=pk)

		else:
			
			sales = Sales()

		form = SalesForm(request.POST, instance = sales)
		
		if form.is_valid():
			sales = form.save(commit=False)
			sales.updated_datetime=timezone.now()
			sales.save()
			
			return redirect('sales_edit', sales.pk)
		else:
			return HttpResponse('Save Error')
	
	else:


		if pk is not None:
			sales = Sales.objects.get(pk = pk)
			
			title="Edit Sales"
			
		else:
			print("session sales")
			sales = Sales()
			#sales.id=201
			title="New Sales"

	if pk is not None:
		sales_det_list = Sales_Det.objects.filter(sales_id=pk)
	else:
		sales_det_list = Sales_Det.objects.none()
		
	form = SalesForm(instance = sales)
	#request.session['sales']=sales.id
	
	context = {'form': form, 'title':title, 'back_url':'sales_list', 'sales_det_list': sales_det_list, 'sales_id': sales.id} 
	return render(request, 'retail/sales_edit.html', context)

def sales_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
	
	sales = Sales.objects.get(pk = pk)

	if request.method == 'POST':
		sales.delete()
	else:

		context = {'sales': sales, 'title':'Delete sales', 'back_url':'sales_list'} 
	
		return render(request, 'retail/sales_delete.html', context)
		
				
	return redirect('purchase_list')

#SALES_DET
def sales_det_list(request):
	list = Sales_Det.objects.all()
	context = {'list': list, 'title':'Sales Detail List', 'object_name':'Sales_Det'}
	return render(request, 'retail/sales_det_list.html', context)

def sales_det_new(request):
	
	if request.method == 'POST':

		sales_det = Sales_Det()

		form = Sales_DetForm(request.POST, instance = sales_det)
		
		
		if form.is_valid():
			sales_det = form.save(commit=False)
			sales_det.updated_datetime=timezone.now()
			sales_det.save()
			return redirect('purchase_edit', sales_det.sales_id)
		else:
			return HttpResponse('Save Error')
	
	else:


		sales_det = Sales_det()
		#sales_det.purchase_id=request.session['sales']
		#sales_det.sales_id=sales_uid
		
		pk=request.session['sales']
		title="New Sales Detail"

	form = Purchase_DetForm(instance = sales_det)
			
	context = {'form': form, 'title':title, 'back_url':'sales_det_list', 'pk':pk} 
	
	return render(request, 'retail/sales_det_new.html', context)

def sales_det_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			sales_det = Sales_Det.objects.get(pk=pk)

		else:
			sales_det = Sales_Det()

		form = Sales_DetForm(request.POST, instance = sales_det)
		
		if form.is_valid():
			sales_det = form.save(commit=False)
			sales_det.updated_datetime=timezone.now()
			sales_det.save()
			
			return redirect('sales_edit', sales_det.sales_id)
		else:
			return HttpResponse('Save Error')
	
	else:


		if pk is not None:
			sales_det = Sales_Det.objects.get(pk=pk)
			title="Edit Purchase Detail"
			
		else:
			sales_det = Sales_Det()
			title="New Purchase Detail"

	form = Sales_DetForm(instance = sales_det)
			
	#pk=request.session['purchase']
	context = {'form': form, 'title':title, 'back_url':'sales_det_list', 'sales_det_list': sales_det_list, 'pk':pk} 
	
	return render(request, 'retail/sales_det_edit.html', context)

def sales_det_delete(request, pk=None):

	if pk is None:
		return HttpResponse('Save Error')
	
		
	sales_det = Sales_Det.objects.get(pk=pk)
	#pk=request.session['purchase']

	if request.method == 'POST':
		sales_det.delete()
		
		return redirect('sales_edit', pk)

	else:

		context = {'sales_det': sales_det, 'title':'Delete Sales Detail', 'back_url':sales_list, 'pk':pk} 
		return render(request, 'retail/sales_det_delete.html', context)
		
				
	return redirect('sales_list')

def sales_web_view(request):
	
	sales=request.session.get('sales')
	sales_det_lst=request.session.get('salesItemList')
	inventoryList = []
	if sales_det_lst is not None:
		
	
		for salesdtl in sales_det_lst:
		
			print("Type: " + str(type(salesdtl)) + " id:" + salesdtl.inventory_id)
			inventory=Inventory.objects.get(pk=salesdtl.inventory_id)
			
			inventoryList.extend([inventory])
		
	
	user=User.objects.get(pk=request.user.id)
	
	context = {'sales': sales, 'sales_det_lst':sales_det_lst, 'inventoryList':inventoryList, 'title':'Edit Sales'} 
	
	return render(request, 'retail/sales_web_view.html', context)

#Price
def price_list(request):
	list = Price.objects.all()
	context = {'list': list, 'title':'Price List', 'object_name':'Price'}
	#return Response(gst.code for gst in list)
	return render(request, 'retail/price_list.html', context)

def price_edit(request, pk=None):

	if request.method == 'POST':

		if pk is not None:
			price=Price.objects.get(pk=pk)

		else:
			price=Price()

		form = PriceForm(request.POST, instance=price)
		
		if form.is_valid():
			price=form.save(commit=False)
			price.updated_datetime=timezone.now()
			price.save()
			
			return redirect('price_list')
		else:
			return HttpResponse('Save Error')
	
	else:
		

		if pk is not None:
			price=Price.objects.get(pk=pk)
			title = 'New Price'
		else:
			price=Price()
			title = 'Edit Price'

	form = PriceForm(instance=price)
			
		
	context = {'form': form, 'title':title, 'back_url':'price_list'} 
	
	return render(request, 'retail/price_edit.html', context)

def price_delete(request, pk=None):

	if pk is None:

		return HttpResponse('Save Error')
	
	price=Price.objects.get(pk=pk)

	if request.method == 'POST':
	
		price.delete()
	
	else:

		context = {'price': price, 'title':'Delete Price', 'back_url':'price_list'} 
	
		return render(request, 'retail/price_delete.html', context)
		
				
	return redirect('price_list')

@csrf_exempt
def price_get(request, cust_id=None, inv_id=None):

	print(1)
	price_list = Price.objects.none()
	data=None;
	
	if request.is_ajax() and request.method == 'POST':

		print(2)
		# if cust_id is not None and inv_id is not None:
		price_list = Price.objects.filter(customer_id=cust_id, inventory_id=inv_id)
		
		print(str(3) + ': ' + str(len(price_list)))
	
		# if len(price_list)==0:
			
			# print(4)
			# price_list = Price.objects.filter(customer_id=None, inventory_id=inv_id)
			
	
	if len(price_list)==0:
		
		print('not found: ')
		price=Price()
	else:
		price=price_list[0]
		print('found: ' + str(price.unit_price))
		
	# if request.is_ajax:
		# data = serializers.serialize('json', [price])
	# else:
		# data = price
	
	data=price.unit_price
	print('price:' + str(data))
	return data

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	print(request.get_full_path())
	
	if reverse('logout') == request.get_full_path():
		print('reached out')

		auth_logout(request)
		return redirect('home')
	
	if reverse('loggedIn')==request.get_full_path():
		print('reach in')
		user = authenticate(username = username, password = password)      
		#print('auth:' + user)
		
		if user is None:
			print('not reached')
			return HttpResponse('Login failed')
			
		else:
			clearSession(request)
			auth_login(request, user)
			print('reached')
			
		return redirect('home')
	else:
		return HttpResponse('Login failed')

def clearSession(request):

	for key in list(request.session.keys()):
		del request.session[key]

def user_profile(request):
	
		
	if request.user.is_authenticated():
		#user=User.objects.get(pk=request.user.id)
		print('Det2: '+ str(user.date_joined))
	else:
		user=User()
		user.date_joined=datetime.date.today()

	if request.method == 'POST':
		print('auth and post')

		form = UserProfileForm(request.POST, instance=user)
		print('auth and post and insert user')

		if form.is_valid():
			print('form valid')
			
			#user=form.save(commit=False)
			
			#if user.pk is None:
			#	create_user(user.username, user.email, user.password)
			print('before:'+user.password)
			user.set_password(user.password)
			print('after:'+user.password)
			user.save()
			print('user saved')

			return redirect('home')
		else:
			return HttpResponse('Save Error')

	else:
		
		print(user.username)
		form = UserProfileForm(instance=user)
		print('form:' )
		context = {'form': form} 
	


	form = UserProfileForm(instance=user)
	context = {'form': form} 

	return render(request, 'retail/register.html', context)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			send_mail(
    'Subject here',
    'Here is the message.',
    'jetl530@msn.com',
    ['jetl530@msn.com'],
    fail_silently=False,
)
			return redirect('home')

	else:
		form = RegistrationForm()
	context = {}
	context.update(request)
	context['form'] = form

	return render(request, 'retail/register.html', context)

class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
    'Subject here',
    'Here is the message.',
    to=['jetl530@msn.com'],
    fail_silently=False,
)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

@csrf_exempt
def doSales(request, inv_id=None, qty=0):
	print('started1')
	sales=request.session.get('sales')
	salesItemList=request.session.get('salesItemList')
	
	if request.is_ajax() and request.method == 'POST':


		
		if sales is None:
		
			sales = Sales()
			user=User.objects.get(pk=request.user.id)
			sales.description = 'Sales by ' + user.last_name
			sales.customer_id = user.pk
			

	else:
		return HttpResponse('invalid request')


	foundItem = False;
		
	if salesItemList is not None:
		print('salesItemList is not None')
		for sales_det in salesItemList:
			print(str(sales_det.inventory_id) + '==>' + str(inv_id))

			if sales_det.inventory_id == str(inv_id):
				foundItem=True
				sales_det.qty  = int(qty)
				
	else:
		print('salesItemList is None')

	
	if not foundItem:
		sales_det = Sales_Det()
		sales_det.inventory_id = inv_id
		sales_det.qty=int(qty)
		print('data:' + str(inv_id))

		if salesItemList is None:
			salesItemList=[]
		
		salesItemList.extend([sales_det])
	
		
		
	# data2 = serializers.serialize('json', [sales_det])
	sales_det.seq=len(salesItemList)+1
	
	for sales_det in salesItemList:
		sales_det.unit_price=price_get(request, 2, inv_id)
		print('unit price: ' + str(sales_det.unit_price) + ' type: ' + str(type(sales_det.unit_price)))
		print('qty: ' + str( sales_det.qty) + ' type: ' + str(type(sales_det.qty)))
		
		sales_det.det_amt=Decimal(sales_det.unit_price * sales_det.qty).quantize(Decimal('0.01'), rounding=ROUND_UP)
		#getcontext().prec=2
		#gstamt=Decimal(0.061).quantize(Decimal('0.01'), rounding=ROUND_UP)
		gstamt=round(float(sales_det.det_amt) * 0.06,2)
		print('gst amt: ' + str(gstamt))
		sales_det.gst_amt = gstamt #round(sales_det.det_amt * gstamt) #Decimal(gstamt).quantize(Decimal('0.01'), rounding=ROUND_UP))
		
		sales_det.net_amt=float(sales_det.det_amt) + float(sales_det.gst_amt)
		
	# print(str(salesItemList))
	# salesItemList.append(data2)
	
	
	# data = serializers.serialize('json',[sales])
	# dataList = serializers.serialize('json',[salesItemList])
	sales.doc_amt=round((sum(c.det_amt for c in salesItemList)),2)
	sales.doc_gst_amt=round((sum(c.gst_amt for c in salesItemList)),2)
	sales.doc_net_amt=round((sum(c.net_amt for c in salesItemList)),2)
	
	request.session['sales']=sales 
	request.session['salesItemList']=salesItemList
	
	
	

	# customer = User.objects.get(pk=sales.customer_id)
	# print('customer:' + customer.username)
	data=list([sales]) + list(salesItemList)
	print('data:\n\n' + serializers.serialize('json',data) + '\n\n')
	return HttpResponse(serializers.serialize('json',data))

@csrf_exempt
def removeSalesItem(request, inv_id=None):
	print('removeSalesItem')
	sales=request.session.get('sales')
	salesItemList=request.session.get('salesItemList')
	
	if request.is_ajax() and request.method == 'POST':
		print('started1')
			

	else:
		return HttpResponse('invalid request')


	foundItem = False;
	getItem=None
	
	if salesItemList is not None:
		print('salesItemList is not None')
		for sales_det in salesItemList:
			print(str(sales_det.inventory_id) + '==>' + str(inv_id))

			if sales_det.inventory_id == str(inv_id):
				foundItem=True
				getItem=sales_det
				
	else:
		print('salesItemList is None')

	
	if foundItem:
		
		salesItemList.remove(getItem)
	

	sales.doc_amt=round((sum(c.det_amt for c in salesItemList)),2)
	sales.doc_gst_amt=round((sum(c.gst_amt for c in salesItemList)),2)
	sales.doc_net_amt=round((sum(c.net_amt for c in salesItemList)),2)
	
	request.session['sales']=sales 
	request.session['salesItemList']=salesItemList
	
	
	

	# customer = User.objects.get(pk=sales.customer_id)
	# print('customer:' + customer.username)
	data=list([sales]) + list(salesItemList)
	print('data:\n\n' + serializers.serialize('json',data) + '\n\n')
	return HttpResponse(serializers.serialize('json',data))

@csrf_exempt
def cancelSales(request):
	print('cancelSales')
	
	sales=request.session['sales']
	
	if request.session.get('salesItemList', None) is not None:
		del request.session['salesItemList']

			
	sales.doc_amt=0
	sales.doc_gst_amt=0
	sales.doc_net_amt=0
	cartAmt=sales.doc_net_amt

	data=[sales]
	print('data:\n\n' + serializers.serialize('json',data) + '\n\n')
	return HttpResponse(serializers.serialize('json',data))

@csrf_exempt
def doSales2(request, inv_id=None, qty=0):

	if request.session.get('sales', None) is not None:
		del request.session['sales']
	
	if request.session.get('salesItemList', None) is not None:
		del request.session['salesItemList']
		
	#print('sales: ' + str(sales))	
	print('salesItemList: ' + str(salesItemList)	)
	
	data=None;
	dataList = {}
	salesItemList=[]
	
	if request.is_ajax() and request.method == 'POST':

		
		#sales_edit(request, None, inv_id, qty)
		
		# sales = request.session['sales']

		# data = serializers.serialize('json', sales)

		
		if sales is None:
		
			sales = Sales()
			user=User.objects.get(pk=request.user.id)
			sales.description = 'Sales by ' + user.last_name
			sales.customer_id = user.pk
			
			foundItem = False;
				
			if salesItemList is not None:
				for sales_det in [salesItemList]:
					print(sales_det)
					if sales_det.inventory_id == inv_id:
						foundItem=True
						sales_det.qty  = qty
			
			if not foundItem:
				sales_det = Sales_Det()
				sales_det.inventory_id = inv_id
				print('data:' + str(inv_id))

				if salesItemList is None:
					salesItemList=[]

				
			data2 = serializers.serialize('json', [sales_det])
			salesItemList2.extend([sales_delete])
			salesItemList.append(data2)
			
			
			data = serializers.serialize('json',[sales])
			dataList = salesItemList #serializers.serialize('json',[salesItemList])
			
			#request.session['sales']=sales 
			#request.session['salesItemList']=salesItemList2 

			#print('data:' + data)
			
			#print('data list: ' + str(dataList))


	else:
		return HttpResponse('invalid request')

	
	return HttpResponse(data)

@csrf_exempt
def checkout(request):

	sales=request.session.get('sales')
	salesItemList=request.session.get('salesItemList')
	
	if request.is_ajax() and request.method == 'POST':


		
		if sales is None:
		
			return HttpResponse('invalid request')
			
		else:
		
			sales.save()
			sales.si_no = 'IV'+ datetime.date.today().strftime("%y%m") + format(sales.id, '04d')
			sales.save()
			
			for sales_det in salesItemList:
				sales_det.sales_id=sales.id
				sales_det.save()
				
			del request.session['salesItemList']
			del request.session['sales']
			request.session.modified=True



	else:
		return HttpResponse('invalid request')

	data=[sales]
	
	print('data:\n\n' + serializers.serialize('json',data) + '\n\n')
	return HttpResponse(serializers.serialize('json',data))


