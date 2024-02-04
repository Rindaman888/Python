height = input('Enter You height: ')
weight = input('Enter You weight: ')

#print(height)
#print(weight)

weight_f = int(weight)
height_f = float(height)
bmi = weight_f / (height_f * height_f)

print(float(bmi))