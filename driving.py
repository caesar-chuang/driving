country = input('which country are you:')
age = input('your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can get driver licence')
	else:
		print('You can not get driver licence')
elif country == 'USA':
    if age >= 16:
        print('You can get driver licence')
    else:
        print('you can not get driver licence') 
else:
    print('You can only input Taiwan or USA')           		