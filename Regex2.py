import re

def extract_phone_number(input):
    pattern = r'(\\91+[-\s]?\d{10} |\d{10})'
    match = re.findall(pattern, input)
    return match

input = "Call me at 1234567890 or +91-0987654321."
result = extract_phone_number(input)

print("Original String:" ,input)
print("Extracted Phone Numbers:",result)