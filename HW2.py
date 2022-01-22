import math
# Create integer variable item_1
item_1 = 3
# Create integer variable item_2
item_2 = 4
# Summarize two variables
result_sum = item_1 + item_2
# Print the result
print(result_sum)
# Subtract variables and print the result
result_subtr = item_2 - item_2
print(result_subtr)
# Multiply variables and print the result
result_multi = item_1 * item_2
print(result_multi)
# Exponentiate item_1 to item_2 and print the result
result_exp = item_1 ** item_2
print(result_exp)
# Exponentiate item_1 to item_2 used math library and print the result
result_m_exp = math.pow(item_1, item_2)
print(result_m_exp)
# Extract square root and print the result
result_s_root = item_2 ** 0.5
print(result_s_root)
# Extract square root using math and print the result
result_m_s_root = math.sqrt(item_2)
print(result_m_s_root)
# Extract square root using math.pow and print the result
result_mp_s_root = math.pow(item_2, 0.5)
print(result_mp_s_root)
# Divide item_1 to item_2 and print the result
result_division = item_1 / item_2
print(result_division)
# Floor result division and print the result
result_m_floor = math.floor(result_division)
print(result_m_floor)
# Ceil result division and print the result
result_m_ceil = math.ceil(result_division)
print(result_m_ceil)
# Floor variable using explicit cast and print the result
result_int = int(result_division)
print(result_int)
# Divide item_1 to item_2 without division loss and print the result
result_no_division_loss = int(item_1 / item_2)
print(result_no_division_loss)
# Find division loss and print the result
result_division_loss = result_division - result_no_division_loss
print(result_division_loss)
# Create integer variable item_3
item_3 = 10
# Arithmetic operation with cast
item_3 += 10
print(item_3)
item_3 -= 5
print(item_3)
item_3 *= 3
print(item_3)
item_3 /= 2
print(item_3)
item_3 **= 2
print(item_3)
item_3 **= 0.5
print(item_3)
item_3 %= 3
print(item_3)
# Boolean operations
# Create boolean variables
b_item_t = True
b_item_f = False
# Summarize two variables and print the result
b_item_result_sum = b_item_t + b_item_f
print(b_item_result_sum)
# Subtract two variables and print the result
b_item_result_subtr = b_item_t - b_item_f
print(b_item_result_subtr)
# Multiply two variables and print the result
b_item_result_multi = b_item_t * b_item_f
print(b_item_result_multi)
# Divide two variables and print the result
b_item_result_division = b_item_t / b_item_f    # Error
print(b_item_result_division)
# Explicit cast boolean to integer and print the result
b_item_1_int = int(b_item_t)
print(b_item_1_int)
b_item_2_int = int(b_item_f)
print(b_item_2_int)
