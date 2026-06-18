print("my work1")
width = float(input("ใส่ความกว้าง: "))
length = float(input("ใส่ความยาว: "))

if width > 0 and length > 0:
    พื้นที่ = width* length
    เส้นรอบรูป = (width+length) * 2
    print(f"พื้นที่คือ: {พื้นที่}")
    print(f"เส้นรอบรูปคือ: {เส้นรอบรูป}")
else:
    print("ข้อผิดพลาด: ความกว้างและความยาวต้องมากกว่า 0")