def menu():


	while True:
		print('\nMain Menu:')
		print('Select Two Sum Algorthem')
		print('Select Algorthem 2 you want to use')
		print('Select Algorthem 3 you want to use')
		print('Select Algorthem 4 you want to use')
		print('Select Algorthem 5 you want to use')
		print('Selct 6 to Exit:')
		choice = int(input('Enter choice: '))

		if choice == 1:
			print('Two Sum')
		elif choice == 2:
			print('Algorthem 2')
		elif choice == 3:
			print('Algorthem 3')
		elif choice == 4:
			print('Algorthem 4')
		elif choice == 5:
			print('Algorthem 5')
		elif choice == 6:
			print('Thank you for your time!')
			break
		else:
			print("Invalid Choice. Please Try Again")
				