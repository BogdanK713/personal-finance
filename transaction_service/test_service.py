import pytest
from unittest.mock import MagicMock

from transaction_service.app.service import TransactionService
from transaction_service.app.proto import transaction_pb2
from transaction_service.app.models import Transaction


@pytest.fixture
def service():
    service_instance = TransactionService()
    # Reset DB before each test to avoid side effects
    service_instance.db.query(Transaction).delete()
    service_instance.db.commit()
    return service_instance


def test_add_transaction(service):
    request = transaction_pb2.TransactionRequest(
        user_id="user1",
        amount=100.0,
        category="Food",
        type="Expense",
        date="2025-03-22"
    )
    context = MagicMock()
    response = service.AddTransaction(request, context)

    assert response.message == "Transaction added"


def test_get_transactions(service):
    add_request = transaction_pb2.TransactionRequest(
        user_id="user2",
        amount=50.0,
        category="Transport",
        type="Expense",
        date="2025-03-22"
    )
    context = MagicMock()
    service.AddTransaction(add_request, context)

    get_request = transaction_pb2.UserRequest(user_id="user2")
    response = service.GetTransactions(get_request, context)

    # Match specific added transaction
    matches = [
        txn for txn in response.transactions
        if txn.amount == 50.0 and txn.category == "Transport"
    ]

    assert len(matches) >= 1


def test_update_transaction(service):
    context = MagicMock()

    add_request = transaction_pb2.TransactionRequest(
        user_id="user3",
        amount=75.0,
        category="Bills",
        type="Expense",
        date="2025-03-22"
    )
    service.AddTransaction(add_request, context)

    transaction_id = service.db.query(Transaction).order_by(Transaction.id.desc()).first().id

    update_request = transaction_pb2.UpdateRequest(
        id=transaction_id,
        amount=90.0,
        category="Utilities",
        type="Expense"
    )
    response = service.UpdateTransaction(update_request, context)

    assert response.message == "Updated"

    updated = service.db.get(Transaction, transaction_id)
    assert updated.amount == 90.0
    assert updated.category == "Utilities"


def test_delete_transaction(service):
    context = MagicMock()

    add_request = transaction_pb2.TransactionRequest(
        user_id="user4",
        amount=30.0,
        category="Snacks",
        type="Expense",
        date="2025-03-22"
    )
    service.AddTransaction(add_request, context)

    transaction_id = service.db.query(Transaction).order_by(Transaction.id.desc()).first().id

    delete_request = transaction_pb2.DeleteRequest(id=transaction_id)
    delete_response = service.DeleteTransaction(delete_request, context)

    assert delete_response.message == "Deleted"

    deleted = service.db.get(Transaction, transaction_id)
    assert deleted is None
