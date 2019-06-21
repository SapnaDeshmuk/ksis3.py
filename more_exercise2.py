number_of_student=int(raw_input("number_of_student"))
expense_of_one_student=int(raw_input("expense_of_one_student"))
total_expense=number_of_student*expense_of_one_student
print total_expense
if total_expense<=50000:
	print"under budget"
else:
	print"out of budget"


