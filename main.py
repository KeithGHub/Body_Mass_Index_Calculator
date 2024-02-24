height = float(input('enter the height in inches: '))
weight = float(input('enter the weight in lbs: '))

def BMI(height, weight):
    BMI = weight/(height * height) * 703
    if (BMI < 16):
        return "Severely underweight", BMI

    elif (BMI >= 16 and BMI < 18.5):
        return "Unerweight", BMI

    elif (BMI >= 18.5 and BMI < 25):
        return "Healthy Weight", BMI

    elif (BMI >= 25 and BMI < 38):
        return "Overweight", BMI

    elif (BMI >= 38):
        return "Obese", BMI

Quote, BMI = BMI(height, weight)
print("Your BMI is {} and you are {}".format(BMI, Quote))