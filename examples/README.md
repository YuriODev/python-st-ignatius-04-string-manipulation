# Examples 👨🏼‍💻

Here are some examples to get you started.

<details open>
<summary><b>Covered topics</b></summary>

| Topic Covered                                           | Code with explanations                           |
| ------------------------------------------------------- | ------------------------------------------------- |
| Repeat Last Two Characters                              | [Detailed code](./example_1.py)      |
| Reverse Digits                                          | [Detailed code](./example_2.py)      |
|  Average Grade Calculation                              | [Detailed code](./example_3.py)      |
|  Number of # Characters Printing              | [Detailed code](./example_4.py)      |
|  Triangle of Numbers Printing                 | [Detailed code](./example_5.py)      |
|  Positive, Negative, and Zero Numbers Counting | [Detailed code](./example_6.py)      |
|  Two-Digit Odd Numbers Printing                | [Detailed code](./example_7.py)      |
|  Number of Digits Counting                     | [Detailed code](./example_8.py)      |
|  Printing Numbers with Conditions             | [Detailed code](./example_9.py)      |
| Multiplication Table Printing                | [Detailed code](./example_10.py)    |
| Sum of Products Calculation                  | [Detailed code](./example_11.py)    |
| Number Entry and Exit                        | [Detailed code](./example_12.py)    |
| Sum of Integers Calculation                  | [Detailed code](./example_13.py)    |
| Pattern Printing                             | [Detailed code](./example_14.py)    |
| Factorial Calculation                        | [Detailed code](./example_15.py)    |
| Sum of Sequence Elements Calculation         | [Detailed code](./example_16.py)    |
| Sum of Digits Calculation                    | [Detailed code](./example_17.py)    |
| Power Calculation                            | [Detailed code](./example_18.py)    |
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

 - Repeat Last Two Characters

**Problem:** Print 5 copies of the last two characters from a user-entered string on the screen (where the length of the entered string is at least 2).

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

# Ensure the input string has at least 2 characters
if len(input_string) >= 2:
    # Extract the last two characters
    last_two = input_string[-2:]
    # Print the last two characters repeated 5 times
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

**Problem:** Compute the number obtained by reversing the digits of a given natural number.

<details open>
<summary><b>Python Solution</b></summary>

```python
input_number = input("Enter a natural number: ")

# Convert the number to a string to reverse it
reversed_number = input_number[::-1]

# Print the reversed number
print(reversed_number)
```
</details>

### Example 3: Check Start of String

**Problem:** The user enters a string and a set of characters. Write a program that checks if the string starts with the given characters.

| No. | Inputs                      | Outputs |
| --- | --------------------------- | ------- |
| 1   | wireless router<br> route     | False   |

**Problem:** Verify whether a user-input string begins with the specified characters.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the string and the prefix to check
input_string = input("Enter the string: ")
prefix = input("Enter the prefix: ")

# Check if the string starts with the given prefix
starts_with_prefix = input_string.startswith(prefix)

# Print the result
print(starts_with_prefix)

```
</details>

Дано натуральне число. Знайти число, що отримується з вхідного перестановкою його першої та останньої цифр. Врахувати випадок введення одноцифрового числа.

Вхідні дані:

1467
5
11
12
Вихідні дані:

7461
5
11
21

## Example 4: Number of # Characters Printing

**Problem:** Write a program to print integers from `n` to `0` with the number of `#` characters equal to the value of the number.

| No. | Inputs | Outputs                               |
| --- | ------ | ------------------------------------- |
| 1   | 6      | 6 ######<br>5 #####<br>4 ####<br>3 ###<br>2 ##<br>1 # |
| 2   | 3      | 3 ###<br>2 ##<br>1 # |
| 3   | 1      | 1 # |

<details open>
<summary><b>Python Solution</b></summary>

```python

n = int(input("Enter the number: "))

for i in range(n, -1, -1):
    print(i, "#" * i)
```
</details>


Користувач вводить рядок, в якому можуть бути пристуні пропуски. Визначити, чи є рядок паліндромом, тобто таким, який однаково читається як справа наліво, так і зліва направо. Для літер регістр не враховувати. Приклади рядків-паліндромів: racecar, 10201, Ada, Never odd or even.

Вхідні дані:

Ada
Able was I ere I saw Elba
10501
Origin
Вихідні дані:

True
True
True
False

## Example 5: Triangle of Numbers Printing

**Problem:** Given an integer `n` (1 ≤ `n` ≤ 9). Print a triangle of numbers from `1` to `n` as shown in the example.

| No. | Inputs | Outputs             |
| --- | ------ | ------------------- |
| 1   | 9      | 1<br>22<br>333<br>4444<br>55555<br>666666<br>7777777<br>88888888<br>999999999 |
| 2   | 5      | 1<br>22<br>333<br>4444<br>55555 |
| 3   | 1      | 1 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(str(i) * i)
```
</details>

Для введеного єдиного символу, перевірте, чи є він цифрою. Під час розв’язування задачі не можна використовувати функції для роботи з рядками. Програма повинна вивести слово Yes, якщо символ є цифрою, або слово No.

Вхідні дані:

7
A
h
Вихідні дані:

Yes
No
No

## Example 6: Positive, Negative, and Zero Numbers Counting

**Problem:** Write a program that counts the positive and negative numbers, as well as zeros entered by the user, and outputs their quantity in one line with one space between them.

| No. | Inputs | Outputs                      |
| --- | ------ | ---------------------------- |
| 1   | 5<br>12<br>-45<br>0<br>14<br>0 | 2 1 2 |
| 2   | 1<br>2<br>3<br>4<br>5<br>6 | 6 0 0 |
| 3   | -1<br>-2<br>-3<br>-4<br>-5<br>-6 | 0 6 0 |

<details open>
<summary><b>Python Solution</b></summary>

```python
positive = 0
negative = 0
zeros = 0

n = int(input("Enter the number of integers: "))

for _ in range(n):
    number = int(input("Enter the number: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zeros += 1

print(positive, negative, zeros)
```
</details>

Користувач вводить рядок, у якому чергуються цифри та інші символи. На початку і у кінці рядка цифри відсутні. Напишіть програму, яка друкує усі символи введеного рядка у тому ж порядку, але без цифр.

Вхідні дані:

H1e2l3l4o5w6o7r8l9d
i1m3p4o9r0t4 6t7h8i9s
Вихідні дані:

Helloworld
import this

## Example 7: Two-Digit Odd Numbers Printing

**Problem:** Print all two-digit odd numbers whose last digit is `n` - an integer entered by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5      | 15 25 35 45 55 65 75 85 95 |
| 2   | 1      | 11 21 31 41 51 61 71 81 91 |
| 3   | 0      | 10 20 30 40 50 60 70 80 90 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

for i in range(10, 100):
    if i % 2 != 0 and i % 10 == n:
        print(i, end=" ")
```
</details>

Напишіть програму, яка виводить перше слово у рядку. Слово - це послідовність непробільних символів, обмежена пропусками або межами рядка. Вхідний рядок містить довільну послідовність символів. Програма повинна вивести перше слово цього рядка.

Вхідні дані:

Stranger Things
Вихідні дані:

Stranger

## Example 8: Number of Digits Counting

**Problem:** Given a natural number `n`. Determine the number of digits in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12367832 | 8       |
| 2   | 142      | 3       |
| 3   | 0        | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python

n = int(input("Enter the number: "))

count = 0

while n > 0:
    n //= 10 # Decrease the number by one digit
    count += 1 # Increase the count by one

print(count)
```
</details>

Для доступу до власного акаунту на сайті соціальної мережі користувач ввів логін і пароль. Так як була увімкнена двофакторна авторизація, на його телефон прийшло повідомлення з рядком цифр та інформацією як отримати код доступу. У повідомленні йшлося: «Кожну цифру, яка більша 5, необхідно націло розділити на 2, а потім з утвореної послідовності цифр видалити усі парні числа». Який код повинен ввести користувач для успішної авторизації? Напишіть програму, на вхід якої вводиться рядок цифр із повідомлення, а програма повинна надрукувати правильний код доступу.

Вхідні дані:

5763
1977
Вихідні дані:

33
33

## Example 9: Printing Numbers with Conditions

**Problem:** Write a program that prints integers from `1` to `n` (1 < `n` ≤ 1000) with the following condition: for numbers divisible by 3, it prints `*3*` instead of the number, for numbers divisible by 5, it prints `*5*`, and for numbers divisible by 3 and 5 simultaneously, the message will be `*35*`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 15     | 1<br>2<br>\*3\*<br>4<br>\*5\*<br>\*3\*<br>7<br>8<br>\*3\*<br>\*5\*<br>11<br>\*3\*<br>13<br>14<br>\*35\* |
| 2   | 20     | 1<br>2<br>\*3\*<br>4<br>\*5\*<br>\*3\*<br>7<br>8<br>\*3\*<br>\*5\*<br>11<br>\*3\*<br>13<br>14<br>\*35\*<br>16<br>17<br>\*3\*<br>19<br>\*5\* |
| 3   | 10     | 1<br>2<br>\*3\*<br>4<br>\*5\*<br>\*3\*<br>7<br>8<br>\*3\*<br>\*5\* |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("*35*")
    elif i % 3 == 0:
        print("*3*")
    elif i % 5 == 0:
        print("*5*")
    else:
        print(i)
```
</details>

Виведіть усі символи ASCII з кодами від n (n > 32) до m (m < 127) і їх коди в наступному вигляді: «символ код».

Вхідні дані:

101
106
Вихідні дані:

e 101
f 102
g 103
h 104
i 105
j 106

## Example 10:  Multiplication Table Printing

**Problem:** Write a program to create a multiplication table (from 1 to 10) for the entered integer `n`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3      | 3 x 1 = 3<br>3 x 2 = 6<br>3 x 3 = 9<br>3 x 4 = 12<br>3 x 5 = 15<br>3 x 6 = 18<br>3 x 7 = 21<br>3 x 8 = 24<br>3 x 9 = 27<br>3 x 10 = 30 |
| 2   | 5      | 5 x 1 = 5<br>5 x 2 = 10<br>5 x 3 = 15<br>5 x 4 = 20<br>5 x 5 = 25<br>5 x 6 = 30<br>5 x 7 = 35<br>5 x 8 = 40<br>5 x 9 = 45<br>5 x 10 = 50 |
| 3   | 7      | 7 x 1 = 7<br>7 x 2 = 14<br>7 x 3 = 21<br>7 x 4 = 28<br>7 x 5 = 35<br>7 x 6 = 42<br>7 x 7 = 49<br>7 x 8 = 56<br>7 x 9 = 63<br>7 x 10 = 70 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
</details>

Дано рядок, що складається з слів, розділених пропусками. Визначте кількість слів у рядку.

Вхідні дані:

Events happened very rapidly with Francis Morgan that late spring morning
Вихідні дані:

11

## Problem 11: Sum of Products Calculation


**Problem:** For a given integer `n` (n > 1), calculate the value `1 × 2 + 2 × 3 + …​ + (n - 1) × n`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 6      | 70      |
| 2   | 5      | 40      |
| 3   | 3      | 8       |

<details open>
<summary><b>Python Solution</b></summary>
    
```python
n = int(input("Enter the number: "))
total = 0

for i in range(1, n):
    total += i * (i + 1)

print(total)

```
</details>

Напишіть програму для розрахунку довжини рядка без використання функції len().

Вхідні дані:

pythonguide.pp.ua
Вихідні дані:

17

## Problem 12: Number Entry and Exit

**Problem:** Write a program where the user enters integers. If an integer `n` is entered, the program should end its execution with the message `Done`. First, the user enters the number `n`, and then the rest of the numbers. 

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>67<br>112<br>14<br>5 | Done |
| 2   | 3<br>1<br>2<br>3 | Done |
| 3   | 1<br>1 | Done |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

while True:
    number = int(input("Enter the number: "))
    if number == n:
        print("Done")
        break
```
</details>

Напишіть програму, яка отримує рядок і обчислює кількість цифр і букв у ньому.

Вхідні дані:

Andromeda, M 31, NGC 224
Вихідні дані:

Letters 13
Digits 5

## Problem 13: Sum of Integers Calculation

**Problem:** Given `n` integers. Each number is entered on a separate line. Calculate the sum of the numbers.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 10<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | 45 |
| 2   | 3<br>1<br>2<br>3 | 6 |
| 3   | 1<br>1 | 1 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number of integers: "))
total = 0

for _ in range(n):
    total += int(input("Enter the number: "))

print(total)
```
</details>

Напишіть програму для перевірки чи є введена літера голосною або приголосною.

Вхідні дані:

F
e
Вихідні дані:

F is a consonant
e is a vowel

## Problem 14: Pattern Printing

**Problem:** Write a program to build a pattern as in the output data for the entered value `n`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 7      | 1  2  3  4  5  6  7<br>2  3  4  5  6  7<br>3  4  5  6  7<br>4  5  6  7<br>5  6  7<br>6  7<br>7 |
| 2   | 5      | 1  2  3  4  5<br>2  3  4  5<br>3  4  5<br>4  5<br>5 |
| 3   | 3      | 1  2  3<br>2  3<br>3 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
```
</details>

При заданому користувачем значенні цілого числа n ≥ 2 обчислити суму 1 x 2 + 2 x 3 + ... + (n - 1) x n. Відповідь виведіть у вигляді обчисленого виразу і його значення в точності, як показано у вихідних даних.

Вхідні дані:

2
4
Вихідні дані:

1*2=2
1*2+2*3+3*4=20

## Problem 15: Factorial Calculation

**Problem:** Given a positive integer `n`, calculate the value of `n!` - the factorial of this number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3      | 6       |
| 2   | 4      | 24      |
| 3   | 1      | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
```
</details>

**Note** We assign the value `1` to the variable `factorial` because the factorial of `0` is `1`. Then, we use a `for` loop to iterate through the numbers from `1` to `n` and multiply them to the `factorial` variable. Also, we can't assign it to `0` because the multiplication of any number by `0` is `0`.

Напишіть програму, яка зчитує рядок, введений користувачем, та визначає у ньому: кількість великих літер, кількість малих літер, кількість символів пропуску.

Вхідні дані:

By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name.
Вихідні дані:

Upper 4
Lower 76
Spaces 18

## Problem 16: Sum of Sequence Elements Calculation

**Problem:** Determine the sum of all elements of the sequence that ends with the number `0`. A sequence of integers that ends with the number `0` is entered (the number `0` itself is not included in the sequence, but is used as a sign of its end).

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>5<br>3<br>0 | 10 |
| 2   | 1<br>2<br>3<br>4<br>5<br>0 | 15 |
| 3   | 0 | 0 |

<details open>
<summary><b>Python Solution</b></summary>

```python
total = 0

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    total += number

print(total)
```
</details>

Вводиться рядок. Потрібно видалити з нього повторювані символи і всі пропуски.

Вхідні дані:

aa
a a b b c dd e
Вихідні дані:

a
abcde

## Problem 17: Largest Element Calculation

**Problem:** Given a sequence of natural numbers, ending with the number `0`. Determine the value of the largest element in the sequence.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>3<br>8<br>0 | 8 |
| 2   | 1<br>2<br>3<br>4<br>5<br>0 | 5 |
| 3   | 17<br>12<br>3<br>0 | 17 |

<details open>
<summary><b>Python Solution</b></summary>

```python
max_number = 0

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    if number > max_number:
        max_number = number

print(max_number)
```
</details>

Знайти у рядку зазначений підрядок і замінити його на новий. Рядок, підрядок для заміни та новий рядок вводить користувач. Розгляньте випадок заміни усіх підрядків. Також необхідно врахувати випадок відсутності підрядка, який необхідно замінити (вивести is impossible).

Вхідні дані:

12 45 32 567 32 109
32
0
12 45 32 567 32 109
33
-1
Вихідні дані:

12 45 0 567 0 109
is impossible

## Problem 18: Sum of Digits Calculation

**Problem:** Write a program that outputs all three-digit numbers whose sum of digits is equal to a certain value `n` entered by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4      | 112 121 130 202 211 220 301 310 400 |
| 2   | 5      | 104 113 122 131 140 203 212 221 230 302 311 320 401 410 500 |
| 3   | 6      | 105 114 123 132 141 150 204 213 222 231 240 303 312 321 330 402 411 420 501 510 600 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

digits_total = 0

for i in range(100, 1000):
    current_number = i
    digits_total = 0
    
    while current_number > 0:
        digits_total += current_number % 10
        current_number //= 10

    if digits_total == n:
        print(i, end=" ")
```

</details>

Дано рядок нулів та одиниць. Напишіть програму для знаходження найдовшої неперервної послідовності нулів у рядку.

Вхідні дані:

1001
100001001010
1000001
Вихідні дані:

2
4
5

## Problem 19: Power Calculation

**Problem:** Given integers `a` and `b`. Calculate `a` to power of `b` without using the exponentiation operation.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>3  | 8       |
| 2   | 3<br>3  | 27      |
| 3   | 5<br>2  | 25      |

<details open>
<summary><b>Python Solution</b></summary>

```python
a = int(input("Enter the base: "))
b = int(input("Enter the exponent: "))

result = 1

for _ in range(b):
    result *= a

print(result)
```
</details>

Дано два слова. Складіть програму, що визначає чи можна чи ні з букв слова A скласти слово B. Програма має враховувати регістр літер введених слів.

Вхідні дані:

Python
not
Ruby
Buy
Вихідні дані:

Yes
No

## Problem 20: Quiz Winner Determination

**Problem:** High school students took part in a computer science quiz. They had to answer 20 questions. The winner of the quiz is the participant who correctly answered the most questions. How many questions did the winner answer correctly? If there are participants in the quiz who could not give a correct answer to any of the questions, print Yes, otherwise print No. It is guaranteed that there are participants who correctly answered at least one question. The program receives the number of quiz participants `n` (1 ≤ `n` ≤ 50) as input, then for each participant, the number of questions they answered correctly is entered.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5<br>10<br>15<br>7<br>0<br>16 | 16<br>Yes |
| 2   | 3<br>0<br>0<br>0<br>0 | 0<br>Yes |
| 3   | 4<br>20<br>20<br>20<br>20 | 20<br>No |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number of participants: "))
max_score = 0
failed_quiz = False

for _ in range(n):
    score = int(input("Enter the score: "))
    if score > max_score:
        max_score = score
    elif score == 0:
        failed_quiz = True

print(max_score)
print("Yes" if failed_quiz else "No")
```
</details>

Дано послідовність символів довжини n (n ≥ 1). Перевірити баланс круглих дужок в цьому виразі (кожна відкита дужка має свою закриту дужку). Наприклад, при введенні виразу (()) () програма повинна повідомити про правильність розстановки дужок (True), а при введенні виразу ((()) - про неправильність (False). Напишіть програму, яка може перевіряти баланс дужок в арифметичних виразах, тексті і т. д.

Вхідні дані:

(3y + 21)(12 - (x + 5))
(61x + 15(y + 2)
Вихідні дані:

True
False

## Problem 21: Average Speed Calculation

**Problem:** A surveillance camera automatically registers the speed of passing cars, rounding the speed values to integers. It is necessary to determine the average registered speed of all cars. If the speed of at least one car was more than 60 km/h, print Yes, otherwise print No. The program receives the number of registered cars `n` (1 ≤ `n` ≤ 30) as input, then the speeds of the cars are indicated. The speed value cannot be less than 1 and more than 300. The program should first print the average speed with an accuracy of one decimal place, then Yes or No.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3<br>50<br>45<br>65 | 53.3<br>Yes |
| 2   | 2<br>100<br>200 | 150.0<br>Yes |
| 3   | 1<br>30 | 30.0<br>No |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number of cars: "))

total_speed = 0
over_speed = False

for _ in range(n):
    speed = int(input("Enter the speed: "))
    total_speed += speed
    if speed > 60:
        over_speed = True

average_speed = total_speed / n
print(f"{average_speed:.1f}")
print("Yes" if over_speed else "No")
```

</details>

Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.

Вхідні дані:

5-3+1
6+3-2
Вихідні дані:

3
7

## Problem 22: Automorphic Number Determination

**Problem:** Given a natural number `n`. Determine if it is an automorphic number. Note. An automorphic number is a number whose square is equal to the last digits of the square of this number: 5 - 25, 6 - 36, 25 - 625.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 9376   | True    |
| 2   | 26     | False   |
| 3   | 25     | True    |
| 4   | 6      | True    |
| 5   | 5      | True    |
| 6   | 1      | True    |
| 7   | 76     | True    |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))
temp_number = n

square = n ** 2
digit_count = 0

while temp_number > 0:
    temp_number //= 10
    digit_count += 1

power = 10 ** digit_count

if square % power == n:
    print(True)
else:
    print(False)

```

</details>

На вхід програми подається два рядка A і B, що складаються з малих букв англійського алфавіту. Виведіть кількість входжень рядка B в рядок A.

Вхідні дані:

aaaa
a
ababada
abc
abababa
aba
Вихідні дані:

4
0
3

## Problem 23: Least Common Multiple Calculation

**Problem:** Write a program that helps to find the least common multiple (LCM) of two numbers. The program should read two positive integers `a` and `b` (each number is entered on a separate line) and print the smallest number that is divisible by both of these numbers without a remainder.
The formula to calculate the Least Common Multiple (LCM) of two numbers `a` and `b` is given by:

$$\text{LCM}(a, b) = \frac{|ab|}{\text{GCD}(a, b)},$$

where $\text{GCD}(a, b)$ is the greatest common divisor of numbers `a` and `b`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4<br>6  | 12      |
| 2   | 15<br>25 | 75      |
| 3   | 1<br>1   | 1       |
| 4   | 5<br>8   | 40      |

<details open>
<summary><b>Python Solution</b></summary>

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x = a
y = b

product = a * b

# Solution 1
while b:
    a, b = b, a % b

gcd = a
lcm = product // gcd
print(lcm)

# Solution 2
while y != 0:
    temp = y
    y = x % y
    x = temp

gcd = x
lcm = product // gcd
print(lcm)
```

</details>

Користувач вводить рядок цифр без пропусків. Необхідно написати програму, яка «розіб’є» це число на трійки цифр справа наліво комами. Якщо число містить менше трьох цифр, то воно виводиться без змін.

Вхідні дані:

4567
123
2348906
Вихідні дані:

4,567
123
2,348,906

## Problem 24: Monotonous Sequence Printing

**Problem:** Given a natural number `n`. Print the first `n` members of the sequence. The sequence is a monotonous sequence in which each natural number `k` occurs exactly `k` times: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ....

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1     | 1       |
| 2   | 2     | 1 2     |
| 3   | 3     | 1 2 2   |
| 4   | 4     | 1 2 2 3 |
| 5   | 5     | 1 2 2 3 3 |
| 6   | 6     | 1 2 2 3 3 3 |
| 7   | 7     | 1 2 2 3 3 3 4 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

i = 1
count = 0

while count < n:
    for _ in range(i):
        if count < n:
            print(i, end=" ")
            count += 1
    i += 1
```

</details>

Дано текст і відомо, що він шифрується наступним чином. Спочатку визначається кількість букв k в найдовшому слові (словом називається безперервна послідовність англійських букв, слова один від одного відокремлюються будь-якими іншими символами, довжина слова не перевищує 20 символів). Потім кожна англійська літера замінюється на букву, що стоїть в алфавіті на k букв раніше (алфавіт вважається циклічним, тобто перед буквою A стоїть буква Z). Інші символи залишаються незмінними. Малі літери при цьому залишаються малими, а великі - великими. Розшифруйте введений текст.

Вхідні дані:

Njzxwxgd Bpihjbdid, rgtpidg du iwt Gjqn egdvgpbbxcv apcvjpvt.
Вихідні дані:

Yukihiro Matsumoto, creator of the Ruby programming language.

## Problem 25: Fibonacci Number Determination

**Problem:** Given a natural number `n`. Determine which Fibonacci number it is. If `n` is not a Fibonacci number, print the value `-1`. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 11     | -1      |
| 2   | 8      | 6       |
| 3   | 13     | 7       |
| 4   | 21     | 8       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

a = 0
b = 1
c = 0
count = 0

while c < n:
    c = a + b
    a = b
    b = c
    count += 1

if c == n:
    print(count)
else:
    print(-1)
```

</details>

У заданому рядку знайти найкоротше слово, вивести це слово і його розмір у символах. Слова можуть бути розділені пропусками, декількома пропусками, знаками пунктуації, цифрами тощо. Якщо найкоротших слів є кілька, вивести лише перше з них. Рядок слів гарантовано закінчується крапкою.

Вхідні дані:

He lives in house number 4.
Now is better than never.
Tom Tells the Truth.
Вихідні дані:

He 2
is 2
Tom 3

## Problem 26: Sequence Element Comparison

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

Кодування довжин послідовностей - це базовий алгоритм стиснення даних. Реалізуйте один з найпростіших його варіантів. На вхід алгоритму подається рядок, що містить символи англійського алфавіту. Цей рядок розбивається на групи однакових символів, що йдуть підряд («серії»). Кожна серія характеризується символом і кількістю повторень. Саме ця інформація і записується в код: спочатку пишеться довжина серії повторюваних символів, потім сам символ. У серій довжиною в один символ кількість повторень не записується.

Вхідні дані:

aaabccccCCaB
aabcccddffffffffff
Вихідні дані:

3ab4c2CaB
2ab3c2d10f

## Problem 27:

**Problem:** Given a sequence of natural numbers that ends with the number `0`. Determine how many elements of this sequence are equal to its largest element.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3<br>8<br>10<br>2<br>10<br>7<br>0 | 2 |
| 2   | 1<br>2<br>3<br>4<br>0 | 1 |
| 3   | 1<br>1<br>1<br>1<br>0 | 4 |

<details open>
<summary><b>Python Solution</b></summary>

```python
max_number = 0
max_count = 0

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    if number > max_number:
        max_number = number
        max_count = 1
    elif number == max_number:
        max_count += 1

print(max_count)
```

</details>

Дано рядок, що містить одне або більше цілих чисел від 0 до 1000000000, розділених знаками + або -. Розрахуйте значення цього виразу.

Вхідні дані:

12-5+3
26-14+2-1
7-0+3
Вихідні дані:

10
13
10

## Problem 28: Sequence Element Comparison

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

## Problem 29: Divisibility Graphical Representation

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

## Problem 30: Number Reversal

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
