from flask import Flask, request, render_template
import urllib
import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/aml', methods=['GET','POST'])
def aml():
    data = {
        "Inputs": {
          "input1": [
            {
              "Pregnancies": 0,
              "Glucose": request.values['p5'],
              "BloodPressure": request.values['p4'],
              "SkinThickness": 35,
              "Insulin": request.values['p6'],
              "BMI": request.values['p3'],
              "DiabetesPedigreeFunction": 2.288,
              "Age": request.values['p1'],
              "Outcome": 1
            }
          ]
        },
        "GlobalParameters": {

        }
      }
    body=str.encode(json.dumps(data))
    url='http://7ac69e26-f176-43dc-b695-668fd9800c4b.eastasia.azurecontainer.io/score'
    api_key='vtGt7uknpxFHb8P40n1AimaYMFvP2wdy'
    headers = {
        "Content-Type":"application/json",
        "Accept":"application/json",
        "Authorization":"Bearer " + api_key
    }

    req = urllib.request.Request(url,data,headers)

    htmlstr="<html><body>"

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        htmlstr=htmlstr+"依據您輸入的參數資料，經過決策模型比對，診斷糖尿病的結果為"

        if str(result['Results']['WebServiceOutput0'][0]['Scored Labels']) =='1.0':
            htmlstr+= ' 陽性</body></html>'
        else:
            htmlstr+= ' 陰性</body></html>'

    except urllib.error.HTTPError as error:
        print("The request failed with status  code:" + str(error.code))
        htmlstr+= '</body></html>'

    return htmlstr


@app.route('/about')
def about():
    return 'About'

if __name__=="__name__":
    app.run()