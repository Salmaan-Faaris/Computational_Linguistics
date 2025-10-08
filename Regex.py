import re
 
 
def exrtact_digit(input):
    pattern = r'\d+'
    match = re.findall(pattern, input)
    return match

input = "abcd1234efgh576"
result = exrtact_digit(input)

print("Original String:", input)
print("Extracted Digits:", result)  