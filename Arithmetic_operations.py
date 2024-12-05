
# دالة لحساب الناتج
def calculate_result(theUnits, theNumber, theUniteFrom, theUniteTo):
    try:
        Number = float(theNumber.get())     # لإخال الرقم
        from_value = theUniteFrom.get() # الوحة الأساسية
        to_value = theUniteTo.get()     # الوحدة المحول إليها
        
        if from_value and to_value:
        # للتحويل بين وحدات الطول 
            if theUnits.get() == "Lengths":
                conversion_factors = {
                        ("Kilometers", "Meters"): 1000,
                        ("Meters", "Kilometers"): 1 / 1000,
                        ("Kilometers", "centimeters"): 100000,
                        ("centimeters", "Kilometers"): 1 / 100000,
                        ("Meters", "centimeters"): 100,
                        ("centimeters", "Meters"): 1 / 100,
                }
        # للتحويل بين وحدات الوزن 
            elif theUnits.get() == "Weights":
                conversion_factors = {
                    ("Ton", "Kilograms"): 1000,
                    ("Kilograms", "Ton"): 1 / 1000,
                    ("Kilograms", "Grams"): 1000,
                    ("Grams", "Kilograms"): 1 / 1000,
                    ("Ton", "Grams"): 1000000,
                    ("Grams", "Ton"): 1 / 1000000,
                }   
        # للتحويل بين وحدات درجات الحرارة 
            elif theUnits.get() == "Temperatures":
                if from_value == "Celsius" and to_value == "Fahrenheit":
                    calculate_result.result.set(f"{round(Number * 9 / 5 + 32, 2)} {to_value}")
                    return 
                elif from_value == "Fahrenheit" and to_value == "Celsius":
                    calculate_result.result.set(f"{round((Number - 32) * 5 / 9, 2)} {to_value}")
                    return
                else:
                    calculate_result.result.set("Conversion not supported!")
                
            elif theUnits.get() == "Memory units":
                conversion_factors = {
                    ("Terabytes", "Gigabytes"): 1024,
                    ("Gigabytes", "Terabytes"): 1 / 1024,
                    ("Gigabytes", "Megabytes"): 1024,
                    ("Megabytes", "Gigabytes"): 1 / 1024,
                    ("Terabytes", "Megabytes"): 1048576,
                    ("Megabytes", "Terabytes"): 1 / 1048576,
                }    
            elif theUnits.get() == "The Time":
                conversion_factors = {
                    ("Hour", "Minute"): 60,
                    ("Minute", "Hour"): 1 / 60,
                    ("Minute", "Second"): 60,
                    ("Second", "Minute"): 1 / 60,
                    ("Hour", "Second"): 3600,
                    ("Second", "Hour"): 1 / 3600,
                }  
            elif theUnits.get() == "The force":
                conversion_factors = {
                    ("Newton", "Kilogram-force"): 0.10197,
                    ("Kilogram-force", "Newton"): 9.80665,
                    ("Newton", "Pound"): 0.22481,
                    ("Pound", "Newton"): 4.44822,
                    ("Kilogram-force", "Pound"): 2.20462,
                    ("Pound", "Kilogram-force"): 0.45359,
                }
            else:
                conversion_factors = {}   
                
             # حساب الناتج باستخدام جدول التحويل
            factor = conversion_factors.get((from_value, to_value))
            if factor:
                result_value = round(Number * factor, 2)
                calculate_result.result.set(f"{result_value} {to_value}")
            else:
                calculate_result.result.set("Conversion not supported!")
        else:
            calculate_result.result.set("Select valid units!")
    except ValueError:
        calculate_result.result.set("Enter a valid number!")       

 