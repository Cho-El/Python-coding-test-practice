my_string = 'Hello, what are doing?'
index = my_string.find('doing')
final_string = my_string[:index] + 'you ' + my_string[index:]
print(final_string)

my_string = 'Hello, what are doing'

split_strings = my_string.split()
split_strings.insert(3, 'you')
final_string = ' '.join(split_strings)
print(final_string)