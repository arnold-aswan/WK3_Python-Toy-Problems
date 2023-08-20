# Phase 3 Week 1 Code Challenge (Toy Problems)

This repository contains solutions to three code challenges. Each challenge is implemented as a Python function. Below is a brief description of each challenge and how to use the corresponding function.

## Challenge 1: Converting 12-hour time to 24-hour time

This challenge involves converting a 12-hour time to 24-hour time (like "0830" or "2030").
The function `convert_time` takes an hour (in the range of 1 to 12), a minute (in the range of 0 to 59), and a period ("am" or "pm") as input and returns a four-digit string representing the time in 24-hour format.

Example usage:

```python
result = convert_time(8, 30, "am")
print(result)  #=> Output: "0830"
result2 = convert_time(8, 30, "pm")
print(result2) #=> Output: "2030"
```

## Challenge 2: Two numbers are positive.

In this challenge, the goal is to determine if exactly two out of three integers are positive numbers. The function `two_positive_numbers` takes three integers (a, b, and c) as arguments and returns True if exactly two of them are positive, otherwise False.

Example usage:

```python
result = two_positive_numbers(2, 4, -3)
print(result)  #=> Output: True
result2 = two_positive_numbers(4, 6, 10)
print(result2)  #=> Output: False
```

## Challenge 3: Consonant value

This challenge involves finding the highest value of consonant substrings in a lowercase string. Consonants are any letters except "aeiou," and their values are assigned from 'a' to 'z' (a = 1, b = 2, c = 3, ..., z = 26). The function consonant_value takes a string with alphabetic characters only and returns the highest value of consonant substrings.

Example usage:

```python
Copy code
result = consonant_value("zodiacs")
print(result)  # Output: 26
```

## Dependencies

Make sue you have the following installed first

- Python (v3)
- Python interpreter

## Project Setup

1. Clone the repo
   `git@github.com:arnold-aswan/WK3_Python-Toy-Problems.git`
2. Navigate to Challenges directory
   `cd Challenges`
3. Open the `Challenges` directory with your desired IDE, i.e `visual studio code`

# Author & License

Author: [Arnold Aswani](https://github.com/arnold-aswan)

Licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
