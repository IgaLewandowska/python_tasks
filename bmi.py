weight = float(input("Podaj swoją wagę w [kg]:"))
height = float(input("Podaj swój wzrost w [m]:"))
bmi = weight/(height**2)
print ("Twoje BMI wynosi:", bmi)
if bmi < 16:
	print ("Jest bardzo źle to WYGŁODZENIE")
elif 16<bmi<16.9:
	print ("Jest źle to WYCHUDZENIE")
elif 17<bmi<18.5:
	print ("Uważaj to NIEDOWAGA")
elif 18.5<bmi<24.9:
	print ("Masz prawidłową wagę")
elif 25<bmi<29.9:
	print ("Uważaj to NADWAGA")
elif 30<bmi<34.9:
	print ("Jest źle to OTYŁOŚĆ I STOPNIA")
elif 35<bmi<39.9:
	print ('Jest bardzo źle to OTYŁOŚĆ II STOPNIA')
elif bmi>40:
	print ('EMERGENCY OTYŁOŚĆ III STOPNIA')