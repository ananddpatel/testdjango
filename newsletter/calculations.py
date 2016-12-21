"""Women: BMR = 655 + (9.6 x weight in kg) + (1.8 x height in cm) - (4.7 x age in years)

Men: BMR = 66 + (13.7 x weight in kg) + (5 x height in cm) - (6.8 x age in years)"""

modifiers = {
	'Male': {
		'mod': 66,
		'weight': 13.7,
		'height': 5,
		'age': 6.8
	},
	'Female':{
		'mod': 655,
		'weight': 9.6,
		'height': 1.8,
		'age': 4.7
	},
}

def calculate_eer(sex, age, weight, height):
	# imperial numbers
	# set perameter for metric/imperial
	mods = modifiers.get(sex)

	sex_mod = mods.get('mod')
	age_mod = mods.get('age')
	weight_mod = mods.get('weight')
	height_mod = mods.get('height')

	age = int(age)
	weight = int(weight)
	height = int(height)
 	
 	# calculate eer here
	eer = sex_mod + (weight_mod*weight) + (height_mod*height) - (age_mod*age)
	rounded_eer = round(eer, 2)

	return rounded_eer
