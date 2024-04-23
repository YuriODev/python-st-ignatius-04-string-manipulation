# **Problem:** Print a part of the multiplication table for numbers in the range [a, b] across [c, d].

# ### Input:
# - Four integers a, b, c, and d defining the ranges.

# ### Output:
# - A formatted multiplication table.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 1<br>4<br>2<br>5 | Output 1         |

# ### Output for Input Example 1

# <pre>	2	3	4	5
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20</pre>

# Prompt the user to enter four integers separated by a space.
print("Enter four integers: a, b, c, and d")

a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
c = int(input("Enter 'c': "))
d = int(input("Enter 'd': "))

# Print the multiplication table.
print("\t", end="")
for i in range(c, d + 1):
    print(i, end="\t")
print()

for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()