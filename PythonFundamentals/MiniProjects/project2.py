cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
days_with_918 = 918 / cost_per_day

print("Cost to operate one server per day: $", cost_per_day)
print("Cost to operate one server per week: $", cost_per_week)
print("Cost to operate one server per month: $", cost_per_month)
print("Days one server can operate with $918:", days_with_918)