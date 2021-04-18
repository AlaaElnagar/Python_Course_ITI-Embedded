
"""
txt = "iti"

x = txt.isidentifier()

print(x)


txt = "123iti"

x = txt.isidentifier()

print(x)


"""

























txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="strict"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))







"""
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	        - ignores the characters that cannot be encoded
'namereplace'	        - replaces the character with a text explaining the character
'strict'	        - Default, raises an error on failure
'replace'	        - replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
"""
