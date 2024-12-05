from tkinter import END

# دالة لتحديث الخيارات بناءً على العنصر المختار
def update_options(event, theUnits, theUniteFrom, theUniteTo, theNumber):
    selected_unit = theUnits.get()  # الحصول على الوحدة المختارة من أول ComboBox
    
    if selected_unit == "Lengths": # للتحويل بين الأطوال 
        options = ["Kilometers", "Meters", "centimeters"]
    elif selected_unit == "Weights": # للتحويل بين الأوزان
        options = ["Ton", "Kilograms", "Grams"]
    elif selected_unit == "Temperatures":  # للتحويل بين درجات الحرارة
        options = ["Celsius", "Fahrenheit"]
    elif selected_unit == "Memory units":  # للتحويل بين وحدات التخزين
        options = ["Terabytes", "Gigabytes", "Megabytes"]
    elif selected_unit == "The Time":  # للتحويل بين وحدات الزمن
        options = ["Hour", "Minute", "Second"] 
    elif selected_unit == "The force":  # للتحويل بين وحدات القوة
        options = ["Newton", "Pound", "Kilogram-force"]
    else:
        options = []
    
    # ComboBox (From و To) لتحديث خيارات
    theUniteFrom['values'] = options
    theUniteTo['values'] = options

    # لإعادة تعيين القيمة الافتراضية
    theUniteFrom.set("")
    theUniteTo.set("")
    
    # لحذف الرقم المدخل في خانة الرقم
    theNumber.delete(0, END)
    
   