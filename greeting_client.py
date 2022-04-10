import grpc

import greeting_pb2 as pb2
import greeting_pb2_grpc as pb2_grpc

def run():
   with grpc.insecure_channel('localhost:50000') as channel:
      stub = pb2_grpc.GreeterStub(channel)
      response = stub.greet(pb2.ClientInput(name='John', greeting = "Yo"))
   print("Greeter client received following from server: " + response.message)   
run()