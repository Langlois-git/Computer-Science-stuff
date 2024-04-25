# ----------------------------------------
# Name:  	David Langlois
# Program:	L1Q1dl.py
# ----------------------------------------
# Purpose: To learn some programming tips
# ----------------------------------------

print("\nHere are some programming tips:")

# Print a blank line
print()
print('1) Print a blank line with: print()')
print('   or use the newline \\n (backslash n) symbol\n')

# Use commas to seperate data in a print statement
print('2) Seperate data', 'in a', 'print statement', 'with commas.')
print('   Each comma seperator','will add','one space','to the output.\n')

# Use sep to change the default seperator action in a print statement
print('3) Change the', 'default', 'seperator', 'action using sep', sep = '---')
print()

# Use end to change the default terminal action in a print statement 
print('4) Combine print statement outputs', end = " ")
print('(on the same line) ', end = "")
print('with end\n')

# Concatenate text strings using +
print('5) Concatenate' + 'strings' + 'using' + '+' + 'to' + 'prevent' + 'spaces\n')

# Tab using \t
print('6) Tab', '\t', 'the text', '\twith the \\t (backslash t) symbol\n')

#Store information in variables
print("7) Use a variable to store information:")
print('\tSet variable x equal to (4 + 2)')
x = 4 + 2
print("\tx + (3 * 4) =", x + (3 * 4))
