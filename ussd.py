from flask import Flask
from flask import request
from flask import make_response
import random

app = Flask(__name__)



@app.route('/api/ussd/callback', methods=['POST', 'GET'])
def ussd_callback():
    session_id      = request.values.get("sessionId", None)
    serviceCode     = request.values.get("serviceCode", None)
    phoneNumber     = request.values.get("phoneNumber", None)
    text            = request.values.get("text", None)

    texttoarray     = text.split('*')
    userResponse    = texttoarray[-1]
    
    #serve menus based on text
    if text == "":
        menu_text = "CON Welcome to KPLC prepaid, please choose an option:\n"
        menu_text += "1. Check my Account information\n"
        menu_text += "2. Top-Up my balance\n"
      
    elif text =="1":
        menu_text = "CON Choose the account information that you want to view \n"
        menu_text += "1. My Token balance\n"
        menu_text += "2. My Account number \n"

    elif text =="2":
        menu_text = "CON Please enter the amount"
            
    elif text =="1*1":
        token = random.randrange(16,38)
        menu_text = "END Your Token balance is: "+ str(token)
        
    elif text =="1*2":
        menu_text = "END Your account number is ACOO10SWO2101."
    
    elif text =="2*"+userResponse:
        send_sms("Thank you the amount paid in is: ", userResponse)
        menu_text = "END Thank-you"
    
    resp = make_response(menu_text, 200)
    resp.headers['Content-Type'] = "text/plain"
    return resp


if __name__ == "__main__":
        app.run()