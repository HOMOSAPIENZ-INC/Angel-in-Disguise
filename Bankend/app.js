import pickle
import ssl
from pymongo import MongoClient
import sklearn
from flask import Flask, render_template, request,jsonify,url_for
app=Flask(__name__)

client = MongoClient("mongodb+srv://himu:himu@cluster0.qkmvt.mongodb.net/students?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db=client["students"]

@app.route('/',methods=['POST'])
def from_student():
    if request.method=='POST':
        req_data = request.get_json()
        srn=req_data["srn"]
        id=req_data["_id"]
        print(id)
        sleephours=int(req_data["sleephours"])
        activity=int(float(req_data["activity"]))
        studyhours=int(req_data["studyhours"])
        classhours=int(req_data["classhours"])
        model = pickle.load(open('/Users/jacksonsunny/Downloads/mdl.pkl', 'rb'))
        res=model.predict([[sleephours,classhours,studyhours,activity]])
        collection=db[srn]
        myquery = { "_id": id }
        newvalues = { "$set": { "performance":res[0] } }
        result=collection.update_one(myquery,newvalues)
        print(res[0])

        return "Done"

if __name__ == '__main__':
    app.run(port=5001)
