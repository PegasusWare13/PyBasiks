#tuples are immutable so data can neither be added not be removed
#so we use a workaround by temporarily converting the tuple into a list
tuple1 = "Kakarot", "Whis", "Beerus", "Champa","Vegeta","Broly","Jiren"
temp_list = list(tuple1)
temp_list.append("Hit")
temp_list.remove("Champa")
tuple1 = tuple(temp_list)
print(tuple1)
print(type(tuple1), type(temp_list))
