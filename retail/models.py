from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class DocNo(models.Model):

	code = models.CharField(max_length = 20)
	currNo = models.IntegerField(default=0)
	format=models.CharField(max_length=20)
	description=models.CharField(max_length = 200)
	doctype=models.CharField(max_length = 200)

	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.code

class State(models.Model):

	code = models.CharField(max_length = 3)
	description=models.CharField(max_length = 200)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class DIM_Role(models.Model):

	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class DIM_Access(models.Model):
	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)
	link=models.CharField(max_length = 200)
		
	# Foreign Key
	role= models.ForeignKey(DIM_Role, null=True, blank = True)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class DIM_Contact_Type(models.Model):
	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 20)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

#def get_absolute_url(self):
	#	return reverse('contact_type_edit', kwargs={'slug':self.slug})
		
class Contact_Info(models.Model):
	
	info=models.CharField(max_length=200)
	eff_date = models.DateTimeField(null = True, blank = True)
	exp_date = models.DateTimeField(null = True, blank = True)
	
	# Foreign Key
	user = models.ForeignKey(User)
	contacttype= models.ForeignKey(DIM_Contact_Type, null=True, blank = True)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)
		
	def __str__(self):
		return self.info
		
class DIM_Unit(models.Model):
	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class DIM_GST(models.Model):
	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)
	percentage_claimable = models.DecimalField(max_digits=3, decimal_places=2)
	percentage_chargeable = models.DecimalField(max_digits=3, decimal_places=2)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class DIM_Category(models.Model):
	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class DIM_SubCategory(models.Model):
	code = models.CharField(max_length = 20)
	description=models.CharField(max_length = 200)
	
	# Foreign Key
	category = models.ForeignKey(DIM_Category, null=True, blank = True)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class Customer(models.Model):

	code = models.CharField(max_length = 20)
	fullname = models.CharField(max_length = 50)
	license_no= models.CharField(max_length = 20)
	business_nature= models.CharField(max_length = 20)
	
	bill_address1=models.CharField(max_length=30)
	bill_address2=models.CharField(max_length=30)
	bill_address3=models.CharField(max_length=30)
	bill_postcode=models.CharField(max_length=5)
	bill_city=models.CharField(max_length=30)

	ship_address1=models.CharField(max_length=30)
	ship_address2=models.CharField(max_length=30)
	ship_address3=models.CharField(max_length=30)
	ship_postcode=models.CharField(max_length=5)
	ship_city=models.CharField(max_length=30)


	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	#Foreign Key
	bill_state=models.ForeignKey(State, null=True, blank=True)
	#ship_state=models.ForeignKey(State, null=True, blank=True)
	
	def __str__(self):
		return self.code

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	company_name = models.CharField(max_length = 50)
	birthdate=models.DateTimeField()

class Supplier(models.Model):
	code = models.CharField(max_length = 20)
	fullname = models.CharField(max_length = 50)
	license_no= models.CharField(max_length = 20)
	business_nature= models.CharField(max_length = 20)
		
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return self.code

class Inventory(models.Model):
	code = models.CharField(max_length = 20)
	description = models.CharField(max_length = 50)
	remark = models.CharField(max_length = 100)
	
	imgFile = models.FileField(upload_to='documents/')
	
	#Foreign Key
	dim_unit = models.ForeignKey(DIM_Unit, null=True, blank = True)
	dim_category = models.ForeignKey(DIM_Category, null=True, blank = True)
	dim_subcategory = models.ForeignKey(DIM_SubCategory, null=True, blank = True)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class Price(models.Model):
	code = models.CharField(max_length = 20)
	unit_price = models.DecimalField(max_digits=6, decimal_places = 2, default=0)
	
	eff_datetime=models.DateTimeField(default=timezone.now)
	exp_datetime=models.DateTimeField()

	#Foreign Key
	inventory = models.ForeignKey(Inventory)
	customer = models.ForeignKey(Customer)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class Tax(models.Model):
	code = models.CharField(max_length = 20)
	unit_price = models.DecimalField(max_digits=6, decimal_places = 2)
	
	eff_datetime=models.DateTimeField(default=timezone.now)
	exp_datetime=models.DateTimeField()

	#Foreign Key
	inventory = models.ForeignKey(Inventory)
	gst = models.ForeignKey(DIM_GST)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code
		
class Review(models.Model):
	description = models.CharField(max_length = 50)
	
	#Foreign Key
	inventory = models.ForeignKey(Inventory)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description


class DIM_Promotion(models.Model):
	code = models.CharField(max_length = 20)
	description = models.CharField(max_length = 50)
	
	promo_cond = models.CharField(max_length = 50)
	promo_percent = models.DecimalField(max_digits=4, decimal_places = 2)
	promo_amt = models.DecimalField(max_digits=6, decimal_places = 2)
	
	#Foreign Key
	inventory = models.ForeignKey(Inventory)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.code

class Sales(models.Model):
	si_no = models.CharField(max_length = 20, default = "")
	description = models.CharField(max_length = 50)
	sales_date = models.DateField(default = timezone.now)
	doc_amt = models.DecimalField(max_digits=7, decimal_places = 2,default = 0)
	doc_gst_amt = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	doc_net_amt = models.DecimalField(max_digits=7, decimal_places = 2,default = 0)
	doc_promotion_amt = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	remark = models.CharField(max_length = 100)
	
	# Foreign Key
	
	customer = models.ForeignKey(User)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.si_no

	def get_absolute_url(self):
		return reverse('sales_edit', kwargs={'slug':self.slug})
	
class Sales_Det(models.Model):
	seq = models.IntegerField(default = 1)
	qty = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	unit_price = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	gst_amt = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	det_amt = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	net_amt = models.DecimalField(max_digits=6, decimal_places = 2,default = 0)
	
	#Foreign Key
	sales = models.ForeignKey(Sales, null = True)
	inventory = models.ForeignKey(Inventory)
	promotion = models.ForeignKey(DIM_Promotion, null=True)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.seq

class Purchase(models.Model):
	pi_no = models.CharField(max_length = 20, default = "")
	description = models.CharField(max_length = 50)
	purchase_date = models.DateTimeField(default = timezone.now)
	doc_amt = models.DecimalField(max_digits=7, decimal_places = 2)
	doc_gst_amt = models.DecimalField(max_digits=6, decimal_places = 2)
	doc_promotion_amt = models.DecimalField(max_digits=6, decimal_places = 2)
	remark = models.CharField(max_length = 100)
	
	# Foreign Key
	supplier = models.ForeignKey(Supplier)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.pi_no

class Purchase_Det(models.Model):

	seq = models.IntegerField(default = 1)
	qty = models.DecimalField(max_digits=6, decimal_places = 2)
	gst_amt = models.DecimalField(max_digits=6, decimal_places = 2)
	det_amt = models.DecimalField(max_digits=6, decimal_places = 2)
	
	#Foreign Key
	purchase = models.ForeignKey(Purchase)
	inventory = models.ForeignKey(Inventory)
	promotion = models.ForeignKey(DIM_Promotion)
	
	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.seq

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
    # if created:
        # Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
    # instance.profile.save()
	
class WebTemplate(models.Model):

	description = models.CharField(max_length = 50)
	pageTitle = models.CharField(max_length = 200)
	
	pageSectionHeader = models.CharField(max_length = 50)
	pageSectionArticle = models.CharField(max_length = 200)

	pageSectionimgFile = models.FileField(upload_to='documents/Template/', null=True, blank = True)

	pageURL = models.URLField(null=True, blank = True)

	created_datetime=models.DateTimeField(auto_now_add=True)
	updated_datetime=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description