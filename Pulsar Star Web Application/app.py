from flask import Flask,request
from sklearn.linear_model import LogisticRegressionCV
from keras.models import Sequential
import numpy as np
import tensorflow as tf

# we are creating a variable which is the Flask application
app = Flask(__name__) 

from joblib import dump, load
loaded_lr = clf = load('lr_pulsarstar.joblib') 

from keras.models import model_from_json
# load json and create model
json_file = open('pulsarstar_nn.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("pulsarstar_nn.h5")
loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
graph = tf.get_default_graph()

@app.route('/predict_lr/<v1>/<v2>/<v3>/<v4>/<v5>/<v6>/<v7>/<v8>')
def predict_lr(v1,v2,v3,v4,v5,v6,v7,v8):
    return loaded_lr.predict([[float(v1),float(v2),float(v3),float(v4),float(v5),float(v6),float(v7),float(v8)]])[0]

@app.route('/predict_nn/<v1>/<v2>/<v3>/<v4>/<v5>/<v6>/<v7>/<v8>')
def predict_nn(v1,v2,v3,v4,v5,v6,v7,v8):
    global graph
    with graph.as_default():
        loaded_model.predict(np.array([[140,50,0.1,-0.9,4,20,5,90]]))
        nn_y = loaded_model.predict(np.array([[float(v1),float(v2),float(v3),float(v4),float(v5),float(v6),float(v7),float(v8)]]))[0]
        if nn_y[0] == 1:
            return 'Pulsar Star'
        else:
            return 'Not a Pulsar Star'

@app.route('/hello')
def hello():
    return 'Hello'

if __name__ =='__main__':
    app.run(debug=True)
