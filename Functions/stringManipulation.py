# 1. Case Conversion

# str.upper(): Converts all characters in a string to uppercase.
# str.lower(): Converts all characters in a string to lowercase.
# str.capitalize(): Capitalizes the first character of the string and converts the rest to lowercase.
# str.title(): Capitalizes the first character of each word in the string.
# str.swapcase(): Swaps the case of all characters in the string.

# 2. String Formatting

# str.format(*args, **kwargs): Formats the string using placeholders.
# str.zfill(width): Pads the string with zeros on the left to fill the specified width.
# str.center(width[, fillchar]): Centers the string within the specified width, optionally filling with a specified character.
# str.ljust(width[, fillchar]): Left-justifies the string within the specified width.
# str.rjust(width[, fillchar]): Right-justifies the string within the specified width.

# 3. String Searching

# str.find(sub[, start[, end]]): Returns the lowest index where the substring is found, or -1 if not found.
# str.rfind(sub[, start[, end]]): Returns the highest index where the substring is found, or -1 if not found.
# str.index(sub[, start[, end]]): Like find(), but raises ValueError if the substring is not found.
# str.rindex(sub[, start[, end]]): Like rfind(), but raises ValueError if the substring is not found.
# str.count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of the substring.

# 4. String Checking

# str.startswith(prefix[, start[, end]]): Returns True if the string starts with the specified prefix.
# str.endswith(suffix[, start[, end]]): Returns True if the string ends with the specified suffix.
# str.isalnum(): Returns True if all characters in the string are alphanumeric.
# str.isalpha(): Returns True if all characters in the string are alphabetic.
# str.isdigit(): Returns True if all characters in the string are digits.
# str.isnumeric(): Returns True if all characters in the string are numeric (includes digits and fractions).
# str.isdecimal(): Returns True if all characters in the string are decimal characters.
# str.islower(): Returns True if all characters in the string are lowercase.
# str.isupper(): Returns True if all characters in the string are uppercase.
# str.isspace(): Returns True if all characters in the string are whitespace.
# str.istitle(): Returns True if the string is in title case (capitalized words).


# 5. String Modification

# str.strip([chars]): Removes leading and trailing characters (whitespace by default).
# str.lstrip([chars]): Removes leading characters (whitespace by default).
# str.rstrip([chars]): Removes trailing characters (whitespace by default).
# str.replace(old, new[, count]): Replaces occurrences of a substring with another substring.
# str.join(iterable): Joins elements of an iterable with the string as a separator.
# str.split(sep=None, maxsplit=-1): Splits the string into a list of substrings based on a separator.
# str.rsplit(sep=None, maxsplit=-1): Splits the string from the right.
# str.splitlines([keepends]): Splits the string at line boundaries.
# str.partition(sep): Splits the string at the first occurrence of the separator.
# str.rpartition(sep): Splits the string at the last occurrence of the separator.
# str.expandtabs(tabsize=8): Replaces tabs in the string with spaces.

# 6. String Encoding/Decoding

# str.encode(encoding='utf-8', errors='strict'): Encodes the string using the specified encoding.