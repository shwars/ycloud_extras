from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
from flask import Flask, request
import os, io

configure_credentials(yandex_credentials=creds.YandexCredentials(api_key=os.environ['api_key']))
app = Flask(__name__)

def synth(txt,voice,role,speed):
    model = model_repository.synthesis_model()
    model.voice = voice
    if role:
        model.role = role
    model.speed = speed
    model.unsafe_mode = True
    result = model.synthesize(txt,raw_format=False)
    return result

@app.route('/speak',methods=['GET','POST'])
def speak_request():
    if request.method=='POST':
        dic = request.json
    else: # GET
        dic = request.args
    res = synth(dic.get('text'),dic.get('voice','jane'),dic.get('role',None),dic.get('speed',1.0))
    bytes = io.BytesIO()
    res.export(bytes,format='mp3')
    #resp = make_response(bytes)
    return bytes

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
