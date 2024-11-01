data = []
import matplotlib.pyplot as plt
import numpy as np
import re
import pyautogui
import time
# รับข้อมูลจากผู้ใช้
for i in range(2000):
    ii = input("กรอกข้อมูล (หรือ 'x' เพื่อหยุด): ")
    if ii.lower() == "x":
        break
    data.append(ii)

import re

pp = []
for i in data:
    # แยกตัวเลขออกจากสตริง
    extracted_numbers = re.findall(r'\d+\.?\d*', i)
    
    # เปลี่ยนตัวเลขที่แยกได้จากสตริงเป็น float และตรวจสอบว่ามากกว่า 59 หรือไม่
    for number in extracted_numbers:
        if float(number) > 59:
            pp.append(i)
            break  # ถ้าเจอตัวเลขที่มากกว่า 59 ให้หยุดแล้วไปเช็คสตริงถัดไป

# แสดงผลลัพธ์ที่มีตัวเลขมากกว่า 59
pp.reverse()
# for i in pp:
#     print(i)

g = pp
oo = []
for data in g:
    valid_numbers = re.findall(r'\d+\.\d+', data)
    for num in valid_numbers:
        number = round(float(num), 2)
        if number not in [0.87, 0.85, 0.88, 0.89]:
            oo.append(number)

first_value = oo[0]
last_value = oo[-1]
oooo = int(first_value - last_value)
std_deviation = np.std(oo)

p = 285
ev = (0.65 * (p*0.87)) - (0.35*p)
eo = ev * 3

plt.ion()

# ตรวจสอบค่าของ std_deviation
if 2.5 < std_deviation < 4.8:
    ii = "T" if abs(oooo) >= 3 else "F"
    plt.plot(oo, marker='o')
    plt.title(f"1 {std_deviation}")
    plt.xlabel('Index')
    plt.ylabel('Value')
elif 2.2 < std_deviation < 4.8:
    ii = "T" if abs(oooo) >= 3 else "F"
    plt.plot(oo, marker='o')
    plt.title(f"22 {std_deviation}")
    plt.xlabel('Index')
    plt.ylabel('Value')
else:
    ii = "T" if abs(oooo) >= 5 else "F"
    plt.plot(oo, marker='o')
    plt.title(f"0 {std_deviation}")
    plt.xlabel('Index')
    plt.ylabel('Value')

plt.draw()
plt.pause(2)  # รอ 5 วินาที
plt.close()

print("\nqm -bth- // tren // <15หลอกเเดกq3 ")
print(" 1 pba wnba korea BasiccOrder AllInFirstBill \n")
print(" 1 pba Compound InterestORder\n")


# ข้อมูลคะแนน Full Time และเปอร์เซ็นต์เฉลี่ยของ Q3
predicted_full_time = last_value  # คะแนน Full Time ที่คาดการณ์
q2_percent = 0.26  # สมมติว่า Q3 คิดเป็น 25% ของคะแนน Full Time
q3_percent = 0.26  # สมมติว่า Q3 คิดเป็น 25% ของคะแนน Full Time

# คำนวณคะแนนที่คาดการณ์สำหรับ Q3
predicted_q3 = predicted_full_time * q3_percent
predicted_q3h = predicted_full_time * q3_percent+3
predicted_q3l = predicted_full_time * q3_percent-3
print(f'คาดการณ์คะแนน Q1/3 1 : {predicted_q3l}-{predicted_q3}-{predicted_q3h}')

# คำนวณความชันของข้อมูลใน oo
slopes = []
for i in range(1, len(oo)):
    slope = (oo[i] - oo[i-1]) / (i - (i-1))  # (y2 - y1) / (x2 - x1)
    slopes.append(slope)

# ค่าความชันเฉลี่ยรวมของกราฟ
average_slope = sum(slopes) / len(slopes) 

print(f"ค่าความชันรวมของกราฟคือ: {average_slope}")
import numpy as np
import matplotlib.pyplot as plt

# ข้อมูล oo ที่มีอยู่แล้ว

# กำหนดช่วงเวลาสำหรับค่าเฉลี่ยเคลื่อนที่ (Moving Average)
window = 20  # สามารถเปลี่ยนได้ตามต้องการ

# คำนวณค่าเฉลี่ยเคลื่อนที่ (Moving Average)
moving_average = np.convolve(oo, np.ones(window)/window, mode='valid')

# คำนวณค่าเบี่ยงเบนมาตรฐาน (Standard Deviation)
rolling_std = []
for i in range(len(oo) - window + 1):
    rolling_std.append(np.std(oo[i:i+window]))

# คำนวณ Bollinger Bands
upper_band = moving_average + (np.array(rolling_std) * 2 )
lower_band = moving_average - (np.array(rolling_std) * 2  )

# สร้างกราฟ Bollinger Bands
plt.figure(figsize=(5,3))
plt.plot(oo, label='Data', color='blue')
plt.plot(range(window-1, len(oo)), moving_average, label='M', color='orange')
plt.plot(range(window-1, len(oo)), upper_band, label='U', color='green')
plt.plot(range(window-1, len(oo)), lower_band, label='L', color='red')
plt.fill_between(range(window-1, len(oo)), lower_band, upper_band, color='lightgray', alpha=0.1)

plt.title('Bollinger Bands')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

# แสดงกราฟแบบไม่ปิดทันที
plt.show()
plt.pause(5)  # กำหนดให้แสดงผล 30 วินาที
plt.close()    # ปิดกราฟหลังจากผ่านไป 30 วินาที
 # กำหนดให้แสดงผลตลอด จนกว่าผู้ใช้จะปิดหน้าต่างกราฟ

