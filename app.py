## flask app routing
from flask import Flask,render_template,request,redirect,url_for,jsonify




# create a simple flask application
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return 'welcome to the hindi channel'


@app.route("/index",methods=["GET"])
def index():
    return 'welcome to the index page'

## variable rule
@app.route('/success1/<int:score>')
def succcess(score):
    return "the person has passed and the scored is  : "+str(score)


@app.route('/success/<int:score>')
def fail(score):
    return "the person has failed and the scored is  : "+str(score)


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result=""
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        return redirect(url_for(result,score=average_marks))

        #return render_template('form.html',score=average_marks)


@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)


if (__name__)=="__main__":
    app.run(debug=True)

