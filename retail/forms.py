from django import forms
from django.forms.utils import ErrorList
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DIM_Category, DIM_GST, DIM_Contact_Type, Contact_Info, Customer, Supplier, Inventory, DIM_Unit, Tax, DIM_Contact_Type, DIM_Promotion, Sales, Purchase, Sales_Det, Purchase_Det, DocNo, State, Price, WebTemplate, DIM_SubCategory

class DivErrorList(ErrorList):
	def __str__(self):
		return self.as_divs()
		
	def as_divs(self):
		if not self: return ''
		
		return ''
	
class LoginForm(AuthenticationForm):
	
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class TestTableModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         # return the field you want to display
         return obj.display_field
		 
class DIM_GSTForm(forms.ModelForm):
	class Meta:
		model=DIM_GST
		fields='__all__'
		
class DIM_CategoryForm(forms.ModelForm):
	class Meta:
		model=DIM_Category
		fields='__all__'

class DIM_SubCategoryForm(forms.ModelForm):
	class Meta:
		model=DIM_SubCategory
		fields='__all__'
		
class PriceForm(forms.ModelForm):
	class Meta:
		model=Price
		
		    
		fields='__all__'
		
		widgets = {
			'eff_datetime': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder':'Select a date'}, ),
			'exp_datetime': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder':'Select a date'}, ),
        }

class DocNoForm(forms.ModelForm):
	class Meta:
		model=DocNo
		fields='__all__'

class StateForm(forms.ModelForm):
	class Meta:
		model=State
		fields='__all__'
		
class Contact_TypeForm(forms.ModelForm):
	class Meta:
		model=DIM_Contact_Type
		fields='__all__'
		
class Contact_InfoForm(forms.ModelForm):
	class Meta:
		model=Contact_Info
		fields='__all__'
		
		
class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields='__all__'
		
class SupplierForm(forms.ModelForm):
	class Meta:
		model=Supplier
		fields='__all__'
		
class InventoryForm(forms.ModelForm):
	class Meta:
		model=Inventory
		fields='__all__'
		
class DIM_UnitForm(forms.ModelForm):
	class Meta:
		model=DIM_Unit
		fields='__all__'
		
class TaxForm(forms.ModelForm):
	class Meta:
		model=Tax
		fields='__all__'

class DIM_PromotionForm(forms.ModelForm):
	class Meta:
		model=DIM_Promotion
		fields='__all__'

class SalesForm(forms.ModelForm):

	class Meta:
		model=Sales



		fields = '__all__' # ('field1', 'field2')
		
		labels={
			'si_no': _('Invoice No.'),
			'description': _('Description'),
			'sales_date': _('Date'),
		}
		
		'''
		help_texts={
			'description': _('Testing'),
		}
		'''
		
		
		widgets = {
			'sales_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder':'Select a date'}, ),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'placeholder':'Describe this sales'}),
			#'doc_amt': forms.TextInput(attrs={'readonly':'readonly'}),
			#'doc_promotion_amt': forms.TextInput(attrs={'readonly':'readonly'}),
			'doc_amt': forms.TextInput(),
			'doc_promotion_amt': forms.TextInput(),
			'si_no': forms.TextInput(attrs={'placeholder':'New Invoice No'}),
			#'customer': forms.Select(attrs={'placeholder':'Select customer', "onChange":'this.form.submit();'}),
        }
		'''
		error_messages={
			'description': {
				'required' : 'Mandatory field',
			},
		}
		si_no = forms.CharField(widget=forms.TextInput(
			attrs={'readonly':'readonly',
				}), label=u'Invoice No')

		'''
		'''
		customer = forms.ModelChoiceField(queryset=cust_list, empty_label="(Nothing)")

	def __init__(self, *args, **kwargs):
		print('testt')
		super(SalesForm, self).__init__(*args, **kwargs)
		
		self.fields['customer'].empty_label='-- Select customer --'
		self.fields['description'].error_messages={'required': 'Mandatory'}
		'''
		

class Sales_DetForm(forms.ModelForm):
	class Meta:
		model=Sales_Det
		fields='__all__'
		
		widgets = {
			'inventory': forms.Select(attrs={'placeholder':'Select customer', "onChange":'test();'}),
			'qty': forms.TextInput(attrs={"onChange":'test();'}),
        }

class PurchaseForm(forms.ModelForm):
	class Meta:
		model=Purchase
		fields='__all__'

class Purchase_DetForm(forms.ModelForm):
	class Meta:
		model=Purchase_Det
		fields='__all__'

class UserForm(AuthenticationForm):
	class Meta:
		model = User
		fields = '__all__'

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = User  
		fields='__all__'
		
		widgets = {
			'username': forms.TextInput(),
			'password': forms.PasswordInput(),
			'date_joined': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder':'Select a date'}, ),
		}
		
		help_texts={
			'username': _(''),
			'password': _(''),
		}
		
		error_messages={
			'username': {
				'required' : '',
			},
			'password': {
				'required' : '',
			},
		}
		
	def save(self, commit=True):
		
		user = super(UserProfileForm, self).save(commit=False)
		print('before save in form: ' + user.password)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
			print('after save in form: ' + user.password)
			
		return user


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
    
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
        
		if commit:
			user.save()
            
		return user
		
class WebTemplateForm(forms.ModelForm):
	class Meta:
		model=WebTemplate
		fields='__all__'
