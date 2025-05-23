import logging
import grpc
from proto import transaction_pb2 as pb2
from proto import transaction_pb2_grpc as pb2_grpc
from database import SessionLocal
from models import Transaction
from producer import publish_transaction  # ✅ Make sure this import works

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TransactionService(pb2_grpc.TransactionServiceServicer):
    def __init__(self):
        self.db = SessionLocal()

    def AddTransaction(self, request, context):
        try:
            txn = Transaction(
                user_id=request.user_id,
                category=request.category,
                amount=request.amount,
                type=request.type,
                date=request.date
            )
            self.db.add(txn)
            self.db.commit()
            
            # ✅ Publish to RabbitMQ
            publish_transaction({
                "user_id": request.user_id,
                "category": request.category,
                "amount": request.amount,
                "type": request.type,
                "date": request.date
        })

            logging.info(f"✅ Added transaction for user_id={request.user_id}, amount={request.amount}, category={request.category}")
            return pb2.TransactionResponse(status="200", message="Transaction added")
        except Exception as e:
            self.db.rollback()
            logging.error(f"❌ AddTransaction failed: {e}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return pb2.TransactionResponse(status="500", message="Failed to add")

    def GetTransactions(self, request, context):
        try:
            txns = self.db.query(Transaction).filter(Transaction.user_id == request.user_id).all()
            logging.info(f"📄 Fetched {len(txns)} transactions for user_id={request.user_id}")
            txn_list = [pb2.Transaction(
                id=t.id,
                category=t.category,
                amount=t.amount,
                type=t.type,
                date=t.date
            ) for t in txns]
            return pb2.TransactionList(transactions=txn_list)
        except Exception as e:
            self.db.rollback()
            logging.error(f"❌ GetTransactions failed: {e}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return pb2.TransactionList()

    def UpdateTransaction(self, request, context):
        try:
            txn = self.db.get(Transaction, request.id)
            if not txn:
                logging.warning(f"⚠️ Update failed: Transaction with id={request.id} not found")
                return pb2.TransactionResponse(status="404", message="Not found")

            txn.category = request.category
            txn.amount = request.amount
            txn.type = request.type
            self.db.commit()
            logging.info(f"✏️ Updated transaction id={request.id} to amount={request.amount}, category={request.category}")
            return pb2.TransactionResponse(status="200", message="Updated")
        except Exception as e:
            self.db.rollback()
            logging.error(f"❌ UpdateTransaction failed: {e}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return pb2.TransactionResponse(status="500", message="Failed to update")

    def DeleteTransaction(self, request, context):
        try:
            txn = self.db.get(Transaction, request.id)
            if txn:
                self.db.delete(txn)
                self.db.commit()
                logging.info(f"🗑️ Deleted transaction id={request.id}")
                return pb2.TransactionResponse(status="200", message="Deleted")

            logging.warning(f"⚠️ Delete failed: Transaction with id={request.id} not found")
            return pb2.TransactionResponse(status="404", message="Not found")
        except Exception as e:
            self.db.rollback()
            logging.error(f"❌ DeleteTransaction failed: {e}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return pb2.TransactionResponse(status="500", message="Failed to delete")
