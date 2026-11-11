import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="A small welcome tool")
parser.add_argument("--name", required=True, help="Your first name")
args = parser.parse_args()

rows = [
    ["Welcome", f"Hello, {args.name}!"],
    ["Course", "Open Source Software"],
    ["Chapter", "Python Refresher"],
    ["Goal", "Learning to use open source libraries"],
]

print(tabulate(rows, headers=["Topic", "Information"], tablefmt="grid"))
