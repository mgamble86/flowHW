input = open("input.txt")

output = open("trim.txt", "w")

for i in input:

    trim = i[14:]

    length = len(trim) - 1

    output.write(trim)

    print("length is " + str(length))
