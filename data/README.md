# Данные

Ожидаемый файл: `FraudShield_Banking_Data.csv`.

Исходный набор был доступен по адресу:
`https://www.kaggle.com/datasets/algozee/financial-transaction-fraud-dataset`.

На 4 сентября 2026 года публичная страница набора недоступна, а связанные Kaggle-ноутбуки показывают источник как private dataset. Поэтому CSV не включён в проект и не скачивается автоматически.

## Ожидаемая схема

```text
Transaction_ID
Customer_ID
Merchant_ID
Device_ID
IP_Address
Transaction_Date
Transaction_Time
Transaction_Location
Customer_Home_Location
Transaction_Type
Merchant_Category
Card_Type
Is_International_Transaction
Is_New_Merchant
Unusual_Time_Transaction
Transaction_Amount (in Million)
Distance_From_Home
Account_Balance (in Million)
Daily_Transaction_Count
Weekly_Transaction_Count
Avg_Transaction_Amount (in Million)
Max_Transaction_Last_24h (in Million)
Failed_Transaction_Count
Previous_Fraud_Count
Fraud_Label
```

Ожидаемые значения `Fraud_Label`: `Normal`, `Fraud` и, согласно статье, четыре пропуска.

Перед запуском ноутбука проверьте файл:

```bash
python scripts/validate_dataset.py data/FraudShield_Banking_Data.csv
```

Не используйте как прямую замену `financial_transactions.csv` из набора `ziya07/financial-transaction-dataset-for-risk-prediction`: его структура не соответствует этому исследованию.

