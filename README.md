Homework docs
# Генераторы финансовых транзакций

Этот модуль использует генераторы Python для эффективной обработки больших наборов данных.

## Функции и примеры использования

### 1. filter_by_currency
Фильтрует транзакции по конкретной валюте.
```python
usd_transactions = filter_by_currency(transactions, "USD")