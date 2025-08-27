# 💳 Wallet API — FastAPI test project

### Тестовое задание
### С частичной имплементацией DDD

---

## Задача: имитация wallet api

- принимает входящие на кошелек операции
- изменяет баланс кошелька в соответствии с операцией
- возвращает баланс кошелька

---


## Стек:
- Python 3.12
- FastAPI
- Pydantic v2
- SQLAlchemy
- asyncpg

---

## GET `/docs`

Документация SwaggetUI

## POST `/api/v1/wallets/{wallet_id}/operation`

Принимает JSON следующего формата:

```json
{
    "operation_type": "DEPOSIT or WITHDRAW",
    "amount": 1000.00
}
```
### Поведение

- Если кошелек с указанным id существует:
  - создаёт `Operation`
  - начисляет сумму на баланс кошелька

Возвращает обработанную операцию

```json
{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "operation_type": "deposit",
    "amount": "string",
    "wallet_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

---

## GET `/api/v1/wallets/{wallet_id}/`

Возвращает текущий баланс кошелька по id:

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "balance": 145000.32
}
```