import pandas as pd

def finals():
	subtot = 0
	sales_tax = 0
	
	for i in costs:
		subtot += i
	
	print('\nSubtotal:', '$', "{:.2f}".format(subtot))
	
	for n in taxes:
		sales_tax += n
	print('Sales Tax:', '$', "{:.2f}".format(sales_tax))
	
	total = subtot + sales_tax
	print('\nTotal: $', "{:.2f}".format(total))
		


#invoice() 
	
name = str(input('\nEnter your name: '))
address = str(input('Enter your address: '))
date = str(input('Enter the date: '))
acc_num = str(input('Enter your account number: ' ))
	
values = {}
items = []
prices = []
quantities = []
taxables = []
costs = []
taxes = []
	
#listing()

nm = str(input('\nEnter item name: '))
price = float(input('Price: ' ))
quantity = float(input('Quantity: '))
taxable = str(input('Taxable (true or false): '))
taxable = taxable.lower()
cost = quantity * price
if taxable == 'true':
	stat = str(input('Enter your state: ' ))
	stat = stat.upper()

	if stat == 'MD':
		tax = cost * 0.06
	elif stat == 'DC':
		tax = cost * 0.053
	elif stat == 'VA':
		tax = cost * 0.0575
	else:
		tax = cost * 0.05
else:
	tax = 0
add_item = str(input('Add another item (y/n): '))
add_item = add_item.lower()
	
#add_dic()

items.append(nm)
prices.append(price)
quantities.append(quantity)
taxables.append(taxable)
costs.append(cost)
taxes.append(tax)


while add_item != 'n':
	#listing()

	nm = str(input('\nEnter item name: '))
	price = float(input('Price: ' ))
	quantity = float(input('Quantity: '))
	taxable = str(input('Taxable (true or false): '))
	taxable = taxable.lower()
	cost = quantity * price
	
	if taxable == 'true':
		stat = str(input('Enter your state: ' ))
		stat = stat.upper()

		if stat == 'MD':
			tax = cost * 0.06
		elif stat == 'DC':
			tax = cost * 0.053
		elif stat == 'VA':
			tax = cost * 0.0575
		else:
			tax = cost * 0.05
	else: 
		tax = 0
		
	add_item = str(input('Add another item (y/n): '))
	add_item = add_item.lower()
		
	#add_dic()

	items.append(nm)
	prices.append(price)
	quantities.append(quantity)
	taxables.append(taxable)
	costs.append(cost)
	taxes.append(tax)

print('\nCustomer name:', name)
print('Address:', address)
print('Date:', date)
print('Account number:', acc_num, '\n')

values['Item Name'] = items
values['Quantity'] = quantities
values['Price'] = prices
values['Cost'] = costs
values['Taxable'] = taxables

###print dictionary to check
#print(values)
#print('\n', taxes)

###Print table
print('\n')
tabled = pd.DataFrame.from_dict(values)
##remove index and set first row as headers
print(tabled)

finals()

