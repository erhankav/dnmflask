"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask,request,jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


@app.route('/predict' , methods=['POST'])
def predict():
    
     data=request.values;

     return json.dumps({'prediction': data})
     #X = np.empty((0,20,9))
     
     #dizi=request.args.get('dnm');
     
     #dizi=dizi.replace(" ",",")
     #dizi=dizi.replace("[,","[")
     #dnm=ast.literal_eval(dizi);
     #dnm=list(dnm)
     #npdizi=np.array(dnm)
     ##npdizi=pd.DataFrame(npdizi)
     #X = np.append(X, [npdizi], axis=0)
     #for i in range(X.shape[1]):
     #   X[:, i, :] = scalers[i].transform(X[:, i, :]) 
   

     #n_timesteps, n_features = X.shape[1], X.shape[2]
     #n_steps, n_length = 2, 10
     #X = X.reshape((X.shape[0], n_steps, n_length, n_features))
     #result=model.predict_classes(X).tolist()
     #return json.dumps({'prediction': result})
     ##return jsonify({'prediction': result.tolist()})
     ##return str(npdizi)
     ##return str(result)


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
