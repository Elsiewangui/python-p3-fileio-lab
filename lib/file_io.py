def write_file(file_name, file_content):
         file_name = f"{file_name}.txt"
         with open(file_name, 'w') as file:
            file.write(file_content)


def append_file(file_name, file_content):
         file_name = f"{file_name}.txt"
         with open(file_name, 'a') as file:
            file.write(file_content)

def read_file(file_name):
         file_name = f"{file_name}.txt"
         with open(file_name, 'r') as file:
            return file.read()



write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n")
append_file(file_name="logfile", file_content="Log 2: 3 bananas subtracted\n")
content = read_file(file_name="logfile")
print(content)
