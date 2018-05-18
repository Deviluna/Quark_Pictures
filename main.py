from flask import Flask,render_template
import os
# -- coding: utf-8 --

app=Flask(__name__)

@app.route("/")
def index():
    pic_folder="static/pictures/"
    pic_list=os.listdir(pic_folder)
    pic_str=""
    
    for item in pic_list:
        pic_str+="<img src='"+pic_folder+item+"' align='center'/><br>"+os.path.basename(item)+"<br>"
        
    return render_template('Quark_index.htm')+pic_str



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
