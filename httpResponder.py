from flask import Flask
from flask import request
from flask import Response
app = Flask(__name__)

#Fetching configs.
try:
    with open("config.txt","r") as configFile:
        configData = configFile.readlines()
        hostRAW = str(configData[1])
        portRAW = configData[4]
        hostToUse = hostRAW[5:]
        portToUse = int(portRAW[5:])
except Exception:
    raise

@app.route('/endpoint1', methods = ['POST'])
# Handling incoming endpoint 1 messages
# Saving incoming messages into a file.
# The file is wiped each time a message is accepted.
def endpoint1():
    with open("messages/endpoint1_MESSAGE.txt","w+") as end1:
        end1Data = str(request.data)
        end1.write(end1Data)
    with open("responses/endpoint1_RESPONSE.txt","r") as end1RespFile:
        end1Response = end1RespFile.read()
    resp = Response(end1Response,200,{'Content-Type': 'application/json'})
    return resp

@app.route('/endpoint2', methods = ['POST'])
def endpoint2():
    with open("messages/endpoint2_MESSAGE.txt","w+") as end2:
        end2Data = str(request.data)
        end2.write(end2Data)
    with open("responses/endpoint2_RESPONSE.txt","r") as end2RespFile:
        end2Response = end2RespFile.read()
    resp = Response(end2Response,200,{'Content-Type': 'application/json'})
    return resp

@app.route('/endpoint3', methods = ['POST'])
def endpoint3():
    with open("messages/endpoint3_MESSAGE.txt","w+") as end3:
        end3Data = str(request.data)
        end3.write(end3Data)
    with open("responses/endpoint3_RESPONSE.txt","r") as end3RespFile:
        end3Response = end3RespFile.read()
    resp = Response(end3Response,200,{'Content-Type': 'application/json'})
    return resp

if __name__ == '__main__':
    app.run(host=hostToUse, port=portToUse, debug=True, use_reloader = False)