from posixpath import split
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')

lines_split=split(file_content)
print(len(lines_split))
