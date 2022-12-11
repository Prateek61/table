import csv

from typing import List

def write_to_csv(rows: List[dict]) -> None:
    with open('table.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
