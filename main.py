from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_origin
import pickle
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
scaler=StandardScaler()
@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('index.html')



@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            rm=float(request.form['RM'])
            age=float(request.form['AGE'])
            ym=float(request.form['YM'])
            rel=float(request.form['REL'])
            occ=float(request.form['OCC'])
            if age<ym:
                msg='Error while giving inputs please check that the age should be greater than years married'
                return render_template('error.html',msg=msg)
            filename='LR.pickle'
            loaded_model=pickle.load(open(filename,'rb'))
            prediction=loaded_model.predict([[rm,age,ym,rel,occ]])
            #print(prediction[0])
            #prediction=loaded_model.predict([[rm,ptratio,lstat]])
            #prediction=prediction
            print(prediction[0])
            if prediction[0]==0:
                ans='Can have no affair'
            else:
                ans='Can have an affair'
            #print('prediction is',prediction[0])
            return render_template('results.html',ans=ans)
        except Exception as e:
            print("Exception is",e)
            return 'Some error occured'
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)