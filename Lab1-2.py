score = float(input("รับค่าคะแนน: "))

if score >= 80 and score <= 100:
    print("Grade A")
elif score >= 70 and score <= 80:
    print("Grade B")
elif score >= 60 and score <= 70:
    print("Grade C")
elif score >= 50 and score <= 60:
    print("Grade D")
elif score < 50 and score >= 0:
    print("Grade F")
    print("YOU FAILED")
    print("พ่อแม่ไม่มีเงินแก้ศูนย์แล้วลูก 500 บาท")
else:
    print("Error: กรุณากรอกข้อมูลใหม่คุณ Autistic (Range 0-100) ")
    
print("ขอแสดงความยินดีด้วย?")