from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index_2.html')


@app.route('/subject',methods=['POST'])
def grade_check():
    if(request.method == 'POST'):
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])

        tot = round((((num1+num2+num3)/300)*100),2)

        if tot>90:
            result = "Student has got " + str(tot) + "%" + " and passed with A+ grade."
        if tot>80 and tot<=90:
            result = "Student has got " + str(tot) + "%" + " and passed with A grade."
        if tot>70 and tot<=80:
            result = "Student has got " + str(tot) + "%" + " and passed with B+ grade."
        if tot>60 and tot<=70:
            result = "Student has got " + str(tot) + "%" + " and passed with B grade."
        if tot>40 and tot<=60 :
            result = "Student has got " + str(tot) + "%" + " and passed with C grade."
        if tot<40 :
            result = "Student has got " + str(tot) + "%" + " and failed."
        
        return render_template('results_1.html' , result = result)

@app.route('/postman_data',methods=['POST'])
def grade_check_1():
    if(request.method == 'POST'):
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        num3 = int(request.json['num3'])

        tot = round((((num1+num2+num3)/300)*100),2)

        if tot>90:
            result = "Student has got " + str(tot) + "%" + " and passed with A+ grade."
        if tot>80 and tot<=90:
            result = "Student has got " + str(tot) + "%" + " and passed with A grade."
        if tot>70 and tot<=80:
            result = "Student has got " + str(tot) + "%" + " and passed with B+ grade."
        if tot>60 and tot<=70:
            result = "Student has got " + str(tot) + "%" + " and passed with B grade."
        if tot>40 and tot<=60 :
            result = "Student has got " + str(tot) + "%" + " and passed with C grade."
        if tot<40 :
            result = "Student has got " + str(tot) + "%" + " and failed."
            
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")