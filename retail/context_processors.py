def CartObj(request):
	
	sales=request.session.get('sales')
	if sales:
		print('sales:' + str(sales.doc_net_amt))
	else:
		print('not sales')
	return {'sales':sales}