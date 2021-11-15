from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import joblib
import numpy as np

app = Flask(__name__)
api = Api(app)


clf_path = 'modelos/model.pkl'
pipeline = joblib.load(clf_path)




class PredictClass(Resource):
    def get(self):
        # use parser and find the user's query
        # argument parsing
        parser = reqparse.RequestParser()
        parser.add_argument('query', action='append')
        parser = parser.parse_args()
        user_query = parser['query']
        user_query = [float(x) for x in user_query]
        prediction = pipeline.predict(np.array(user_query).reshape(1,-1))

        # Output either 'Negative' or 'Positive' along with the score
        if prediction == 0:
            pred_text = 'Este usuario NO ES propenso a dejar de pagar.'
        else:
            pred_text = 'Este usuario ES propenso a dejar de pagar.'
            
        # create JSON object
        output = {'prediction': pred_text}
        
        return output

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictClass, '/')


if __name__ == '__main__':
    app.run(debug=True)