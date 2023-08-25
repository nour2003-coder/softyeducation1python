def rotate_tuple(input_tuple, n):
    length = len(input_tuple)
    n = n % length  # Handle cases where n is larger than tuple length
    new_tuple = input_tuple[-n:] + input_tuple[:-n]
    return new_tuple

# Taking input from the user
input_list = []
while True:
    print("Press -1 to exit")
    a = int(input("Give me an element: "))
    if a == -1:
        break
    else:
        input_list.append(a)

input_tuple = tuple(input_list)  # Convert list to tuple
print("Original tuple:", input_tuple)

while True:
    n = int(input("Enter a positive integer: "))
    if n > 0 and n < len(input_tuple):
        break

new_rotated_tuple = rotate_tuple(input_tuple, n)
print("Rotated tuple:", new_rotated_tuple)
