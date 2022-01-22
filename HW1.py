# Create variables of different types
str_var = "Hello!"
int_var = 1
float_var = 1.0
bytes_var = b"Hello"
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
set_var = {1, 2, 3}
frozenset_var = frozenset(set_var)
dict_var = {'1': 1, '2': 2}
# Print all variables with types
print(str_var, type(str_var))
print(int_var, type(int_var))
print(float_var, type(float_var))
print(bytes_var, type(bytes_var))
print(list_var, type(list_var))
print(tuple_var, type(tuple_var))
print(set_var, type(set_var))
print(frozenset_var, type(frozenset_var))
print(dict_var, type(dict_var))
# Create two string variables, concatenate these variables and print the result
str_var_one = "Hello"
str_var_two = "World"
con_str_var = str_var_one + str_var_two
print(con_str_var)
# Print two string variables using comma
print(str_var, int_var)
# Print sting variable and int variable using plus
print(str_var + str(int_var))
