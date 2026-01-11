# Luhn Check (Card Number Validation)

This function checks whether a card number is valid using the **Luhn algorithm**. It works by cleaning the input, doubling every second digit from the right, subtracting 9 if the doubled digit is greater than 9, and then checking if the total is divisible by 10.

## Code

```python
def verify_card_number(accNum):
    cleaned = accNum.replace(" ", "").replace("-", "")
    digits = [int(d) for d in cleaned]

    total = 0

    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]

        if (len(digits) - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    return "VALID!" if total % 10 == 0 else "INVALID!"
```

## Line-by-Line Explanation

- `cleaned = accNum.replace(" ", "").replace("-", "")`  
  Removes spaces and dashes so only digits remain.  
  Example: `"4539 1488-0343 6467"` becomes `"4539148803436467"`.

- `digits = [int(d) for d in cleaned]`  
  Converts each character into an integer digit.  
  Example: `"4539"` becomes `[4, 5, 3, 9]`.

- `total = 0`  
  Initializes a running sum for the Luhn calculation.

- `for i in range(len(digits) - 1, -1, -1):`  
  Loops from the last digit to the first.  
  This is important because the Luhn rule doubles every **second** digit from the right.

- `digit = digits[i]`  
  Pulls out the current digit so it can be modified safely.

- `if (len(digits) - i) % 2 == 0:`  
  Checks whether this digit is in an even position **from the right**.  
  Example with length 16:  
  - Rightmost digit (i=15) → position 1 (odd) → not doubled  
  - Next digit (i=14) → position 2 (even) → doubled  

- `digit *= 2`  
  Doubles the digit when required.

- `if digit > 9: digit -= 9`  
  If doubling creates a two-digit number, subtract 9 to simulate summing its digits.  
  Example: `8 * 2 = 16` → `1 + 6 = 7` → `16 - 9 = 7`.

- `total += digit`  
  Adds the (possibly modified) digit into the running total.

- `return "VALID!" if total % 10 == 0 else "INVALID!"`  
  If the total is divisible by 10, the number passes the Luhn check.

## Step-by-Step Example (Valid)

Input: `"4539 1488 0343 6467"`  
Cleaned: `4539148803436467`

Process digits from right to left:

```
Digits: 4 5 3 9 1 4 8 8 0 3 4 3 6 4 6 7
Index : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

Rightmost position (from the right):
pos:   16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1
double? yes no yes no yes no yes no yes no yes no yes no yes no
```

Apply Luhn:

- Double digits in even positions from the right:
  - 6 → 12 → 3
  - 4 → 8
  - 6 → 12 → 3
  - 4 → 8
  - 8 → 16 → 7
  - 4 → 8
  - 9 → 18 → 9
  - 5 → 10 → 1

Sum all adjusted digits:

```
Total = 80
```

Since `80 % 10 == 0`, the function returns `"VALID!"`.

## Step-by-Step Example (Invalid)

Input: `"4539 1488 0343 6468"`  
This is the same as the valid example but with the last digit changed.

The total becomes `81`, and:

```
81 % 10 != 0
```

So the function returns `"INVALID!"`.
