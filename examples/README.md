# Examples 👨🏼‍💻

Here are some examples to get you started.

<details open>
<summary><b>Covered topics</b></summary>

| Topic Covered                                           | Code with explanations                            |
| ------------------------------------------------------- | ------------------------------------------------- |
| Repeat Last Two Characters                              | [Detailed code](./example_1.py)                   |
| Reverse Digits                                          | [Detailed code](./example_2.py)                   |
| Check Start of String                                   | [Detailed code](./example_3.py)                   |
| Number reversal                                         | [Detailed code](./example_4.py)                   |
| Palindrome String                                       | [Detailed code](./example_5.py)                   |
| Is Digit Check                                          | [Detailed code](./example_6.py)                   |
| Digits and Characters                                   | [Detailed code](./example_7.py)                   |
| The first word in a string                              | [Detailed code](./example_8.py)                   |
| Access Code Calculation                                 | [Detailed code](./example_9.py)                   |
| ASCII Characters                                        | [Detailed code](./example_10.py)                  |
| Count Words in a String                                 | [Detailed code](./example_11.py)                  |
| String Len                                              | [Detailed code](./example_12.py)                  |
| Digits and Characters Count                             | [Detailed code](./example_13.py)                  |
| Vowel and Consonant Check                               | [Detailed code](./example_14.py)                  |
| Sum of Sequence Elements Calculation                    | [Detailed code](./example_15.py)                  |
| Uppercase, Lowercase, and Space Count                   | [Detailed code](./example_16.py)                  |
| Remove Duplicate Characters                             | [Detailed code](./example_17.py)                  |
| Find and Replace Substring                              | [Detailed code](./example_18.py)                  |

| Power Calculation                            | [Detailed code](./example_19.py)    |
| Quiz Winner Determination                    | [Detailed code](./example_20.py)    |
| Average Speed Calculation                    | [Detailed code](./example_21.py)    |
| Automorphic Number Determination             | [Detailed code](./example_22.py)    |
| Least Common Multiple Calculation            | [Detailed code](./example_23.py)    |
| Monotonous Sequence Printing                 | [Detailed code](./example_24.py)    |
| Fibonacci Number Determination               | [Detailed code](./example_25.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_26.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_27.py)    |
| Fibonacci Number Determination               | [Detailed code](./example_28.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_29.py)    |
| Sequence Element Comparison                  | [Detailed code](./example_30.py)    |

</details>

### Example 1: Repeat Last Two Characters

**Problem:** Write a program that displays a string of 5 copies of the last two characters of a user-entered string (the length of the entered string must be at least 2).

| No. | Inputs | Outputs         |
| --- | ------ | --------------- |
| 1   | emu    | mumumumumu      |
| 2   | lion   | ononononon      |
| 3   | tiger  | ererererer      |
| 4  | snake  | kekekekeke      |


 - Repeat Last Two Characters

**Problem:** Print 5 copies of the last two characters from a user-entered string on the screen (where the length of the entered string is at least 2).

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

if len(input_string) >= 2:
    last_two = input_string[-2:]
    print(last_two * 5)
```
</details>

### Example 2: Reverse Digits

**Problem:** Given a natural number, find the number obtained by reading its digits from right to left.

| No. | Inputs   | Outputs   |
| --- | -------- | --------- |
| 1   | 98       | 89        |
| 2   | 10010010 | 01001001  |
| 3   | 1235     | 5321      |
| 4   | 1        | 1         |
| 5   | 0        | 0         |

**Problem:** Compute the number obtained by reversing the digits of a given natural number.

<details open>
<summary><b>Python Solution</b></summary>

```python
input_number = input("Enter a natural number: ")

reversed_number = input_number[::-1]

print(reversed_number)
```
</details>

### Example 3: Check Start of String

**Problem:** The user enters a string and a set of characters. Write a program that checks if the string starts with the given characters.

| No. | Inputs                      | Outputs |
| --- | --------------------------- | ------- |
| 1   | wireless router<br> route     | False   |
| 2   | python programming<br> py     | True    |
| 3   | 12345<br> 123                 | True    |
| 4   | 12345<br> 234                 | False   |
| 5   | 12345<br> 12345               | True    |

**Problem:** Verify whether a user-input string begins with the specified characters.

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter the string: ")
prefix = input("Enter the prefix: ")

starts_with_prefix = input_string.startswith(prefix)

print(starts_with_prefix)
```
</details>



## Example 4:  Number reversal

**Problem:** Given a natural number `n`. Find a number obtained by permuting its first and last digits. Consider the case of entering a single-digit number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1467   | 7461    |
| 2   | 5      | 5       |
| 3   | 11     | 11      |
| 4   | 12     | 21      |
| 5  | 1      | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = input("Enter the number: ")

if len(n) > 2:
    reversed_number = n[-1] + n[1:-1] + n[0]
elif len(2) == 2:
    reversed_number = n[-1] + n[0]
else:
    reversed_number = n

print(reversed_number)
```
</details>



## Example 5: Palindrome String

**Problem:** A user enters a string which can contain digits and other characters. Determine if the line is a palindrome, i.e., it reads the same from left to right and from right to left. Do not consider the case of letters. Examples of palindrome strings: racecar, 10201, Ada, Never odd or even.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Ada    | True    |
| 2   | Able was I ere I saw Elba | True    |
| 3   | 10501  | True    |
| 4   | Origin | False   |
| 5   | 12321  | True    |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

input_string = input_string.replace(" ", "").lower()

is_palindrome = input_string == input_string[::-1]

print(is_palindrome)
```
</details>


## Example 6: Is Digit Check


**Problem:**  For the entered symbol, check if it is a digit. You cannot use string functions to solve the problem. The program should print the word Yes if the character is a digit, or the word No.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 7      | Yes     |
| 2   | A      | No      |
| 3   | 0      | Yes     |
| 4   | 9      | Yes     |
| 5   | h      | No      |


<details open>
<summary><b>Python Solution</b></summary>

```python
# Solution 1

symbol = input("Enter a symbol: ")


if "0" <= symbol <= "9":
    print("Yes")
else:
    print("No")

# Solution 2

digits = "0123456789"

if symbol in digits:
    print("Yes")
else:
    print("No")
```
</details>



## Example 7: Digits and Characters

**Problem:** A user enters a string in which digits and other characters alternate. The string does not contain digits at the beginning and end. Write a program that prints all the characters of the entered string in the same order, but without digits.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | H1e2l3l4o5w6o7r8l9d | Helloworld |
| 2   | i1m3p4o9r0t4 6t7h8i9s | import this |
| 3   | 1H2e3l4l5o6 7W8o9r0l1d | Hello World |
| 4   | 1a2b3c4d5e6f7g8h9i0j | abcdefghij |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

result = ""

for char in input_string:
    if not char.isdigit():
        result += char

print(result)
```
</details>

## Example 8: The first word in a string

**Problem:** Write a program that outputs the first word in a string. A word is a sequence of non-space characters bounded by spaces or the ends of a string. The input string contains an arbitrary sequence of characters. The program should print the first word of this string. Need to consider the case when the string has just one word

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Stranger Things | Stranger |
| 2   | The Mandalorian | The |
| 3   | The Witcher | The |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

first_space_index = input_string.find(" ")

if first_space_index != -1:
    first_word = input_string[:first_space_index]
else:
    first_word = input_string

print(first_word)
```
</details>


## Example 9: Access Code Calculation

**Problem:** To access their account on a social network site, a user entered their login and password. Since two-factor authentication was enabled, they received a message with a string of numbers and information on how to get the access code. The message read: "Each digit greater than 5 must be divided by 2 and then all even numbers must be removed from the resulting sequence of digits." What code should the user enter for successful authorization? Write a program that takes a string of numbers from the message as input and prints the correct access code.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5763   | 33      |
| 2   | 1977   | 33      |
| 3   | 12345  | 1       |
| 4   | 987654 | 33      |
| 5   | 123456 | 1       |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

result = ""

for char in input_string:
    if char.isdigit() and int(char) > 5:
        result += str(int(char) // 2)
    elif char.isdigit() and int(char) % 2 != 0:
        result += char

print(result)
```
</details>


## Example 10:  ASCII Characters

**Problem:** Print all ASCII characters with codes from `n` (n > 32) to `m` (m < 127) and their codes in the following format: "character code".

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 101<br>106 | e 101<br>f 102<br>g 103<br>h 104<br>i 105<br>j 106 |
| 2   | 65<br>70   | A 65<br>B 66<br>C 67<br>D 68<br>E 69<br>F 70 |
| 3   | 33<br>40   | ! 33<br>" 34<br># 35<br>$ 36<br>% 37<br>& 38<br>' 39 |


<details open>
<summary><b>Python Solution</b></summary>

```python
start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

for i in range(start, end + 1):
    print(chr(i), i)
```
</details>


## Example 11: Count Words in a String


**Problem:** Given a string of words separated by spaces. Determine the number of words in the string.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Events happened very rapidly with Francis Morgan that late spring morning | 11 |
| 2   | The quick brown fox jumps over the lazy dog | 9 |
| 3   | The cat in the hat | 5 |
| 4   | The quick brown fox jumps over the lazy dog | 9 |
| 5   | The cat in the hat | 5 |


<details open>
<summary><b>Python Solution</b></summary>
    
```python
input_string = input("Enter a string: ")

if len(input_string) == 0:
    print(0)
else:
    word_count = 1
    for char in input_string:
        if char == " ":
            word_count += 1

    print(word_count)
```
</details>


## Example 12: String Len

**Problem:** Write a program to calculate the length of a string without using the `len()` function. 

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | pythonguide.pp.ua | 17 |
| 2   | python | 6 |
| 3   | guide | 5 |
| 4   | pp.ua | 5 |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

length = 0

for _ in input_string:
    length += 1

print(length)
```
</details>


## Example 13: Digits and Characters Count

**Problem:** Write a program that receives a string and calculates the number of digits and letters in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Andromeda, M 31, NGC 224 | Letters 13<br>Digits 5 |
| 2   | Python 3.9 | Letters 6<br>Digits 2 |
| 3   | 12345 | Letters 0<br>Digits 5 |
| 4   | 1a2b3c4d5e | Letters 5<br>Digits 5 |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

letter_count = 0
digit_count = 0

for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Letters {letter_count}")
print(f"Digits {digit_count}")
```
</details>


## Example 14: Vowel and Consonant Check

**Problem:** Write a program to check if the entered letter is a vowel or a consonant.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | F      | F is a consonant |
| 2   | e      | e is a vowel |
| 3   | a      | a is a vowel |
| 4   | b      | b is a consonant |
| 5   | c      | c is a consonant |


<details open>
<summary><b>Python Solution</b></summary>

```python
letter = input("Enter a letter: ")

if letter.lower() in "aeiou":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
```
</details>

## Example 15: Sum of Sequence Elements Calculation

**Problem:** User defines a number `n` such as `n >= 2`. Calculate the sum of the following sequence: `1 x 2 + 2 x 3 + ... + (n - 1) x n`. Print the result in the format shown in the output data.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2      | 1*2=2   |
| 2   | 4      | 1*2+2*3+3*4=20 |
| 3   | 5      | 1*2+2*3+3*4+4*5=35 |
| 4   | 6      | 1*2+2*3+3*4+4*5+5*6=56 |
| 5   | 7      | 1*2+2*3+3*4+4*5+5*6+6*7=84 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

total = 0
output = ""

if n >= 2:
    for i in range(1, n):
        total += i * (i + 1)
        output += f"{i}*{i + 1}+"

    output = output[:-1]
    output += f"={total}"
    print(output)
else:
    print("Invalid input")
```
</details>

**Note** We assign the value `1` to the variable `factorial` because the factorial of `0` is `1`. Then, we use a `for` loop to iterate through the numbers from `1` to `n` and multiply them to the `factorial` variable. Also, we can't assign it to `0` because the multiplication of any number by `0` is `0`.



## Example 16: Uppercase, Lowercase, and Space Count

**Problem:** Write a program that reads a string entered by the user and determines the number of uppercase letters, lowercase letters, and spaces in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name. | Upper 4<br>Lower 76<br>Spaces 18 |
| 2   | The quick brown fox jumps over the lazy dog | Upper 3<br>Lower 32<br>Spaces 8 |
| 3   | The cat in the hat | Upper 1<br>Lower 12<br>Spaces 4 |
| 4   | The quick brown fox jumps over the lazy dog | Upper 3<br>Lower 32<br>Spaces 8 |
| 5   | The cat in the hat | Upper 1<br>Lower 12<br>Spaces 4 |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

upper_count = 0
lower_count = 0
space_count = 0

for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isspace():
        space_count += 1

print(f"Upper {upper_count}")
```
</details>


## Example 17: Remove Duplicate Characters

**Problem:** Enter a string. Remove all duplicate characters and spaces from it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | aa     | a       |
| 2   | a a b b c dd e | abcde |
| 3   | 12345  | 12345  |
| 4   | 123 123  | 123   |
| 5   | 1 2 3 4 5  | 12345 |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

unique_chars = ""

for char in input_string:
    if char not in unique_chars and not char.isspace():
        unique_chars += char

print(unique_chars)


```
</details>


## Example 18: Find and Replace Substring

**Problem:** Given a string, find a specified substring and replace it with a new one. The user enters the string, the substring to replace, and the new string. Consider the case of replacing all substrings. Also, consider the case when the substring to be replaced is not present (print is impossible).

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12 45 32 567 32 109<br>32<br>0 | 12 45 0 567 0 109 |
| 2   | 12 45 32 567 32 109<br>33<br>-1 | is impossible |
| 3   | abc abc abc abc<br>abc<br>xyz | xyz xyz xyz xyz |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

substring = input("Enter the substring to replace: ")

new_substring = input("Enter the new substring: ")

# Solution 1

if substring in input_string:
    # Without using replace 
    result = ""
    i = 0
    while i < len(input_string) - len(substring) + 1:
        if input_string[i:i + len(substring)] == substring:
            result += new_substring
            i += len(substring)
        else:
            result += input_string[i]
            i += 1

    print(result)
else:
    print("is impossible")

# Solution 2

if substring in input_string:
    result = input_string.replace(substring, new_substring)
    print(result)
else:
    print("is impossible")
```

</details>

## Example 19: Longest Sequence of Zeros

**Problem:** Given a string of zeros and ones, write a program to find the longest continuous sequence of zeros in the string.

| No. | Inputs         | Outputs |
| --- | -------------- | ------- |
| 1   | 1001           | 2       |
| 2   | 100001001010   | 4       |
| 3   | 1000001        | 5       |

**Problem:** Determine the longest unbroken chain of zeros within a binary string.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the binary string
binary_string = input("Enter the binary string: ")

# Initialize variables to track the longest zero sequence and current zero count
longest_sequence = 0
current_count = 0

# Iterate over each character in the string
for char in binary_string:
    if char == '0':
        current_count += 1
    else:
        if current_count > longest_sequence:
            longest_sequence = current_count
        current_count = 0

# Check the last sequence in case the string ends with '0'
if current_count > longest_sequence:
    longest_sequence = current_count

# Print the longest sequence of zeros
print(longest_sequence)
```
</details>



## Example 20: Can Construct

**Problem:** Given two words, write a program that determines whether word B can be constructed from the letters of word A, taking into account the case sensitivity of the letters.

| No. | Inputs                | Outputs |
| --- | --------------------- | ------- |
| 1   | Python<br>not         | Yes     |
| 2   | Ruby<br>Buy           | No      |

**Problem:** Check if it is possible to construct word B using the letters from word A, considering letter case sensitivity.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for word A
word_a = input("Enter word A: ")
# Take input for word B
word_b = input("Enter word B: ")

# Check if word B can be constructed from word A
can_construct = True

for char_b in word_b:
    char_b_count = 0
    char_a_count = 0
    for char in word_b:
        if char == char_b:
            char_b_count += 1
    for char in word_a:
        if char == char_b:
            char_a_count += 1
    if char_b_count > char_a_count:
        can_construct = False
        break

# Output result
print("Yes" if can_construct else "No")
```
</details>

## Example 21: Check Bracket Balance

**Problem:** Given a sequence of characters of length n (n ≥ 1), verify the balance of parentheses in the expression (each opening parenthesis must have its corresponding closing parenthesis). For example, the input `(()) ()` should result in `True`, indicating correct placement, while the input `((())` should result in `False`, indicating incorrect placement. The program should be capable of checking the balance of parentheses in arithmetic expressions, text, etc.

| No. | Inputs                              | Outputs       |
| --- | ----------------------------------- | ------------- |
| 1   | (3y + 21)(12 - (x + 5))             | True          |
| 2   | (61x + 15(y + 2)                    | False         |

**Problem:** Write a program to check the balance of parentheses in various expressions.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the expression
expression = input("Enter the expression: ")

# Initialize counter for open parentheses
balance = 0
is_balanced = True

# Iterate through each character in the expression
for char in expression:
    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1
    # If at any point there are more closing parentheses, it's unbalanced
    if balance < 0:
        is_balanced = False
        break

# If there are open parentheses left unmatched, it's unbalanced
if balance != 0:
    is_balanced = False

# Output result
print("True" if is_balanced else "False")
```

</details>

## Example 22: Evaluate Expression

**Problem:** Given a string that consists of n digits (i.e., single-digit numbers), separated by n-1 operation signs which can be either '+' or '-', calculate the value of this expression. The program should print the result of evaluating this expression.

| No. | Inputs    | Outputs |
| --- | --------- | ------- |
| 1   | 5-3+1     | 3       |
| 2   | 6+3-2     | 7       |

**Problem:** Write a program to evaluate expressions consisting of single-digit numbers separated by '+' or '-' signs.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the expression
expression = input("Enter the expression: ")

# Initialize the result with the first number (assumes expression starts with a number)
result = int(expression[0])

# Loop through the expression starting from the first operator
i = 1
while i < len(expression):
    operator = expression[i]
    digit = int(expression[i+1])
    
    if operator == '+':
        result += digit
    elif operator == '-':
        result -= digit
    
    i += 2  # Move to the next operator

# Print the final result
print(result)
```
</details>



## Example 23: Count String Occurrences

**Problem:** Two strings A and B, consisting of lowercase English letters, are given as input. Output the number of occurrences of string B in string A.

| No. | Inputs                    | Outputs |
| --- | ------------------------- | ------- |
| 1   | aaaa<br>a                 | 4       |
| 2   | ababada<br>abc            | 0       |
| 3   | abababa<br>aba            | 3       |

**Problem:** Write a program that prints the number of times string B occurs in string A using two different approaches.

<details open>
<summary><b>Solution One</b></summary>

```python
# Input string A
a = input("Enter string A: ")
# Input string B
b = input("Enter string B: ")

count = 0
# Use a loop to manually check for occurrences
for i in range(len(a) - len(b) + 1):  # Only go up to where B can fully fit in A
    if a[i:i+len(b)] == b:  # Check if the substring of A equals B
        count += 1

# Print the number of occurrences
print(count)
```
</details>

<details open>
<summary><b>Solution Two</b></summary>
 
```python
# Input string A
a = input("Enter string A: ")
# Input string B
b = input("Enter string B: ")

# Initialize the count and the starting index
count = 0
start = 0

# Loop to find occurrences of string B in string A
while True:
    start = a.find(b, start)  # Find the next occurrence of B starting from index 'start'
    if start == -1:  # No more occurrences found
        break
    count += 1
    start += 1  # Move start index to the next character after the current match

# Print the number of occurrences
print(count)
```
</details>

## Example 24: Format Number with Commas

**Problem:** The user enters a string of digits without spaces. Write a program that "breaks" this number into groups of three digits from right to left using commas. If the number contains fewer than three digits, it should be displayed without changes.

| No. | Inputs   | Outputs     |
| --- | -------- | ----------- |
| 1   | 4567     | 4,567       |
| 2   | 123      | 123         |
| 3   | 2348906  | 2,348,906   |

**Problem:** Write a program that formats a string of digits by grouping every three digits with commas from right to left.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Input string of digits
number = input("Enter a string of digits: ")

# Start from the end and insert commas every three digits
formatted_number = ''
count = 0

# Reverse iterate over the number string
for i in range(len(number) - 1, -1, -1):
    formatted_number = number[i] + formatted_number
    count += 1
    if count == 3 and i != 0:  # Avoid adding a comma at the start
        formatted_number = ',' + formatted_number
        count = 0

# Print the formatted number
print(formatted_number)
```

</details>


## Example 25: Find and Replace Substring

**Problem:** Write a program that decrypts an input text using the method described.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Njzxwxgd Bpihjbdid, rgtpidg du iwt Gjqn egdvgpbbxcv apcvjpvt. | Yukihiro Matsumoto, creator of the Ruby programming language. |
| 2   | Wklv, qmzv, wklv, qmzv, wklv, qmzv. | This, that, this, that, this, that. |


<details open>
<summary><b>Python Solution</b></summary>

```python
# Input encrypted text
text = input("Enter encrypted text: ")

# Determine the number of letters 'k' in the longest word
k = 0
current_length = 0
max_length = 0

for char in text:
    if char.isalpha():
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
        current_length = 0

if current_length > max_length:
    max_length = current_length

k = max_length

# Decrypt the text directly in the loop
decrypted_text = ''
for char in text:
    if 'a' <= char <= 'z':  # Lowercase letters
        new_pos = (ord(char) - ord('a') - k) % 26 + ord('a')
        decrypted_text += chr(new_pos)
    elif 'A' <= char <= 'Z':  # Uppercase letters
        new_pos = (ord(char) - ord('A') - k) % 26 + ord('A')
        decrypted_text += chr(new_pos)
    else:
        decrypted_text += char  # Non-alphabet characters remain unchanged

# Output the decrypted text
print(decrypted_text)
```

</details>

## Example 26: Find Shortest Word and Its Length

**Problem:** In the given string, find the shortest word, and display this word along with its length in characters. Words may be separated by spaces, multiple spaces, punctuation marks, digits, etc. If there are multiple shortest words, only display the first one. The string of words is guaranteed to end with a period.

| No. | Inputs                         | Outputs  |
| --- | ------------------------------ | -------- |
| 1   | He lives in house number 4.    | He 2     |
| 2   | Now is better than never.      | is 2     |
| 3   | Tom Tells the Truth.           | Tom 3    |

**Problem:** Write a program that finds and prints the shortest word in the input text along with its length using only string operations.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Input a sentence from the user
sentence = input("Enter a sentence ending with a period: ")

# Remove the trailing period for ease of processing
sentence = sentence[:-1]

# Initialize variables to find the shortest word and its length
shortest_word = ''
min_length = len(sentence)
current_word = ''

# Traverse each character in the sentence
for char in sentence:
    # Build a word while iterating through alphabetical characters
    if char.isalpha():
        current_word += char
    else:
        # Check if a word was built and is shorter than the known shortest word
        if current_word and (len(current_word) < min_length):
            shortest_word = current_word
            min_length = len(current_word)
        # Reset current word after saving
        current_word = ''

# Final check for the last word in case the sentence ends directly after it
if current_word and (len(current_word) < min_length):
    shortest_word = current_word
    min_length = len(current_word)

# Output the shortest word and its length
print(f'{shortest_word} {min_length}')


## Example 26: Sequence Element Comparison

**Problem:** Given a sequence of natural numbers that ends with the number `0`. Determine how many elements of this sequence are greater than the previous element.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4<br>3<br>6<br>8<br>0 | 2 |
| 2   | 1<br>2<br>3<br>4<br>0 | 3 |
| 3   | 1<br>1<br>1<br>1<br>0 | 0 |

<details open>
<summary><b>Python Solution</b></summary>

```python
count = 0
previous = int(input("Enter the number: "))

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    if number > previous:
        count += 1
    previous = number

print(count)
```

</details>

## Example 27: Run-Length Encoding

**Problem:** Implement a simple version of the run-length encoding (RLE) data compression algorithm. The algorithm receives a string containing English alphabet characters. This string is split into groups of consecutive identical characters ("runs"). Each run is characterized by the character and the number of repetitions. This information is then encoded: the length of the run of repeated characters is written first, followed by the character itself. If a run consists of only one character, the count is omitted.

| No. | Inputs                  | Outputs        |
| --- | ----------------------- | -------------- |
| 1   | aaabccccCCaB            | 3ab4c2CaB      |
| 2   | aabcccddffffffffff      | 2ab3c2d10f     |

**Problem:** Write a program that outputs a run-length encoding of the input text.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Input string
input_string = input("Enter a string: ")

# Variable to store the encoded result
encoded_string = ""

# Initialize count and previous character
count = 1
previous_char = input_string[0]

# Iterate over the string starting from the second character
for char in input_string[1:]:
    if char == previous_char:
        count += 1
    else:
        # Append the count and character to the result string if count is more than 1
        if count > 1:
            encoded_string += str(count)
        encoded_string += previous_char
        # Reset the count and update previous character
        previous_char = char
        count = 1

# Handle the last run
if count > 1:
    encoded_string += str(count)
encoded_string += previous_char

# Print the encoded string
print(encoded_string)

```

</details>

## Example 28: Evaluate Simple Arithmetic Expression

**Problem:** Given a string containing one or more integers between 0 and 1,000,000,000, separated by '+' or '-' signs, calculate the value of this expression.

| No. | Inputs       | Outputs |
| --- | ------------ | ------- |
| 1   | 12-5+3       | 10      |
| 2   | 26-14+2-1    | 13      |
| 3   | 7-0+3        | 10      |

**Problem:** Write a program that calculates and outputs the result of evaluating these arithmetic expressions.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Function to evaluate the given arithmetic expression
def evaluate_expression(expression):
    current_number = 0
    total = 0
    last_sign = 1  # Start assuming the first number is positive

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+' or char == '-':
            total += last_sign * current_number
            current_number = 0
            last_sign = 1 if char == '+' else -1

    # Add the last number
    total += last_sign * current_number

    return total

# Example input and output
expressions = ["12-5+3", "26-14+2-1", "7-0+3"]
results = [evaluate_expression(expr) for expr in expressions]
for expr, result in zip(expressions, results):
    print(f'Input: {expr}, Output: {result}')


## Example 28: Sequence Element Comparison

**Problem:** Given a sequence of natural numbers that ends with the number `0`. Determine the largest number of elements in this sequence that go one after the other and are equal to each other (i.e., the longest consecutive sequence of identical elements). Also, print the element that is repeated most consecutively. If there are multiple elements with the same maximum consecutive count, the task does not specify which one to print, so we'll choose to print any one of them.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>5<br>5<br>4<br>3<br>9<br>9<br>9<br>7<br>0 | 3<br>9 |
| 2   | 1<br>2<br>3<br>4<br>0 | 1<br>No numbers were entered before 0. |
| 3   | 1<br>1<br>1<br>1<br>0 | 4<br>1 |


<details open>
<summary><b>Python Solution</b></summary>

```python
max_count = 0
max_element = None
current_count = 1
last_element = None

number = int(input("Enter a number (0 to end): "))
last_element = number

while number != 0:
    number = int(input("Enter a number (0 to end): "))
    
    if number == last_element:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            max_element = last_element
        current_count = 1
    
    last_element = number

if current_count > max_count:
    max_count = current_count
    max_element = last_element

print(f"Longest sequence length: {max_count}")
if max_count > 0:
    print(f"Most repeated element: {max_element}")
else:
    print("No numbers were entered before 0.")

```

</details>

Дано рядок, який може міститити пропуски. Визначте, яка буква англійського алфавіту (або які букви) в цьому рядку зустрічається найчастіше. Великі і малі літери вважаються однаковими, а інші символи, які не є буквами, не враховуються. Програма повинна вивести в першому рядку всі букви, які зустрічаються найчастіше в заданому рядку. Виводити букви необхідно у верхньому регістрі, в алфавітному порядку (додатково), без пропусків. У другому рядку виведіть єдине число - скільки разів у цьому рядку зустрічаються ці літери. При виконанні цього завдання не можна користуватися вкладеними циклами. Вхідний рядок повинен оброблятися за один прохід.

Вхідні дані:

Project Gutenberg EBook of The jungle book, by Rudyard Kipling
Вихідні дані:

EO
6

## Example 29: Divisibility Graphical Representation

**Problem:** Write a program to graphically represent the divisibility of numbers from `1` to `n` (the value of `n` is entered from the keyboard). In each line, print the next number and as many `+` characters as there are divisors of this number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1     | 1+      |
| 2   | 2     | 1+<br>2++ |
| 3   | 3     | 1+<br>2++<br>3++ |
| 4   | 4     | 1+<br>2++<br>3++<br>4+++ |
| 5   | 5     | 1+<br>2++<br>3++<br>4+++<br>5++ |
| 6   | 6     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++ |
| 7   | 7     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++ |
| 8   | 8     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++<br>8++++ |
| 9   | 9     | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++<br>8++++<br>9++++ |
| 10  | 10    | 1+<br>2++<br>3++<br>4+++<br>5++<br>6++++<br>7++<br>8++++<br>9++++<br>10++++ |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

for i in range(1, n + 1):
    divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisors += 1
    print(f"{i}{'+' * divisors}")
```

</details>

У мережі Інтернет кожному комп’ютері присвоюється IP-адреса (чотирьохбайтовий код, який прийнято записувати у вигляді чотирьох чисел, кожне з яких може приймати значення від 0 до 255 і між якими ставлять крапку). Ось приклади правильних IP-адрес: 192.168.0.1, 255.0.255.255, 10.10.0.2. Програма отримує на вхід рядок з довільних символів і якщо цей рядок є коректним записом IP-адреси, виведіть Yes, інакше виведіть No.

Вхідні дані:

C.E.R.N
192.168.0.200
256.0.0.255
Вихідні дані:

No
Yes
No

## Example 30: Number Reversal

**Problem:** Given a natural number `n`. Print the number that is the reverse of the order of its digits.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 125    | 521     |
| 2   | 123456789 | 987654321 |
| 3   | 1      | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
temp_number = n

reversed_number = 0

# Solution 1
while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10

print(reversed_number)

# Solution 2
n = temp_number
power = 0 
while temp_number > 0:
    temp_number //= 10
    power += 1

reversed_number = 0

while n > 0:
    current_digit = n % 10
    number_to_add = current_digit * (10 ** (power - 1))
    reversed_number += number_to_add
    n //= 10
    power -= 1

print(reversed_number)
```

</details>


**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
