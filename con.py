from flask import Flask,request,make_response,render_template
import os,json
import requests
import bs4


app = Flask(__name__) 

@app.route('/news', methods =['POST', 'GET'])
def weather():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def processRequest(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    if parameters.get("news") :
    	url="https://coronaclusters.in/maharashtra/sangli#data"
        ds=requests.get(url)
        sp=bs4.BeautifulSoup(ds.text,'html.parser')
        s=[]
        for data in sp.find_all('h5'):
            d=data.text
            s.append(d)
        cases="Confirmed"+":"+s[0]+'\n'+"Acive"+":"+s[1]+'\n'+"Recoverd"+":"+s[2]+'\n'+"Deaths"+":"+s[3]
    return {
    		"fulfillmentText": cases
    		}
if __name__ == '__main__':
    app.run(debug = True) 
