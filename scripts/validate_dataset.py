#!/usr/bin/env python3
"""Validate the FraudShield CSV before running the research notebook."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


EXPECTED_COLUMNS = {
    "Transaction_ID",
    "Customer_ID",
    "Merchant_ID",
    "Device_ID",
    "IP_Address",
    "Transaction_Date",
    "Transaction_Time",
    "Transaction_Location",
    "Customer_Home_Location",
    "Transaction_Type",
    "Merchant_Category",
    "Card_Type",
    "Is_International_Transaction",
    "Is_New_Merchant",
    "Unusual_Time_Transaction",
    "Transaction_Amount (in Million)",
    "Distance_From_Home",
    "Account_Balance (in Million)",
    "Daily_Transaction_Count",
    "Weekly_Transaction_Count",
    "Avg_Transaction_Amount (in Million)",
    "Max_Transaction_Last_24h (in Million)",
    "Failed_Transaction_Count",
    "Previous_Fraud_Count",
    "Fraud_Label",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    path = args.csv_path.expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"Файл не найден: {path}")

    label_counts: dict[str, int] = {}
    row_count = 0
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = sorted(EXPECTED_COLUMNS - columns)
        if missing:
            raise SystemExit("Не хватает столбцов: " + ", ".join(missing))

        for row in reader:
            row_count += 1
            label = (row.get("Fraud_Label") or "<missing>").strip() or "<missing>"
            label_counts[label] = label_counts.get(label, 0) + 1

    unexpected = sorted(set(label_counts) - {"Normal", "Fraud", "<missing>"})
    if unexpected:
        raise SystemExit("Неожиданные значения Fraud_Label: " + ", ".join(unexpected))

    print(f"Файл: {path}")
    print(f"Строк: {row_count:,}")
    print(f"Столбцов: {len(columns)}")
    print(f"Fraud_Label: {label_counts}")
    if row_count != 50_000:
        print("Предупреждение: в статье описан набор из 50 000 строк.")
    print("Схема совместима с ноутбуком.")


if __name__ == "__main__":
    main()

