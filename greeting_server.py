from concurrent import futures

import grpc
import greeting_pb2 as pb2
import greeting_pb2_grpc as pb2_grpc

class Greeter(pb2_grpc.GreeterServicer):
    def greet(self, request, context):
        print("Request Received : -- "+str(request))
        return pb2.ServerOutput(message='{0} {1}!'.format(request.greeting, request.name))

class DoTheMath(pb2_grpc.DoTheMathServicer):
    def domath(self, request, context):
        print(f'the request math received{str(request)}')
        total = request.number1+ request.number2
        print(total)
        return pb2.ServerOutput(total=total)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    pb2_grpc.add_DoTheMathServicer_to_server(DoTheMath(),server)
    server.add_insecure_port('[::]:50000')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()
server()