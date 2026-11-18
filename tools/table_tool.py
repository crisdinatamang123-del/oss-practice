
import argparse
import pandas as pd
from pathlib import Path
from rich.console import Console
from rich.table import Table

parser = argparse.ArgumentParser(
    description="Filter server data and export to Excel"
)
parser.add_argument("csv_path", help="Path to CSV file")
args = parser.parse_args()

# Read CSV file
df = pd.read_csv(args.csv_path)

# Custom filter: Servers in Seoul or Daejeon with at least 64 GB memory
filtered_df = df[
    (df["location"].isin(["Seoul", "Daejeon"])) &
    (df["memory_gb"] >= 64)
]

# Create Rich table
table = Table(title="Selected High-Memory Servers")

for column in filtered_df.columns:
    table.add_column(column)

for _, row in filtered_df.iterrows():
    table.add_row(*[str(value) for value in row])

# Display table
console = Console()
console.print(table)

# Export to Excel
output_path = Path(args.csv_path).with_name("filtered_servers.xlsx")
filtered_df.to_excel(output_path, index=False)

print(f"Saved {output_path}")

