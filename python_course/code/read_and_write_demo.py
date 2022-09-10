file_name = "data.txt"

def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(',')
    courses = line[1].rstrip().split(',')
    return first_name, last_name, courses

def prep_to_write(first_name, last_name, courses):
    full_name = f"{first_name},{last_name}"
    courses = ','.join(courses)
    return f"{full_name}:{courses}"

with open(file_name,"r") as to_read:
    for line in to_read:
        print(line.strip())
        first_name, last_name, courses = prep_record(line)
        print(first_name, last_name, courses)

to_write = prep_to_write(first_name, last_name, courses)
print(to_write)
record_to_add = "john,schmoe:python,ruby,javascript"

# with open(file_name, "a+") as to_write:
#     to_write.write(f"{record_to_add}\n")
