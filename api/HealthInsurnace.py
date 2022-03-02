import pickle
import pandas as pd
import numpy as np

class HealthInsurance:
    def __init__(self):
        self.home_path = '/home/romulo/Documentos/health_insurance/health_insurance/'
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl'))
        self.age_scaler = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl'))
        self.gender_premium_scaler = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl'))
        self.policy_sales_channel_scaler = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl'))
        self.region_code_scaler = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl'))
        self.vintage_scaler = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl'))
        
    def data_cleaning(self, df1):
        cols_old = ['id', 'Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage', 'Response']
        snakecase = lambda x: inflection.underscore(x)
        cols_new = list(map(snakecase, cols_old))
        # rename
        df1.columns = cols_new
        
        return df1

    def feaure_engineering(self, df2):
        # vehicle age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_and_2_year' if x == '1-2 Year' else 'below_1_year')
        # vehicle demage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        return df2
    
    def data_preparation(self, df5):
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5[['annual_premium']].values)      
        df5['age'] = self.age_scaler.transform(df5[['age']].values)
        df5['vintage'] = self.vintage_scaler.transform(df5[['vintage']].values)

        # gender -- Target Encoding
        df5.loc[:,'gender'] = df5['gender'].map(self.target_encode_gender_scaler)

        # region_code -- Target encoding
        df5.loc[:, 'region_code'] = df5['region_code'].map(self.target_encode_region_code_scaler)

        # vehicle_age -- One Hot Encoding / Order Encoding
        df5 = pd.get_dummies(df5, prefix='vehicle_age', columns=['vehicle_age'])

        # policy_sales_channel -- Frequency encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map(self.policy_sales_channel_scaler)
        
        # Feature Selection
        cols_selected = ['vintage','annual_premium','age','region_code','vehicle_damage', 'policy_sales_channel', 'previously_insured']
        
        return df5[ cols_selected ]
    
    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )
        
        # join prediction into original data
        original_data['prediction'] = pred
        
        return original_data.to_json( orient='records', date_format='iso' )
