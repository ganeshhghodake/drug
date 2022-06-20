from flask import Flask,request,render_template
import pickle as pkl

model = pkl.load(open('drug_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def prediction():
    return render_template('index.html')

@app.route('/result',methods=["post"])
def result ():
    var_age = int(request.form.get("agee"))
    var_sex = int(request.form.get('sex'))
    var_bp = int(request.form.get('bp'))
    var_chol = int(request.form.get('chol'))
    var_na = float(request.form.get('na'))

    test = model.predict([[var_age,var_sex,var_bp,var_chol,var_na]])
    if test[0] == 1:
        return "drugy"
    elif test[0] == 2:
        return "drugx"
    elif test[0] == 3:
        return "druga"
    elif test[0] == 4:
        return "drugc"
    else :
        return "drugb"

if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0' , port='8080')