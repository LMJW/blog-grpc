import grpc

import test_pb2
import test_pb2_grpc

x = dict(pttransactionID = 'abcde',
    ptproperties = 'This is a plain text transaction',
    ptsenderID = 'Will smith')
def run():
    channel = grpc.insecure_channel('localhost:22222')
    stub = test_pb2_grpc.EncodeServiceStub(channel)
    response = stub.GetEncode(test_pb2.plaintext(**x))
    print("Encdded service received:\n EnctransactionID:%s\n,Encproperties:%s\n,EncsenderID:%s\n"%(response.enctransactionID,response.encproperties,response.encsenderID))

if __name__ == "__main__":
    run()
