author = "..."

first_name = str()
last_name = str()
domain = str()
split_name = author.split(" ")
for n in range(len(split_name) - 1):
    first_name += str(split_name[n])
last_name = str(split_name[-1])
print(first_name)
print(last_name)
try:
    first_initial = first_name[0]
except IndexError:
    first_initial = ""
try:
    last_initial = last_name[0]
except IndexError:
    last_initial = ""


print(first_initial)
print(last_initial)
