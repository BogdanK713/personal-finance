from concurrent import futures
import grpc
from transaction_service.app.proto import transaction_pb2_grpc as pb2_grpc
from transaction_service.app.service import TransactionService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    server.add_insecure_port("[::]:50051")
    print("Transaction gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
