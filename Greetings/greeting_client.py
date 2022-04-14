import grpc

import greeting_pb2 as pb2
import greeting_pb2_grpc as pb2_grpc


def greetings(i_name, i_surname):
   with grpc.insecure_channel('localhost:50000') as channel:
      stub = pb2_grpc.GreeterStub(channel)
      response = stub.greet(pb2.ClientInput(name=i_name, greeting = i_surname))
   print("Greeter client received following from server: " + response.message)   

def mainMath(i_num1,i_num2):
   with grpc.insecure_channel('localhost:50000') as channel:
      stub = pb2_grpc.DoTheMathStub(channel)
      response =stub.domath(pb2.MathInput(number1=float(i_num1),number2=float(i_num2)))
      print(str(response.total))

print("Hi Welcome Client")
name =input("Name Please: \n")
surname = input("Surname Please: \n")
greetings(name,surname)
print('\n')
print('\n')
print("Do the math")
num1 =input ('Number 1\n')
num2 =input ('Number 2\n')
mainMath(num1,num2)