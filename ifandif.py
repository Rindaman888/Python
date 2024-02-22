age=int(input("อายุของคุณ : "))
sex=str(input("ชาย/หญิง : "))

if sex =="ชาย":
    if age >= 15:
        print("คำนำหน้าเป็น นาย")
    else:
        print("คำนำหน้าเป็น เด็กชาย")
elif sex == "หญิง":
    if age >= 15:
        print("คำนำหน้าเป็น นางสาว")
    else:
        print("คำนำหน้าเป็น เด็กหญิง")
else:
    print("---กรุณาใส่ช้อมูลให้ถูกต้อง---")