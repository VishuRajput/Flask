from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index_1.html')


@app.route('/grade',methods=['POST'])
def grade_check():
    if(request.method == 'POST'):
        #chk = request.form['operation']
        num1 = int(request.form['num1'])
        if num1>90:
            result = "Student has passed with A+ grade."
        if num1>80 and num1<=90:
            result = "Student has passed with A grade."
        if num1>70 and num1<=80:
            result = "Student has passed with B+ grade."
        if num1>60 and num1<=70:
            result = "Student has passed with B grade."
        if num1>40 and num1<=60 :
            result = "Student has passed with C grade."
        if num1<40 :
            result = "Student has failed."
        
        return render_template('results_1.html' , result = result)

@app.route('/postman_data',methods=['POST'])
def grade_check_1():
    if(request.method == 'POST'):
        #chk = request.json['operation']
        num1 = int(request.json['num1'])
        if num1>90:
            result = "Student has passed with A+ grade."
        if num1>80 and num1<=90:
            result = "Student has passed with A grade."
        if num1>70 and num1<=80:
            result = "Student has passed with B+ grade."
        if num1>60 and num1<=70:
            result = "Student has passed with B grade."
        if num1>40 and num1<=60 :
            result = "Student has passed with C grade."
        if num1<40 :
            result = "Student has failed."
            
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")