height = input('请输入您的身高(m): ')
weight = input('请输入您的体重(kg): ')
height = float(height)
weight = float(weight)
bmi = weight/height**2

if bmi < 18.5:
	print('您的BMI为:', round(bmi,1), '属于体重过轻')
elif bmi >= 18.5 and bmi < 24:
	print('您的BMI为:', round(bmi,1), '属于正常范围')
elif bmi >= 24 and bmi < 27:
	print('您的BMI为:', round(bmi,1), '属于过重')
elif bmi >= 27 and bmi < 30:
	print('您的BMI为:', round(bmi,1), '属于轻度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的BMI为:', round(bmi,1), '属于中度肥胖')
else: 
	print('您的BMI为:', round(bmi,1), '属于重度肥胖')