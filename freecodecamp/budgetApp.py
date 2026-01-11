"""Budget App: Category class and spend chart."""


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
