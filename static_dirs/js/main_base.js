var myMenu = document.getElementById("myMenu");
var menuOpen;
var cover=document.getElementById("cover");
var pop=document.getElementById("frmPop");
var pop_body=document.getElementById("lblBody");
var content_body=document.getElementById("myContent");
var pop_content=document.getElementsByClassName("pop-content")[0];
var span = document.getElementsByClassName("close")[0];
var container=document.getElementsByClassName("container")[0];

function showLoader(){
//hide after finish loading
	hidePage();
}

function showPage(){
	//$("body").css("overflow","hidden");
	//alert(9);
	//document.getElementById("loader-container").style.zIndex="1500";
	//document.getElementById("loading").style.zIndex="1600";
}

function hidePage(){
	//alert(0);
	//document.getElementById("loader-container").style.zIndex="999";
	//document.getElementById("loading").style.zIndex="-999";
}

function test(){

	var a=$.ajax({ 
		method: "GET",
		url: "/price/get/",
		dataType:'json',
		data: { price_list:"price_list" },
		beforeSend: function(){
			showPage();
		},
		success: function(data){

			for(var i = 0 ; i < data.length ; i++)
			{
				var price = data[i];
				var unit_price= price["fields"]["unit_price"];
				var qty = document.getElementById("id_qty").value;
				var txtDetAmt = document.getElementById("id_det_amt");
				var txtNetAmt = document.getElementById("id_net_amt");
				var txtGSTAmt = document.getElementById("id_gst_amt");
				var txtUnitPrice = document.getElementById("id_unit_price");
				
				txtUnitPrice.value = unit_price;
				txtDetAmt.value = Math.round(qty * unit_price);
				txtGSTAmt.value = Math.round(txtDetAmt.value * 0.06);
				txtNetAmt.value = parseInt(txtDetAmt.value) + parseInt(txtGSTAmt.value);
				
			}
			
			hidePage();
		}
	})
}


function test2(inv_id){
	var a=$.ajax({ 
		method: "POST",
		url: "/price/get/2/"+inv_id+"/",
		dataType:'json',
		//data: { cust_id:"2", inv_id:"2" },
		beforeSend: function(){
			showPage();
		},
		success: function(data){

			for(var i = 0 ; i < data.length ; i++)
			{
				var price = data[i];
				var unit_price= price["fields"]["unit_price"];
				var qty = 100;
				var txtDetAmt = document.getElementById("id_det_amt");
				var txtNetAmt = document.getElementById("id_net_amt");
				var txtGSTAmt = document.getElementById("id_gst_amt");
				var txtUnitPrice = document.getElementById("id_unit_price");
				var lblAmt = document.getElementById("amt");
				
				txtUnitPrice.value = unit_price;
				txtDetAmt.value = Math.round(qty * unit_price);
				txtGSTAmt.value = Math.round(txtDetAmt.value * 0.06);
				txtNetAmt.value = parseInt(txtDetAmt.value) + parseInt(txtGSTAmt.value);
				lblAmt.innerHTML = txtNetAmt.value;
				
			}
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){hidePage();}

	})
}

//sales
function doSales(inv_id, qty){
	//print(inv_id, qty)
	var a=$.ajax({ 
		method: "POST",
		url: "/doSales/"+inv_id+"/"+qty+"/",
		dataType:'json',
		beforeSend: function(){
			showPage();
		},
		success: function(data){

			for(var i = 0 ; i < data.length ; i++)
			{
				var price = data[i];
				if (price["model"]=="retail.sales"){
					var lblCartAmtTotal = document.getElementById("amt");
					lblCartAmtTotal.innerHTML=parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}

				var unit_price= price["fields"]["unit_price"];
				var qty = 100;
				var txtDetAmt = document.getElementById("id_det_amt");
				var txtNetAmt = document.getElementById("id_net_amt");
				var txtGSTAmt = document.getElementById("id_gst_amt");
				var txtUnitPrice = document.getElementById("id_unit_price");
				var lblAmt = document.getElementById("amt");
				
				txtUnitPrice.value = unit_price;
				txtDetAmt.value = price["fields"]["det_amt"];
				txtGSTAmt.value = price["fields"]["gst_amt"];
				txtNetAmt.value = price["fields"]["net_amt"];
				//lblAmt.innerHTML = txtNetAmt.value;
				
			}
			
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){hidePage();}

	})
}

//sales modal
function doSalesModal(inv_id, qty, iscart){
	//print(inv_id, qty)
	var a=$.ajax({ 
		method: "POST",
		url: "/doSales/"+inv_id+"/"+qty+"/",
		dataType:'json',
		beforeSend: function(){
			
			showPage();
		},
		success: function(data){
			var lblAmt1 = document.getElementById("amt");
			lblAmt1.disabled=false;
			
			for(var i = 0 ; i < data.length ; i++)
			{
				
				var price = data[i];
				//print("success sales:" + price)
				if (price["model"]=="retail.sales" && iscart==false){
					var lblCartAmtTotal = document.getElementById("amt");
					lblCartAmtTotal.innerHTML=parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}
				
			if (iscart){
				if (price["model"]=="retail.sales_det"){
					var unit_price= price["fields"]["unit_price"];
					var txtDetAmt = document.getElementById("mod_id_det_amt__" + price["fields"]["seq"]);
					var txtNetAmt = document.getElementById("mod_id_net_amt__" + price["fields"]["seq"]);
					var txtGSTAmt = document.getElementById("mod_id_gst_amt__" + price["fields"]["seq"]);
					var txtUnitPrice = document.getElementById("mod_id_unit_price__" + price["fields"]["seq"]);

					
					txtDetAmt.innerHTML = parseFloat(price["fields"]["det_amt"]).toFixed(2);
					txtGSTAmt.innerHTML = parseFloat(price["fields"]["gst_amt"]).toFixed(2);
					txtNetAmt.innerHTML = parseFloat(price["fields"]["net_amt"]).toFixed(2);
					
				}
				
				if (price["model"]=="retail.sales"){

					var txtDetAmtTotal = document.getElementById("mod_id_doc_amt_total");
					var txtNetAmtTotal = document.getElementById("mod_id_doc_net_amt_total");
					var txtGSTAmtTotal = document.getElementById("mod_id_doc_gst_amt_total");
					

					
					txtDetAmtTotal.innerHTML = parseFloat(price["fields"]["doc_amt"]).toFixed(2);
					txtGSTAmtTotal.innerHTML = parseFloat(price["fields"]["doc_gst_amt"]).toFixed(2);
					txtNetAmtTotal.innerHTML = parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
					
					lblAmt1.innerHTML = parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}
				

				//alert(price["fields"]["net_amt"]);
				
			}
			
			
			}
			

		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){hidePage();}

	})
}

function updateQty(id, mod, iscart){
		// Get the field name
		var buttonName = id;
		var n = buttonName.lastIndexOf("__");
		var invID = buttonName.substring(n)
		invID = invID.replace("__", "");
		txtQtyName="quantity__" + invID;
        
		var txtQty = document.getElementById(txtQtyName);
        var quantity = parseInt(txtQty.value);
		
		if ((quantity + mod) >= 0 ){
			quantity = quantity + mod;
			txtQty.value = quantity;
			doSalesModal(invID, quantity, iscart);
		}
		

}

function confirmModal(goBack=false){
	
	if(goBack){
	    $('#myModal3').modal('hide');  
	
			var lblMsgEmail = document.getElementById("msgEmail");
			var lblMsgCancel = document.getElementById("msgCancel");
			var footer = document.getElementById("footer");
				
			lblMsgEmail.style.visibility="visible";
			lblMsgCancel.style.visibility="hidden";
			footer.style.visibility="hidden";

		$('#myModal1').modal('show');  
	}
	else{
		$('#myModal1').modal('hide');  
	
		var lblMsgEmail = document.getElementById("msgEmail");
		var lblMsgCancel = document.getElementById("msgCancel");
		var footer = document.getElementById("footer");
			
		lblMsgEmail.style.visibility="hidden";
		lblMsgCancel.style.visibility="visible";
		footer.style.visibility="visible";
	
        $('#myModal3').modal('show');  
	}
	
}//sales modal

function cancelSales(){
	var a=$.ajax({ 
		method: "POST",
		url: "/cancelSales/",
		dataType:'json',
		beforeSend: function(){
			showPage();
		},
		success: function(data){
			$("#salesOrder_body").empty();
			
			for(var i = 0 ; i < data.length ; i++)
			{
				
				var price = data[i];
				if (price["model"]=="retail.sales"){
					var lblCartAmtTotal = document.getElementById("amt");
					lblCartAmtTotal.innerHTML=parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}

				if (price["model"]=="retail.sales_det"){
					var unit_price= price["fields"]["unit_price"];
					var txtDetAmt = document.getElementById("mod_id_det_amt__" + price["fields"]["seq"]);
					var txtNetAmt = document.getElementById("mod_id_net_amt__" + price["fields"]["seq"]);
					var txtGSTAmt = document.getElementById("mod_id_gst_amt__" + price["fields"]["seq"]);
					var txtUnitPrice = document.getElementById("mod_id_unit_price__" + price["fields"]["seq"]);
					var lblAmt = document.getElementById("amt");
					lblAmt.disabled=true;
					lblAmt.innerHTML = '';
			

					
					txtDetAmt.innerHTML = parseFloat(price["fields"]["det_amt"]).toFixed(2);
					txtGSTAmt.innerHTML = parseFloat(price["fields"]["gst_amt"]).toFixed(2);
					txtNetAmt.innerHTML = parseFloat(price["fields"]["net_amt"]).toFixed(2);
					
				}
				
				if (price["model"]=="retail.sales"){

					var txtDetAmtTotal = document.getElementById("mod_id_doc_amt_total");
					var txtNetAmtTotal = document.getElementById("mod_id_doc_net_amt_total");
					var txtGSTAmtTotal = document.getElementById("mod_id_doc_gst_amt_total");
					
					
					txtDetAmtTotal.innerHTML = parseFloat(price["fields"]["doc_amt"]).toFixed(2);
					txtGSTAmtTotal.innerHTML = parseFloat(price["fields"]["doc_gst_amt"]).toFixed(2);
					txtNetAmtTotal.innerHTML = parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}
				

				//alert(price["fields"]["net_amt"]);
				
			}
			
			$('#myModal3').modal('hide');  
			//$('#myModal1').modal('show');  

			//confirmModal(true);
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){hidePage();}

	})
}

function checkout(){
		var a=$.ajax({ 
		method: "POST",
		url: "/checkout/",
		dataType:'json',
		beforeSend: function(){
			showPage();
		},
		success: function(data){
			$('#myModal1').modal('hide');  
			
			var lblMsgEmail = document.getElementById("msgEmail");
			var lblMsgCancel = document.getElementById("msgCancel");
			var footer = document.getElementById("footer");
			var lblAmt = document.getElementById("amt");
				
			lblMsgEmail.style.visibility="visible";
			lblMsgCancel.style.visibility="hidden";
			footer.style.visibility="hidden";
			lblAmt.innerHTML = '';
			lblAmt.disabled=true;
			$('#myModal3').modal('show');  

		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){hidePage();}

	})
}

$(document).ready(function($) {
			$('body').on('hidden.bs.modal', '.modal', function () {
	$(this).removeData('bs.modal');
	});
	
	

 $('#loginForm').on('submit',function (ev) {
                alert('ok');
	      $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
  			window.parent.closeModal();
            }
        });

    });
		
		$('.tabs').on('click', 'li a', function(e){
			alert(11);
  e.preventDefault();
  var $tab = $(this),
       href = $tab.attr('href');

   $('.active').removeClass('active');
   $tab.addClass('active');

   $('.show')
      .removeClass('show')
      .addClass('hide')
      .hide();
  
    $(href)
      .removeClass('hide')
      .addClass('show')
      .hide()
      .fadeIn(550);
});
		

	function testTab(){
	  //e.preventDefault();
  var $tab = $(this);
       href = $tab.attr('href');

   $('.active').removeClass('active');
   $tab.addClass('active');

   $('.show')
      .removeClass('show')
      .addClass('hide')
      .hide();
  
    $(href)
      .removeClass('hide')
      .addClass('show')
      .hide()
      .fadeIn(550);
	}
	
	//(function($){
  (function($) {
$.fn.menumaker = function(options) {  
 var cssmenu = $(this), settings = $.extend({
   format: "dropdown",
   sticky: false
 }, options);
 return this.each(function() {
   $(this).find(".button").on('click', function(){
     $(this).toggleClass('menu-opened');
     var mainmenu = $(this).next('ul');
     if (mainmenu.hasClass('open')) { 
       mainmenu.slideToggle().removeClass('open');
     }
     else {
       mainmenu.slideToggle().addClass('open');
       if (settings.format === "dropdown") {
         mainmenu.find('ul').show();
       }
     }
   });
   cssmenu.find('li ul').parent().addClass('has-sub');
multiTg = function() {
     cssmenu.find(".has-sub").prepend('<span class="submenu-button"></span>');
     cssmenu.find('.submenu-button').on('click', function() {
       $(this).toggleClass('submenu-opened');
       if ($(this).siblings('ul').hasClass('open')) {
         $(this).siblings('ul').removeClass('open').slideToggle();
       }
       else {
         $(this).siblings('ul').addClass('open').slideToggle();
       }
     });
   };
   if (settings.format === 'multitoggle') multiTg();
   else cssmenu.addClass('dropdown');
   if (settings.sticky === true) cssmenu.css('position', 'fixed');
resizeFix = function() {
  var mediasize = 700;
     if ($( window ).width() > mediasize) {
       cssmenu.find('ul').show();
     }
     if ($(window).width() <= mediasize) {
       cssmenu.find('ul').hide().removeClass('open');
     }
   };
   resizeFix();
   return $(window).on('resize', resizeFix);
 });
  };
})(jQuery);

(function($){
$(document).ready(function(){
$("#cssmenu").menumaker({
   format: "multitoggle"
});
});
})(jQuery);

	});