

$(document).ready(function () {

	$('[data-toggle="offcanvas"]').click(function () {
		$('.row-offcanvas').toggleClass('active')
	});
  
	var url = "/login";
	jQuery('#modellink').click(function(e) {
var targetElement = e.target;
		$('.modal-container').load(url,function(result){
		//	$('#myModal').modal({show:true});
		});
	});

//sales
function doSales(inv_id, qty){
	//print(inv_id, qty)
	var a=$.ajax({ 
		method: "POST",
		url: "/doSales/"+inv_id+"/"+qty+"/",
		dataType:'json',
		beforeSend: function(){
			alert('sending');
		//	showPage();
		},
		success: function(data){
			alert('sent');

			for(var i = 0 ; i < data.length ; i++)
			{
				var price = data[i];
				if (price["model"]=="retail.sales"){
					var lblCartAmtTotal = document.getElementById("amt");
					lblCartAmtTotal.innerHTML=parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}

				/*var unit_price= price["fields"]["unit_price"];
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
				*/
			}
			
			
			
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert('sent error');
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){
			alert('completed sent');
			//hidePage();
		}

	})
}

function removeSalesItem(inv_id){
	//print(inv_id, qty)
	var a=$.ajax({ 
		method: "POST",
		url: "/removeSalesItem/"+inv_id+"/",
		dataType:'json',
		beforeSend: function(){
			alert('sending');
		//	showPage();
		},
		success: function(data){
			alert('sent');

			for(var i = 0 ; i < data.length ; i++)
			{
				var price = data[i];
				if (price["model"]=="retail.sales"){
					var lblCartAmtTotal = document.getElementById("amt");
					lblCartAmtTotal.innerHTML=parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}

				/*var unit_price= price["fields"]["unit_price"];
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
				*/
			}
			
			
			
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert('sent error');
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){
			alert('completed sent');
			//hidePage();
		}

	})
}


function checkout(){
		var a=$.ajax({ 
		method: "POST",
		url: "/checkout/",
		dataType:'json',
		beforeSend: function(){
			
		},
		success: function(data){
			alert("Thanks");
			/*
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
*/
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){}

	})
}

function cancelSales(){
	
	var a=$.ajax({ 
		method: "POST",
		url: "/cancelSales/",
		dataType:'json',
		beforeSend: function(){
		},
		success: function(data){
			
			for(var i = 0 ; i < data.length ; i++)
			{
				
				var price = data[i];
				if (price["model"]=="retail.sales"){
					var lblCartAmtTotal = document.getElementById("amt");
					lblCartAmtTotal.innerHTML=parseFloat(price["fields"]["doc_net_amt"]).toFixed(2);
				}

/*				if (price["model"]=="retail.sales_det"){
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
*/				

				//alert(price["fields"]["net_amt"]);
				
			}
			
		},
		error: function (xhr, ajaxOptions, thrownError) {
			alert(xhr.status);
			alert(thrownError);
		},
		complete: function(){}

	})
}
	document.onclick = function(event) {
		var targetElement = event.target;
		if ( targetElement.className == "btnCart" ) {
		   
			var invId = targetElement.id.replace("inv_", "");
			var txtqty = document.getElementById("inv_" + invId + "_Qty");
			qty = txtqty.value;
			doSales(invId, qty);
		}   

		if ( targetElement.id == "btnCancel" ) {
			cancelSales();
			//targetElement.classList.add('open');
			//targetElement.parent('a').addClass('open');
		}   

		if ( targetElement.className == "btnRemove" ) {
			var invId = targetElement.id.replace("inv_", "");
			
			removeSalesItem(invId);
		}  

		if ( targetElement.id == "btnCheckout" ) {
			checkout();
		}  		
	};


});


	