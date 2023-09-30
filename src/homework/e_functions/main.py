import value_return

total_seconds = int(input("Enter total seconds:"))
hours = value_return.get_hour(total_seconds)
minutes = value_return.get_minutes(total_seconds)
seconds = value_return.get_seconds(total_seconds)

print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))



