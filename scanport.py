import socket
import threading

def scan_port(target_ip, port):
    try:
        # สร้าง Socket Object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ตั้งค่า Timeout เพื่อหลุดจากการเชื่อมต่อที่ไม่สำเร็จ
        sock.settimeout(1)
        # พยายามเชื่อมต่อ
        sock.connect((target_ip, port))
        print(f"Port {port} is open")
    except socket.error:
        # ถ้าเกิดข้อผิดพลาดในการเชื่อมต่อ
        pass
    finally:
        # ปิดการเชื่อมต่อ
        sock.close()

def port_scan(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip}...")
    for port in range(start_port, end_port + 1):
        # สร้าง thread เพื่อสแกนหลายพอร์ตพร้อมกัน
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()

if __name__ == "__main__":
    # กำหนด target IP และช่วงพอร์ตที่ต้องการสแกน
    target_ip =  input('target_ip :')
    start_port = 1
    end_port = 1024
    
    # เรียกใช้งานฟังก์ชันสแกนพอร์ต
    port_scan(target_ip, start_port, end_port)
