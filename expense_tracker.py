print("="*45,"\n")
print(f"PERSONAL EXPENSE TRACKER".center(65))
print("="*45,"\n")
categories = ["Food","Transport","Entertainment","Shopping","Bills","Others"]
expenses = []
expense = {}
total = 0
while True:
 print("1. Add new expenses")
 print("2. View all expenses")
 print("3. Category summary")
 print("4. Set/Check Budget")
 print("5. Search Expenses")
 print("6. Exit")
 print("="*45,"\n")
 
 choice = int(input("Enter your choice(1-6) :"))
 print("\n")
 if choice == 1:
 	print("--- Add new Expense ---\n")
 	print(f' Available categories : {", ".join(categories)}')
 	category = input("Enter the Category :  ")
 	amount = float(input("Enter the amount : "))
 	desc = input("Enter the description : ")
 	print("\n")
 	expense = { "category":category ,"amount": amount, "description":desc}
 	
 	expenses.append(expense)
 	print("***Expense Added Successfully***\n")
 	add = 0
 	for i in expenses:
 		add = add + 1
 		print(f"Expense no. {add} :")
 		print(f'--Category--||--Amount--||--Description--')
 		print(f' {i["category"]:^15} \t {i["amount"]:^12} \t {i["description"]:^15}  \n')
 	
 	
 elif choice == 2:
 	print("--- Your expenses are as below :---\n")
 	print("—— All expenses ——")
 	count  = 0
 	for j in expenses:
 			count = count + 1
 			total = total + j["amount"]
 			print(f' #{count} |  {j["category"]} |  {j["amount"]} |  {j["description"]}  ')
 	print("-"*40)
 	print(f"Your total expense is : {total} rupees. ")
 	print("\n")	  
 	  
 elif choice == 3:
    cat_summary = {}

    for x in expenses:
        item = x["category"].title()
        amt = x["amount"]

        if item in cat_summary:
            cat_summary[item] += amt
        else:
            cat_summary[item] = amt

    print("---- Category Summary ----")
    categories_sum = 0

    for y, z in cat_summary.items():
        print(f' {y} : {z} rupees ')
        categories_sum += z

    print("-" * 40)
    print(f"Category total : {categories_sum} rupees")
    print("\n")
 	
 	
 	
 	
 elif choice == 4:
 	print("--- Set/Check Budget ---")
 	budget = float(input("Enter your budget :"))
 	total_expense = 0
 	for i in expenses:
 		total_expense = total_expense + i["amount"]
 	if budget > total_expense:
 		print(f"You can still spend some money. You have more {budget - total_expense} rupees to spend")
 	else:
 		print(f"You are out of budget by {budget - total_expense} rupees.")
 		print("-"*40)
 		print("\n")
 	
 	
 	
 elif choice == 5:
 	print("--- Search Expenses ---")
 	Choice = input("Enter type by which tou want to search (category,amount,description) :")
 	if Choice == "category":
 		select_cat = input("Enter category to search :")
 		for i in expenses:
 			if i["category"].title() == select_cat.title():
 				print(f'{i["category"]} | {i["amount"]} | {i["description"]}  ')
 	
 	elif Choice == "amount":
 	            	select_cat = float(input("Enter amount to search : "))
 	            	for i in expenses:
 	            	 if i["amount"] == select_cat:
 	            	 	print(f'{i["category"]} | {i["amount"]} | {i["description"]}   ')
 			            
 	elif Choice == "description":
 		select_cat = input("Enter description to search :")
 		for i in expenses:
 			if i["description"].title() == select_cat.title():
 				print(f'{i["category"]} --> {i["amount"]} --> {i["description"]}   ')
 	print("\n")
 	print("-"*40)
 			
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 elif choice == 6:
 	print("-- Thankyou for visiting.Hope you enjoyed using the tracker!! --")
 	break
 else :
  	print("Invalid option try again.")
 	
  