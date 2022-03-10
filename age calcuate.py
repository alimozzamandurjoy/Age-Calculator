def findAge(current_date, current_month, current_year,
			birth_date, birth_month, birth_year):

	
	
	month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if (birth_date > current_date):
		current_month = current_month - 1
		current_date = current_date + month[birth_month-1]
		
		
	
	if (birth_month > current_month):		
		current_year = current_year - 1
		current_month = current_month + 12
		
	calculated_date = current_date - birth_date
	calculated_month = current_month - birth_month
	calculated_year = current_year - birth_year
	
	print( "Your Present Age is: ", calculated_year, "Years" ,calculated_month,"Months", calculated_date, "Days")
	

current_d = input("Enter the Current Date: ")
current_m =input("Enter the Current month: ")
current_y = input("Enter the Current year: ")

current_date= int(current_d)
current_month = int(current_m)
current_year = int(current_y)



birth_d= input("Enter the Birthday Date: ")
birth_m =input("Enter the Birthday month: ")
birth_y= input("Enter the Birthday year: ")


birth_date= int(birth_d)
birth_month= int(birth_m)
birth_year= int(birth_y)

findAge(current_date, current_month, current_year,birth_date, birth_month, birth_year)
