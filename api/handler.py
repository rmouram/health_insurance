import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurante import HealthInsurance

# loading model
path = '/home/romulo/Documentos/health_insurance/health_insurance/'
model = pickle.load ( open(path + 'models/model_linear_regression.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json:
        if isinstance(test_json, dict): #unique exemple
            test_raw = pd.DataFrame(test_json, index=[0])
        else: #multiple exemple
            test_raw = pd.DatFrame(test_json, columns=test_json[0].keys())
    
        pipeline = HealthInsurance()
        
        df1 = pipeline.data_cleaning(test_raw)
        df2 = pipeline.feaure_engineering(df1)
        df3 = pipeline.data_preparation(df2)
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response

    else:
        return Response( '{}', status=200, mimetype='application/json' )
    
if __name__ == '__main__':
    app.run( '0.0.0.0', debug=True )
