import decisions

options = float(input('Options?'))

total = float(input('Total?'))

result = decisions.get_options_ratio(options, total)

result = decisions.get_faculty_rating(result)

print(result)
