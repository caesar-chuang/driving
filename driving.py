country = input('which country are you:')
age = input('your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can get driver licence')
	else:
		print('You can not get driver licence')