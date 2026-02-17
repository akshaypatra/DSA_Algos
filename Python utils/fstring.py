
'''
f"" → formatted string literal

The f before the quotes means:

“Evaluate variables inside {} and insert their values into the string.”

- Example 1:

h = 9
m = 5
print(f"{h}:{m}")

- Output:
9:5

----------------------------------------------------------------------------
- Example 2 :

f"{h}:{m:02d}"

This is format specification:

Breakdown:

m → variable

: → start formatting

0 → pad with zeros

2 → total width = 2 characters

d → decimal integer

Meaning:

👉 Display m as a 2-digit decimal number, padding with leading zeros if needed.

-------------------------------------------------------------------------------
'''