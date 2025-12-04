salary = float(input("กรอกเงินเดือนเดิม: "))
years = float(input("กรอกอายุงาน (ปี): "))

if years < 1:
    rate = 0
elif years < 3:
    rate = 0.03
elif years < 5:
    rate = 0.05
else:
    rate = 0.07

increase = salary * rate
new_salary = salary + increase

print("เงินเดือนใหม่ =", new_salary)
