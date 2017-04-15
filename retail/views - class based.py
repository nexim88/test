from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import DIM_GST, DIM_Unit, DIM_Contact_Type, Contact_Info, Tax, Customer, Supplier, Inventory, Price, Review, Purchase, Purchase_Det, Sales,  Sales_Det, DIM_Promotion
from .forms import Contact_InfoForm

# Create your views here.

#index
class IndexView(TemplateView):
	title = "Homepage"
	
	template_name = 'retail/index.html'

#GST
class ListGSTView(TemplateView):
	title = "GST List"
	
	template_name = 'retail/gst_list.html'

	def GSTs(self):
		return DIM_GST.objects.all()
	
class CreateGSTView(CreateView):
	model = DIM_GST
	fields = ['id', 'code','description', 'percentage_claimable', 'percentage_chargeable']
	template_name = 'retail/edit.html'
	
	def get_success_url(self):
		return reverse('gst_list')
		
	def get_context_data(self, **kwargs):
		context = super(CreateGSTView, self).get_context_data(**kwargs)
		context['action'] = reverse('gst_new')
	
		return context
		
class UpdateGSTView(UpdateView):
	model = DIM_GST
	title = "Edit GST"
	fields = ['id', 'code','description', 'percentage_claimable', 'percentage_chargeable']
	template_name = 'retail/edit.html'
	
	success_url = 'gst_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateGSTView, self).get_context_data(**kwargs)
		context['action'] = reverse('gst_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteGSTView(DeleteView):

	model = DIM_GST
	fields = ['id', 'code','description', 'percentage_claimable', 'percentage_chargeable']
	template_name = 'retail/delete.html'
	success_url = 'gst_list'

	def get_success_url(self):
		return reverse(self.success_url)
	
#DIM_Unit
class ListUnitView(TemplateView):
	title = "Unit List"
	
	template_name = 'retail/unit_list.html'

	def Units(self):
		return DIM_Unit.objects.all()
	
class CreateUnitView(CreateView):
	model = DIM_Unit
	fields = ['id', 'code','description']
	template_name = 'retail/edit.html'
	
	def get_success_url(self):
		return reverse('unit_list')
		
	def get_context_data(self, **kwargs):
		context = super(CreateUnitView, self).get_context_data(**kwargs)
		context['action'] = reverse('unit_new')
	
		return context
		
class UpdateUnitView(UpdateView):
	model = DIM_Unit
	title = "Edit Unit"
	fields = ['id', 'code','description']
	template_name = 'retail/edit.html'
	
	success_url = 'unit_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateUnitView, self).get_context_data(**kwargs)
		context['action'] = reverse('unit_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteUnitView(DeleteView):

	model = DIM_Unit
	fields = ['id', 'code','description']
	template_name = 'retail/unit_delete.html'
	success_url = 'unit_list'

	def get_success_url(self):
		return reverse(self.success_url)

#TAX
class ListTaxView(TemplateView):
	title = "Tax List"
	
	template_name = 'retail/tax_list.html'

	def Taxs(self):
		return Tax.objects.all()
	
class CreateTaxView(CreateView):
	model = Tax
	fields = ['id', 'code', 'unit_price', 'eff_datetime', 'exp_datetime', 'inventory', 'gst']
	template_name = 'retail/edit.html'
	
	def get_success_url(self):
		return reverse('tax_list')
		
	def get_context_data(self, **kwargs):
		context = super(CreateTaxView, self).get_context_data(**kwargs)
		context['action'] = reverse('tax_new')
	
		return context
		
class UpdateTaxView(UpdateView):
	model = Tax
	title = "Edit Tax"
	fields = ['id', 'code', 'unit_price', 'eff_datetime', 'exp_datetime', 'inventory', 'gst']
	template_name = 'retail/edit.html'
	
	success_url = 'tax_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateTaxView, self).get_context_data(**kwargs)
		context['action'] = reverse('tax_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteTaxView(DeleteView):

	model = Tax
	fields = ['id', 'code', 'unit_price', 'eff_datetime', 'exp_datetime', 'inventory', 'gst']
	template_name = 'retail/tax_delete.html'
	success_url = 'tax_list'

	def get_success_url(self):
		return reverse(self.success_url)

#DIM_Contact_Type
class ListContactTypeView(TemplateView):

	title = "Contact Type List"
	
	template_name = 'retail/contact_type_list.html'

	def ContactTypes(self):
		print(DIM_Contact_Type.objects.all().query)

		test_filter = self.request.session.get('test')
		if test_filter:
			print("found")
			return DIM_Contact_Type.objects.filter(pk=test_filter)
			
		print("not found")
		return DIM_Contact_Type.objects.all()
			
		
	
class CreateContactTypeView(CreateView):
	model = DIM_Contact_Type
	
	fields = ['id', 'code','description']
	template_name = 'retail/edit.html'

	success_url = 'contact_type_list'
	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreateContactTypeView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact_type_new')
	
		return context
	
class UpdateContactTypeView(UpdateView):
	model = DIM_Contact_Type
	
	title = "Edit Contact Type"
	fields = ['id', 'code','description']
	
	template_name = 'retail/edit.html'
	
	success_url = 'contact_type_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateContactTypeView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact_type_edit', kwargs={'pk': self.get_object().id})

		return context
		

class DeleteContactTypeView(DeleteView):

	model = DIM_Contact_Type
	fields = ['id', 'code','description']
	template_name = 'retail/contact_type_delete.html'
	success_url = 'contact_type_list'

	def get_success_url(self):
		return reverse(self.success_url)

#DIM_Promotion
class ListPromotionView(TemplateView):
	title = "Promotion List"
	
	template_name = 'retail/promotion_list.html'

	def Promotions(self):
		return DIM_Promotion.objects.all()
	
class CreatePromotionView(CreateView):

	model = DIM_Promotion
	fields = ['id', 'code','description', 'promo_cond', 'promo_percent', 'promo_amt', 'inventory']
	template_name = 'retail/edit.html'

	success_url = 'promotion_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreatePromotionView, self).get_context_data(**kwargs)
		context['action'] = reverse('promotion_new')
	
		return context
		
class UpdatePromotionView(UpdateView):

	model = DIM_Promotion
	title = "Edit Promotion"
	fields = ['id', 'code','description', 'promo_cond', 'promo_percent', 'promo_amt', 'inventory']
	template_name = 'retail/edit.html'
	
	success_url = 'promotion_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdatePromotionView, self).get_context_data(**kwargs)
		context['action'] = reverse('promotion_edit', kwargs={'pk': self.get_object().id})

		return context

class DeletePromotionView(DeleteView):


	model = DIM_Promotion
	fields = ['id', 'code','description', 'promo_cond', 'promo_percent', 'promo_amt', 'inventory']
	template_name = 'retail/promotion_delete.html'
	success_url = 'promotion_list'

	def get_success_url(self):
		return reverse(self.success_url)

#Contact_Info
class ListContactInfoView(TemplateView):

	title = "Contact Info List"
	
	template_name = 'retail/contact_info_list.html'

	def ContactInfos(self):
		return Contact_Info.objects.all()
	
def contactinfo_new(request, contacttype_id):
	print('test')
	ct = DIM_Contact_Type.objects.get(pk=contacttype_id)
	usr=User.objects.get(username='fai')
	print(ct.description)
	form = Contact_InfoForm(initial={'contacttype':ct,'info':'-2-', 'user':usr})
	return render(request, 'retail/edit.html', {'form': form})
	
def contactinfo_view(request, pk):
	print('test22')
	ci = Contact_Info.objects.get(pk=pk)
	print('test33')
	print(ci.info)
	form = Contact_InfoForm(instance=ci)
	return render(request, 'retail/edit.html', {'form': form})

class CreateContactInfoView(CreateView):

	model = Contact_Info
	#fields = ['id', 'info', 'eff_date', 'exp_date', 'user', 'contacttype']
	template_name = 'retail/edit.html'
	success_url = 'contact_info_list'
	title = "New Contact Info"
	form_class = Contact_InfoForm
	
	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):

		print("create contact info" + ' test' + ': ' + self.kwargs['contacttype_id'])
		ct_id=self.kwargs['contacttype_id']
		ct = DIM_Contact_Type.objects.get(pk=self.kwargs['contacttype_id'])
		Contact_Info.contacttype=ct
		context = super(CreateContactInfoView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact_info_new')
	
		return context

		
		'''
    This view allows a user to edit details of a project.
def EditProject(request, project_id=None):
	title = u'Unirac - Edit Project'
    project = Project.objects.get(id=4)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # save form
            form.save()
        else:
            return render_to_response('edit_project.html', {
                'title': title,
                'form': form,
            }, RequestContext(request))
    else:
        form = ProjectForm(instance=project)
        return render_to_response('edit_project.html', {
            'title': title,
            'form': form,
        }, RequestContext(request))
		

	def get_context_data(self, **kwargs):
		print("create contact info" + ' test' + ': ' + self.kwargs['contacttype_id'])
		ct_id=self.kwargs['contacttype_id']
		ct = DIM_Contact_Type.objects.get(pk=self.kwargs['contacttype_id'])
		Contact_Info.contacttype=ct
		context = super(CreateContactInfoView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact_info_new')
	
		return context

'''
		
class UpdateContactInfoView(UpdateView):
	model = Contact_Info
	title = "Edit Contact Info"
	fields = ['id', 'info', 'eff_date', 'exp_date', 'user', 'contacttype']
	template_name = 'retail/edit.html'
	
	success_url = 'contact_info_list'
	title = "Edit Contact Info"

		
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateContactInfoView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact_info_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteContactInfoView(DeleteView):

	model = Contact_Info
	fields = ['id', 'info', 'eff_date', 'exp_date', 'user', 'contacttype']
	template_name = 'retail/contact_info_delete.html'
	success_url = 'contact_info_list'
	title = "Delete Contact Info"

	def get_success_url(self):
		return reverse(self.success_url)

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
		
#INVENTORY
class ListInventoryView(TemplateView):
	title = "Inventory List"
	
	template_name = 'retail/Inventory_list.html'

	def Inventorys(self):
		return Inventory.objects.all()
	
class CreateInventoryView(CreateView):
	model = Inventory
	fields = ['id', 'code','description', 'remark', 'dim_unit']
	template_name = 'retail/edit.html'
	
	def get_success_url(self):
		return reverse('inventory_list')
		
	def get_context_data(self, **kwargs):
		context = super(CreateInventoryView, self).get_context_data(**kwargs)
		context['action'] = reverse('inventory_new')
	
		return context
		
class UpdateInventoryView(UpdateView):
	model = Inventory
	title = "Edit Inventory"
	fields = ['id', 'code','description', 'remark', 'dim_unit']
	template_name = 'retail/edit.html'
	
	success_url = 'inventory_list'
	
	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateInventoryView, self).get_context_data(**kwargs)
		context['action'] = reverse('inventory_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteInventoryView(DeleteView):

	model = Inventory
	fields = ['id', 'code','description', 'remark', 'dim_unit']
	template_name = 'retail/inventory_delete.html'
	success_url = 'inventory_list'

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
			
#SUPPLIER
class ListSupplierView(TemplateView):

	title = "Supplier List"
	
	template_name = 'retail/supplier_list.html'

	def Suppliers(self):
		return Supplier.objects.all()
	
class CreateSupplierView(CreateView):
	model = Supplier
	fields = ['code','fullname', 'license_no', 'business_nature']
	template_name = 'retail/edit.html'
	success_url = 'supplier_list'

	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreateSupplierView, self).get_context_data(**kwargs)
		context['action'] = reverse('supplier_new')
	
		return context
		
class UpdateSupplierView(UpdateView):
	model = Supplier
	title = "Edit Supplier"
	fields = ['code','fullname', 'license_no', 'business_nature']
	template_name = 'retail/edit.html'
	success_url = 'supplier_list'

	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateSupplierView, self).get_context_data(**kwargs)
		context['action'] = reverse('supplier_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteSupplierView(DeleteView):

	model = Supplier
	fields = ['code','fullname', 'license_no', 'business_nature']
	template_name = 'retail/supplier_delete.html'
	success_url = 'supplier_list'

	def get_success_url(self):
		return reverse(self.success_url)

#PURCHASES
class ListPurchaseView(ListView):


	title = "Purchase List"
	model = Purchase
	
	template_name = 'retail/purchase_list.html'

	
class CreatePurchaseView(CreateView):

	model = Purchase
	fields = ['pi_no', 'supplier', 'description', 'purchase_date', 'doc_amt', 'doc_gst_amt', 'doc_promotion_amt', 'remark']
	template_name = 'retail/edit.html'
	success_url = 'purchase_list'

	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreatePurchaseView, self).get_context_data(**kwargs)
		context['action'] = reverse('purchase_new')
	
		return context
		
class UpdatePurchaseView(UpdateView):


	model = Purchase
	title = "Edit Purchase"
	fields = ['pi_no', 'supplier', 'description', 'purchase_date', 'doc_amt', 'doc_gst_amt', 'doc_promotion_amt', 'remark']
	template_name = 'retail/edit.html'
	success_url = 'purchase_list'

	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		print(kwargs)
		context = super(UpdatePurchaseView, self).get_context_data(**kwargs)
		context['action'] = reverse('purchase_edit', kwargs={'pk': self.get_object().id})

		return context

class DeletePurchaseView(DeleteView):

	model = Purchase
	fields = ['pi_no', 'supplier', 'description', 'purchase_date', 'doc_amt', 'doc_gst_amt', 'doc_promotion_amt', 'remark']
	template_name = 'retail/purchase_delete.html'
	success_url = 'purchase_list'

	def get_success_url(self):
		return reverse(self.success_url)
		
#PURCHASE_DET
class ListPurchaseDetView(TemplateView):

	title = "Purchase Detail List"
	
	template_name = 'retail/purchase_det_list.html'

	def PurchaseDets(self):
		return Purchase_Det.objects.all()
	
class CreatePurchaseDetView(CreateView):
	model = Purchase_Det
	fields = ['purchase', 'seq', 'qty', 'gst_amt', 'det_amt', 'inventory', 'promotion']
	template_name = 'retail/edit.html'
	success_url = 'purchase_det_list'

	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreatePurchaseDetView, self).get_context_data(**kwargs)
		context['action'] = reverse('purchase_det_new')
	
		return context
		
class UpdatePurchaseDetView(UpdateView):

	model = Purchase_Det
	title = "Edit Purchase Detail"
	fields = ['purchase', 'seq', 'qty', 'gst_amt', 'det_amt', 'inventory', 'promotion']
	template_name = 'retail/edit.html'
	success_url = 'purchase_det_list'

	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdatePurchaseDetView, self).get_context_data(**kwargs)
		context['action'] = reverse('purchase_det_edit', kwargs={'pk': self.get_object().id})

		return context

class DeletePurchaseDetView(DeleteView):

	model = Purchase_Det
	fields = ['purchase', 'seq', 'qty', 'gst_amt', 'det_amt', 'inventory', 'promotion']
	template_name = 'retail/purchase_det_delete.html'
	success_url = 'purchase_det_list'

	def get_success_url(self):
		return reverse(self.success_url)

#CUSTOMER
class ListCustomerView(TemplateView):
	title = "Customer List"
	
	template_name = 'retail/customer_list.html'

	def Customers(self):
		return Customer.objects.all()
	
class CreateCustomerView(CreateView):
	model = Customer
	fields = ['code','fullname', 'license_no', 'business_nature']
	template_name = 'retail/edit.html'
	success_url = 'customer_list'

	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		context = super(CreateCustomerView, self).get_context_data(**kwargs)
		context['action'] = reverse('customer_new')
	
		return context
		
class UpdateCustomerView(UpdateView):
	model = Customer
	title = "Edit Customer"
	fields = ['code','fullname', 'license_no', 'business_nature']
	template_name = 'retail/edit.html'
	success_url = 'customer_list'

	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		context = super(UpdateCustomerView, self).get_context_data(**kwargs)
		context['action'] = reverse('customer_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteCustomerView(DeleteView):

	model = Customer
	fields = ['code','fullname', 'license_no', 'business_nature']
	template_name = 'retail/customer_delete.html'
	success_url = 'customer_list'

	def get_success_url(self):
		return reverse(self.success_url)

#SALES
class ListSalesView(ListView):


	title = "Sales List"
	model = Sales
	template_name = 'retail/sales_list.html'

	def SalesDets(self, id):
		print('here1')
		return Sales_Det.objects.filter(sales=id)
	'''
	def Sales(self):
		print('here sales')
		return Sales.objects.all()
		
	'''
	
class CreateSalesView(CreateView):


	model = Sales
	title = "New Sales"
	#success_url = 'sales_list'
	fields = ['si_no', 'customer', 'description', 'sales_date', 'doc_amt', 'doc_gst_amt', 'doc_promotion_amt', 'remark']
	#template_name = 'retail/sales_edit.html'

'''

	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		print('ok')
		context = super(CreateSalesView, self).get_context_data(**kwargs)
		print('ok')
		print(Sales_Det.objects.count())
		context['salesdetlst'] = Sales_Det.objects.all()
		context['action'] = reverse('sales_new')
	
		return context
'''		
'''
	def SalesDets(self):
		print('test')
		return Sales_Det.objects.all()
'''

class UpdateSalesView(UpdateView):
	model = Sales
	title = "Edit Sales"
	fields = ['si_no', 'customer', 'description', 'sales_date', 'doc_amt', 'doc_gst_amt', 'doc_promotion_amt', 'remark']
	#template_name = 'retail/sales_edit.html'
	#success_url = 'sales_list'

	#def get_success_url(self):
	#	return reverse(self.success_url)
	'''
	def get_context_data(self, **kwargs):
		print(self.get_object().id)
		print('ok')
		#print(Sales_det.count())
		context = super(UpdateSalesView, self).get_context_data(**kwargs)
		#context['salesdetlst'] = Sales_Det.objects.all()
		#context['salesdetlst'] = self.get_object.description
		context['action'] = reverse('sales_edit', kwargs={'pk': self.get_object().id})

		return context

	def SalesDets(self):
		print('test')
		return Sales_Det.objects.filter(sales=self.get_object().id)
	'''

class DeleteSalesView(DeleteView):


	model = Sales
	fields = ['si_no', 'customer', 'description', 'sales_date', 'doc_amt', 'doc_gst_amt', 'doc_promotion_amt', 'remark']
	template_name = 'retail/sales_delete.html'
	success_url = 'sales_list'

	def get_success_url(self):
		return reverse(self.success_url)

#SALES_DET
class ListSalesDetView(DetailView):

	title = "Sales Detail List"
	model = Sales
	template_name = 'retail/sales_det_list.html'

'''
	def SalesDets(self):
		print('test')
		return Sales_Det.objects.all()
	
	def GSTDets(self):
		return DIM_GST.objects.all()
		
	def InvDets(self):
		return Inventory.objects.all()
'''

class CreateSalesDetView(CreateView):

	model = Sales_Det
	fields = ['sales', 'seq', 'qty', 'gst_amt', 'det_amt', 'inventory', 'promotion']
	template_name = 'retail/sales_det_edit.html'
	success_url = 'sales_det_list'

	def get_success_url(self):
		return reverse(self.success_url)
		
	def get_context_data(self, **kwargs):
		print(	)
		
		for kwarg in kwargs:
			print(kwarg)
		
		context = super(CreateSalesDetView, self).get_context_data(**kwargs)
		context['action'] = reverse('sales_det_new')
	
		return context
		
class UpdateSalesDetView(UpdateView):

	model = Sales_Det
	title = "Edit Sales Detail"
	fields = ['sales', 'seq', 'qty', 'gst_amt', 'det_amt', 'inventory', 'promotion']
	template_name = 'retail/sales_det_edit.html'
	success_url = 'sales_det_list'

	def get_success_url(self):
		return reverse(self.success_url)
	
	def get_context_data(self, **kwargs):
		print("updateview")
		context = super(UpdateSalesDetView, self).get_context_data(**kwargs)
		context['action'] = reverse('sales_det_edit', kwargs={'pk': self.get_object().id})

		return context

class DeleteSalesDetView(DeleteView):

	model = Sales_Det
	fields = ['sales', 'seq', 'qty', 'gst_amt', 'det_amt', 'inventory', 'promotion']
	template_name = 'retail/sales_det_delete.html'
	success_url = 'sales_det_list'

	def get_success_url(self):
		return reverse(self.success_url)
		