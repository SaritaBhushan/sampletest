invList =[]

def getList(l):
	if len(l)==0:
		print("Inventry is Empty.")
	else:
		print("Items in the Inventry:")
		print(l)

def sortList(l):
	if len(l)==0:
		print("Inventry is Empty.")
	else:
		print("Items in the Inventry:")
		print(l.sort())

def add(l, item):
	try:
		if len(l) >=10:
			raise Exception("Overflow: Inventory Capacity Full.")
		
		if item not in l:
			l.append(item)
		else:
			raise Exception("Duplicate: {0} aleady present in the list.".format(item))
	except Exception as e:
		print(e)

	# return l # No need to Return.

def remove(l, item):
	try:
		l.remove(item)
	except ValueError as e:
		print("ValueError: {0} not in list.".format(item))
	except Exception as e:
		print(e)
	# return l # No need to Return.
