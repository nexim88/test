
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
#from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		url(r'^__debug__/', include(debug_toolbar.urls)),
		url(r'^$', views.index, name='index',),
		url(r'^$', views.home, name='home',),
		url(r'^dashboard/$', views.dashboard, name='dashboard_index',),
		url(r'^about/$', views.about, name='about',),
		url(r'^contact/$', views.contact, name='contact',),
		
		url(r'^login/$', views.login, name='login',),
		url(r'^register/$', views.register, name='register',),
		
		url(r'^accounts/login/$', views.auth_view, name='loggedIn'),
		url(r'^accounts/logout/$', views.auth_view, name='logout'),
		
		url(r'^docno/$', views.docno_list, name='docno_list',),
		url(r'^docno/new$', views.docno_edit, name='docno_new',),
		url(r'^docno/edit/(?P<pk>\d+)/$', views.docno_edit, name='docno_edit',),
		url(r'^docno/delete/(?P<pk>\d+)/$', views.docno_delete, name='docno_delete',),

		url(r'^state/$', views.state_list, name='state_list',),
		url(r'^state/new$', views.state_edit, name='state_new',),
		url(r'^state/edit/(?P<pk>\d+)/$', views.state_edit, name='state_edit',),
		url(r'^state/delete/(?P<pk>\d+)/$', views.state_delete, name='state_delete',),

		url(r'^gst/$', views.gst_list, name='gst_list',),
		url(r'^gst/new$', views.gst_edit, name='gst_new',),
		url(r'^gst/edit/(?P<pk>\d+)/$', views.gst_edit, name='gst_edit',),
		url(r'^gst/delete/(?P<pk>\d+)/$', views.gst_delete, name='gst_delete',),

		url(r'^post/$', views.post_list, name='post_list',),
		url(r'^post/new$', views.post_edit, name='post_new',),
		url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit',),
		url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete',),

		url(r'^unit/$', views.unit_list, name='unit_list',),
		url(r'^unit/new$', views.unit_edit, name='unit_new',),
		url(r'^unit/edit/(?P<pk>\d+)/$', views.unit_edit, name='unit_edit',),
		url(r'^unit/delete/(?P<pk>\d+)/$', views.unit_delete, name='unit_delete',),

		url(r'^category/$', views.category_list, name='category_list',),
		url(r'^category/new$', views.category_edit, name='category_new',),
		url(r'^category/edit/(?P<pk>\d+)/$', views.category_edit, name='category_edit',),
		url(r'^category/delete/(?P<pk>\d+)/$', views.category_delete, name='category_delete',),

		url(r'^subcategory/$', views.subcategory_list, name='subcategory_list',),
		url(r'^subcategory/new$', views.subcategory_edit, name='subcategory_new',),
		url(r'^subcategory/edit/(?P<pk>\d+)/$', views.subcategory_edit, name='subcategory_edit',),
		url(r'^subcategory/delete/(?P<pk>\d+)/$', views.subcategory_delete, name='subcategory_delete',),

		url(r'^tax/$', views.tax_list, name='tax_list',),
		url(r'^tax/new$', views.tax_edit, name='tax_new',),
		url(r'^tax/edit/(?P<pk>\d+)/$', views.tax_edit, name='tax_edit',),
		url(r'^tax/delete/(?P<pk>\d+)/$', views.tax_delete, name='tax_delete',),

		url(r'^contact_type/$', views.contacttype_list, name='contact_type_list',),
		url(r'^contact_type/new$', views.contacttype_edit, name='contact_type_new',),
		url(r'^contact_type/edit/(?P<pk>\d+)/$', views.contacttype_edit, name='contact_type_edit',),
		url(r'^contact_type/delete/(?P<pk>\d+)/$', views.contacttype_delete, name='contact_type_delete',),

		url(r'^contact_info/$', views.contactinfo_list, name='contact_info_list',),
		url(r'^contact_info/new/$', views.contactinfo_edit, name='contact_info_new',),
		url(r'^contact_info/edit/(?P<pk>\d+)/$', views.contactinfo_edit, name='contact_info_edit',),
		url(r'^contact_info/delete/(?P<pk>\d+)/$', views.contactinfo_delete, name='contact_info_delete',),

		#url(r'^contact_info/new/(?P<contacttype_id>\d+)/$', views.contactinfo_new, name='contact_info_new',),
		#url(r'^contact_info/view/(?P<pk>\d+)/$', views.contactinfo_view, name='contact_info_view',),
		#url(r'^contact_info/new/(?P<contacttype_id>\d+)/$', views.contact_info_new, name='contact_info_new',),
		#url(r'^contact_info/edit/(?P<pk>\d+)/(?P<contacttype_id>\d+)/$', views.UpdateContactInfoView.as_view(), name='contact_info_edit',),
		
		url(r'^review/$', views.ListReviewView.as_view(), name='review_list',),
		url(r'^review/new$', views.CreateReviewView.as_view(), name='review_new',),
		url(r'^review/edit/(?P<pk>\d+)/$', views.UpdateReviewView.as_view(), name='review_edit',),
		url(r'^review/delete/(?P<pk>\d+)/$', views.DeleteReviewView.as_view(), name='review_delete',),

		url(r'^inventory/$', views.inventory_list, name='inventory_list',),
		url(r'^inventory/new$', views.inventory_edit, name='inventory_new',),
		url(r'^inventory/view/(?P<pk>\d+)/$', views.inventory_edit, name='inventory_view',),
		url(r'^inventory/edit/(?P<pk>\d+)/$', views.inventory_edit, name='inventory_edit',),
		url(r'^inventory/delete/(?P<pk>\d+)/$', views.inventory_delete, name='inventory_delete',),

		url(r'^inventory/view/(?P<v>\w+)/(?P<pk>\d+)/$', views.inventory_web_view, name='inventory_web_view',),
		url(r'^products/(?P<type>\w+)/$', views.inventory_stationery_view, name='inventory_stationery_view',),
		
		url(r'^price/$', views.price_list, name='price_list',),
		url(r'^price/new$', views.price_edit, name='price_new',),
		url(r'^price/view/(?P<pk>\d+)/$', views.price_edit, name='price_view',),
		url(r'^price/edit/(?P<pk>\d+)/$', views.price_edit, name='price_edit',),
		url(r'^price/delete/(?P<pk>\d+)/$', views.price_delete, name='price_delete',),

		url(r'^price/get/(?P<cust_id>\d+)/(?P<inv_id>\d+)/$', views.price_get, name='price_get',),

		url(r'^promotion/$', views.promotion_list, name='promotion_list',),
		url(r'^promotion/new$', views.promotion_edit, name='promotion_new',),
		url(r'^promotion/edit/(?P<pk>\d+)/$', views.promotion_edit, name='promotion_edit',),
		url(r'^promotion/delete/(?P<pk>\d+)/$', views.promotion_delete, name='promotion_delete',),

		url(r'^supplier/$', views.supplier_list, name='supplier_list',),
		url(r'^supplier/new$', views.supplier_edit, name='supplier_new',),
		url(r'^supplier/edit/(?P<pk>\d+)/$', views.supplier_edit, name='supplier_edit',),
		url(r'^supplier/delete/(?P<pk>\d+)/$', views.supplier_delete, name='supplier_delete',),


		url(r'^customer/$', views.customer_list, name='customer_list',),
		url(r'^customer/new$', views.customer_edit, name='customer_new',),
		url(r'^customer/view/(?P<pk>\d+)/$', views.customer_edit, name='customer_view',),
		url(r'^customer/edit/(?P<pk>\d+)/$', views.customer_edit, name='customer_edit',),
		url(r'^customer/delete/(?P<pk>\d+)/$', views.customer_delete, name='customer_delete',),

		url(r'^sales/$', views.sales_list, name='sales_list',),
		url(r'^sales/new$', views.sales_edit, name='sales_new',),
		url(r'^sales/view/(?P<pk>\d+)/$', views.sales_edit, name='sales_view',),
		url(r'^sales/edit/(?P<pk>\d+)/$', views.sales_edit, name='sales_edit',),
		url(r'^sales/delete/(?P<pk>\d+)/$', views.sales_delete, name='sales_delete',),
			
		url(r'^sales/det/new$', views.sales_det_new, name='sales_det_new',),
		url(r'^sales/det/edit/(?P<pk>\d)+/$', views.sales_det_edit, name='sales_det_edit',),
		url(r'^sales/det/delete/(?P<pk>\d+)/$', views.sales_det_delete, name='sales_det_delete',),

		url(r'^doSales/(?P<inv_id>\d+)/(?P<qty>\d+)/$', views.doSales, name='doSales',),
		url(r'^cancelSales/$', views.cancelSales, name='cancelSales',),
		url(r'^removeSalesItem/(?P<inv_id>\d+)/$', views.removeSalesItem, name='removeSalesItem',),
		url(r'^sales/view/$', views.sales_web_view, name='sales_web_view',),
		url(r'^checkout/$', views.checkout, name='checkout',),

			
		url(r'^purchase/$', views.purchase_list, name='purchase_list',),
		url(r'^purchase/new$', views.purchase_edit, name='purchase_new',),
		url(r'^purchase/edit/(?P<pk>\d+)/$', views.purchase_edit, name='purchase_edit',),
		url(r'^purchase/delete/(?P<pk>\d+)/$', views.purchase_delete, name='purchase_delete',),
			
		url(r'^purchase/det/new$', views.purchase_det_new, name='purchase_det_new',),
		url(r'^purchase/det/edit/(?P<pk>\d)+/$', views.purchase_det_edit, name='purchase_det_edit',),
		url(r'^purchase/det/delete/(?P<pk>\d+)/$', views.purchase_det_delete, name='purchase_det_delete',),
	]

	urlpatterns += staticfiles_urlpatterns()
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)