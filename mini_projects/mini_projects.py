"""Five mini-projects in one file. Run with --demo for a non-interactive demo,
or run plain and pick a project from the menu.
1 calculator, 2 number guessing, 3 password generator, 4 quiz, 5 contact book.
"""
import random, string, sys

def calculator(a, b):
    return {"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}

def guessing_game(secret, guesses):
    for g in guesses:
        if g == secret:
            yield f"Correct! The number was {secret}."
            return
        yield "Too low." if g < secret else "Too high."
    yield "Out of guesses."

def password_generator(length=12, seed=42):
    rng = random.Random(seed)
    chars = string.ascii_letters + string.digits + "!@#"
    return "".join(rng.choice(chars) for _ in range(length))

QUIZ = [("Python is a programming language. True or False?", "true"),
        ("2 + 2 = 5. True or False?", "false")]

def quiz(answers):
    return sum(1 for (_, correct), given in zip(QUIZ, answers)
               if given.lower() == correct)

class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add(self, name, phone):
        self.contacts[name] = phone
    def list_all(self):
        return self.contacts

def demo():
    print("1) Calculator 12 and 8:", calculator(12, 8))
    print("2) Guessing game, secret 7, guesses 3, 9, 7:")
    for hint in guessing_game(7, [3, 9, 7]):
        print("  ", hint)
    print("3) Password:", password_generator())
    print("4) Quiz score:", quiz(["true", "false"]), "/", len(QUIZ))
    book = ContactBook(); book.add("Shoaib", "0300-1234567")
    print("5) Contacts:", book.list_all())

if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        print("Run with --demo, or import the functions in your own code.")
        demo()
