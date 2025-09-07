hours_input = input("Enter Hours: ")
rate_input = input("Enter Rate: ")

try:
    hours = float(hours_input)
    rate = float(rate_input)
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40.0) * (rate * 1.5)
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours * rate

print("Pay:", total_pay)
