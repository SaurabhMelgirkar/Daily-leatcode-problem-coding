# Initialize an empty set
elements_set = set()

# Loop to accept 'h' elements
h = int(input("Enter the number of elements (h): "))
print(f"Please enter {h} elements from 0-9, a-z, or A-Z:")

for _ in range(h):
    element = input().strip()
    # Check if the element is valid (alphanumeric)
    if element.isalnum() and len(element) == 1:
        elements_set.add(element)
    else:
        print("Invalid input. Please enter a single character from 0-9, a-z, or A-Z.")

# Display the set elements and its length
print("Set elements:", elements_set)
print("Length of the set:", len(elements_set))
# d=sum(1 for char in elements_set if char.isdigit())
def find_first_digit(elements_set):
    for i in elements_set:
        if i.isdigit():
            return i  
    return None 
print(find_first_digit(elements_set))