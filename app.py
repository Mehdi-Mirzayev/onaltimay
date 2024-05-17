with open("input.txt", "w") as file:
    file.write("veteni qorumaq her bir kesin vezife borcudur.")


with open("input.txt", "r") as file:
    first_line = file.readline().upper()


with open("output.txt", "w") as file:
    file.write(first_line)
