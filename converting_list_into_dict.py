def read_lines():
 with open('students.txt') as f:
      new_names = f.read()
      list_of_words = new_names.split()
 new_dict = dict()
 for key in list_of_words:
     new_dict[key] = ''

 print (new_dict)

read_lines()
