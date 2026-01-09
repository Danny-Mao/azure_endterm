from flask import Flask, request, render_template
import urllib
import json
import math

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
                    "Column1": 5,
                    "SeriousDlqin2yrs": 0,
                    "RevolvingUtilizationOfUnsecuredLines": 3,
                    "age": int(request.values["age"]),
                    "NumberOfTime30-59DaysPastDueNotWorse": 1,
                    "DebtRatio": float(request.values["deb"]),
                    "MonthlyIncome": request.values["mon"],
                    "NumberOfOpenCreditLinesAndLoans": 7,
                    "NumberOfTimes90DaysLate": int(request.values["num"]),
                    "NumberRealEstateLoansOrLines": 1,
                    "NumberOfTime60-89DaysPastDueNotWorse": 0,
                    "NumberOfDependents": "0"
                }
            ]
        },
        "GlobalParameters": {

        }
    }
    #return data
    body=str.encode(json.dumps(data))
    url='http://77efcf34-05ee-46a8-80e6-2a68fdc8e7a8.eastasia.azurecontainer.io/score'
    api_key='GKyjGkdxUchwKxkVWXb0SE6LUekM2FqB'
    headers = {
        "Content-Type":"application/json",
        "Accept":"application/json",
        "Authorization":"Bearer " + api_key
    }

    req = urllib.request.Request(url,body,headers)

    htmlstr="<html><body>"

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        htmlstr += str(result)
        htmlstr=htmlstr+"<p>依據您輸入的參數資料，經過決策模型比對：</p>"
        htmlstr += "違約風險類別為 "
        '''
        if str(result['Results']['WebServiceOutput0'][0]['Scored Labels']) =='1.0':
            htmlstr+= ' 陽性</body></html>'
        else:
            htmlstr+= ' 陰性</body></html>' 
        '''

    except urllib.error.HTTPError as error:
        print("The request failed with status  code:" + str(error.code))
        htmlstr+= '</body></html>'

    #return htmlstr


@app.route('/about')
def about():
    return 'About'

if __name__=="__name__":
    app.run()