#!/usr/bin/env python

#import necessary libraries
# pip install flask 
#export FLASK_APP=flask-app
#flask run
from flask import Flask, json, flash,render_template, session,request,jsonify,redirect, url_for
import os
import pandas as pd
pd.set_option('display.max_columns',15)

#create instance of Flask app
app = Flask(__name__)

#decorator 
@app.route("/")
def echo_hello():
    return "<p>Hello Nobel.json!!!!!</p>"

@app.route("/all")
def nobel():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    return render_template('index.html',data=data_json)


@app.route("/<year>",methods=["GET","POST"])
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']

    if request.method == "GET":
        output_data = [x for x in data if x['year']==year]
        return render_template('user_nobel.html',data=output_data)

    elif request.method == "POST":
        category = request.form['category']
        id=request.form["id"]
        firstname=request.form['firstname']
        surname=request.form['surname']
        motivation=request.form['motivation']
        share=request.form['share']
        create_row_data= {'year': year, 'category': category, 'laureates': [{'id': id, 'firstname': firstname, 'surname': surname,'motivation': motivation, 'share': share}]}
        print (create_row_data)
        filename='./static/nobel.json'
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data['prizes'].append(create_row_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        
        return render_template('user_nobel.html',data=create_row_data)
       

if __name__ == "__main__":
    app.run(debug=True)