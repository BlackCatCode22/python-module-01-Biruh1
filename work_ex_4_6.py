def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40.0) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

hours_input = input("Enter Hours: ")
rate_input = input("Enter Rate: ")

hours = float(hours_input)
rate = float(rate_input)

pay = computepay(hours, rate)

print("Pay:", pay)
