people_in_line = input("People in line: ")
num_inside = int(input("Number of people inside: "))

max_capacity = 8

people_list = people_in_line.split(", ")

available_seats = max_capacity - num_inside

if available_seats > 0:
  can_enter = people_list[:available_seats]
  print(f"These people can enter: {', '.join(can_enter)}")
else:
  print("No more room!")
