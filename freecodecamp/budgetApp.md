# Budget App: Category Class (and Spend Chart)

This write-up covers the `Category` class requested in the user stories. At the end, there is an optional `create_spend_chart` function that generates the percentage graph mentioned in the prompt.

## Category Class (Meets the User Stories)

```python
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}"
        lines = [title]
        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            lines.append(f"{desc:<23}{amount:>7}")
        lines.append(f"Total: {self.get_balance()}")
        return "\n".join(lines)
```

## Method-by-Method Explanation

### `__init__(self, name)`
- Stores the category name.
- Creates `ledger` as an empty list, which will hold transaction dictionaries.

Example:
- `food = Category("Food")`
- `food.ledger` starts as `[]`.

### `deposit(self, amount, description="")`
- Adds a transaction with a positive amount.
- Uses the dictionary format required by the tests.

Example:
- `food.deposit(1000, "initial deposit")`
- Ledger becomes:
  - `{"amount": 1000, "description": "initial deposit"}`

### `withdraw(self, amount, description="")`
- Checks funds first.
- Stores the withdrawal as a negative amount.
- Returns `True` if it succeeds, `False` otherwise.

Example:
- `food.withdraw(15.25, "groceries")`
- Adds:
  - `{"amount": -15.25, "description": "groceries"}`

### `get_balance(self)`
- Sums all amounts in the ledger to get the current balance.

Example:
- Deposits `100`, withdraws `30` → balance is `70`.

### `transfer(self, amount, category)`
- Uses `check_funds` to verify balance.
- Withdraws from the source with description `Transfer to [Destination]`.
- Deposits into the destination with description `Transfer from [Source]`.

Example:
- `food.transfer(10, entertainment)` produces:
  - Food ledger: `{"amount": -10, "description": "Transfer to Entertainment"}`
  - Entertainment ledger: `{"amount": 10, "description": "Transfer from Food"}`

### `check_funds(self, amount)`
- Returns `True` if the balance is enough, `False` otherwise.
- This method is used by both `withdraw` and `transfer`.

### `__str__(self)`
- Builds the formatted output required by the tests.
- Title is centered in 30 characters with `*` padding.
- Each ledger line shows a left-aligned description (max 23 chars) and a right-aligned amount (2 decimals, max 7 chars).
- Ends with `Total: [balance]`.

Example output:

```
*************Food*************
initial deposit        1000.00
groceries               -15.25
Total: 984.75
```

## Example Usage

```python
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.transfer(50, clothing)

print(food)
print(clothing)
```

## Optional: Spend Chart (Percentage Graph)

If you need the percentage graph, use this helper. It calculates total spent per category and formats the chart in 10% increments.

```python
def create_spend_chart(categories):
    spent = []
    total_spent = 0

    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += -item["amount"]
        spent.append(category_spent)
        total_spent += category_spent

    percentages = [
        int((amount / total_spent) * 100) // 10 * 10 for amount in spent
    ]

    lines = ["Percentage spent by category"]
    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for percent in percentages:
            line += "o  " if percent >= level else "   "
        lines.append(line)

    lines.append("    " + "-" * (len(categories) * 3 + 1))

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return "\n".join(lines)
```
