import logging
from transaction_service.app.proto import transaction_pb2 as pb2
from transaction_service.app.proto import transaction_pb2_grpc as pb2_grpc
from .database import SessionLocal
from .models import Transaction

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TransactionService(pb2_grpc.TransactionServiceServicer):
    def __init__(self):
        self.db = SessionLocal()

    def AddTransaction(self, request, context):
        txn = Transaction(
            user_id=request.user_id,
            category=request.category,
            amount=request.amount,
            type=request.type,
            date=request.date
        )
        self.db.add(txn)
        self.db.commit()
        logging.info(f"Added transaction for user_id={request.user_id}, amount={request.amount}, category={request.category}")
        return pb2.TransactionResponse(status="200", message="Transaction added")

    def GetTransactions(self, request, context):
        txns = self.db.query(Transaction).filter(Transaction.user_id == request.user_id).all()
        logging.info(f"Fetched {len(txns)} transactions for user_id={request.user_id}")
        txn_list = [pb2.Transaction(
            id=t.id,
            category=t.category,
            amount=t.amount,
            type=t.type,
            date=t.date
        ) for t in txns]
        return pb2.TransactionList(transactions=txn_list)

    def UpdateTransaction(self, request, context):
        txn = self.db.get(Transaction, request.id)
        if not txn:
            logging.warning(f"Update failed: Transaction with id={request.id} not found")
            return pb2.TransactionResponse(status="404", message="Not found")

        txn.category = request.category
        txn.amount = request.amount
        txn.type = request.type
        self.db.commit()
        logging.info(f"Updated transaction id={request.id} to amount={request.amount}, category={request.category}")
        return pb2.TransactionResponse(status="200", message="Updated")

    def DeleteTransaction(self, request, context):
        txn = self.db.get(Transaction, request.id)
        if txn:
            self.db.delete(txn)
            self.db.commit()
            logging.info(f"Deleted transaction id={request.id}")
            return pb2.TransactionResponse(status="200", message="Deleted")

        logging.warning(f"Delete failed: Transaction with id={request.id} not found")
        return pb2.TransactionResponse(status="404", message="Not found")
