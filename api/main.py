from flask import Flask,request,Response
from spamapp.spam import SpamIdentify
from json import dumps,loads
app = Flask(__name__)

spam = SpamIdentify()

@app.route("/",methods=['GET'])
def home():
    return Response(response=dumps({"msg":"App successfull"}), status=200, mimetype='application/json')

@app.route("/spamapi/",methods=['GET','POST'])
def apicall():
    try:
        predTxt = loads(request.data)
        predTxt = predTxt['input']
        response = spam.predict_data(predTxt)
        return Response(response=dumps(response), status=200, mimetype='application/json')
    except Exception as e:
        print("Error",e)
        return Response(response=dumps({"result": 6}), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(
        host="192.168.2.240", 
        port=5000,
        debug=True
        )