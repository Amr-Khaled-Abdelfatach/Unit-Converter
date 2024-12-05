from tkinter import *
from tkinter import ttk

from The_Unites import update_options
from Arithmetic_operations import calculate_result 
 
# إنشاء نافذة التطبيق
theFrame = Tk()
theFrame.title("Unit Converter")
theFrame.geometry("550x600")
theFrame.configure(bg="#3498db")

# حول الوحدات                        العنوان   
theLabel = Label(theFrame, text="✨Unit Converter✨", font="Tahoma 25", fg="#c0392b", bg="#3498db")
theLabel.pack( anchor="center")

# اختيار الوحدة
unit_label = Label(theFrame, text="Units :-", font=("Arial", 13), bg="#3498db").pack(pady=5)

# قائمة اختيار نوع الوحدة
theUnits = ttk.Combobox(theFrame, values=["Lengths", "Weights", "Temperatures", "Memory units","The Time","The force"], font=("Arial", 15))
theUnits.pack()

# ادخال الرقم
unit_label = Label(theFrame, text="The Number :-", font=("Arial", 13), bg="#3498db").pack(pady=5)

# حقل إدخال الرقم
theNumber = Entry(theFrame, width=20)
theNumber.pack()

# الوحدة المراد التحويل منها
unit_label = Label(theFrame, text="From :~", font=("Arial", 13), bg="#3498db").pack(pady=5)


theUniteFrom = ttk.Combobox(theFrame, font=("Arial", 12))
theUniteFrom.pack()

# الوحدة المراد التحويل ليها
unit_label = Label(theFrame, text="To :~", font=("Arial", 12), bg="#3498db").pack(pady=5)

theUniteTo = ttk.Combobox(theFrame, font=("Arial", 12))
theUniteTo.pack()

theUnits.bind("<<ComboboxSelected>>", lambda event: update_options(event, theUnits, theUniteFrom, theUniteTo, theNumber))  # ربط تغيير الاختيار بالدالة

# زر للحصول على النتيجة
theButton = Button(theFrame, text="Get Answer", font=("Arial", 14 ), bg="#2980b9", fg="#ffffff",
                   command= lambda: calculate_result(theUnits, theNumber, theUniteFrom, theUniteTo) )
theButton.pack(pady=20)

# خانة لعرض الناتج
result = StringVar()
theResult = Entry(theFrame, textvariable=result, state="readonly",width=25, font="Tahoma 23").pack(pady=5)

calculate_result.result = result
# تشغيل التطبيق
theFrame.mainloop()

