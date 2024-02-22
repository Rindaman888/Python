
def check_password_strength(password):
    # ตรวจสอบความยาวของรหัสผ่าน
    if len(password) < 8:
        return False, "รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร"
    
    # ตรวจสอบว่ามีตัวเลขหรือไม่
    if not any(char.isdigit() for char in password):
        return False, "รหัสผ่านต้องมีตัวเลขอย่างน้อย 1 ตัว"
    
    # ตรวจสอบว่ามีตัวอักษรตัวใหญ่หรือไม่
    if not any(char.isupper() for char in password):
        return False, "รหัสผ่านต้องมีตัวอักษรตัวใหญ่อย่างน้อย 1 ตัว"
    
    # ตรวจสอบว่ามีตัวอักษรพิเศษหรือไม่
    special_chars = "!@#$%^&*()-+"
    if not any(char in special_chars for char in password):
        return False, "รหัสผ่านต้องมีอักขระพิเศษอย่างน้อย 1 ตัว"
    
    return True, "รหัสผ่านมีความปลอดภัย"

# ทดสอบการใช้งาน
password = input("กรุณาป้อนรหัสผ่าน: ")
is_secure, message = check_password_strength(password)
if is_secure:
    print("รหัสผ่านมีความปลอดภัย")
else:
    print("รหัสผ่านไม่ปลอดภัย:", message)
