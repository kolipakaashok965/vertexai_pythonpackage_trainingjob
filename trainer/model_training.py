
import pandas as pd
#import io
import gcsfs
#from google.cloud import storage  
from sklearn.linear_model import LinearRegression

def model_train():

    df = pd.read_csv('gs://qwiklabs-gcp-00-f078c97156ea-bucket/Real estate.csv')

    X_cols=set(df.columns.values)-set(['Y house price of unit area'])
    X_train=df[X_cols]
    Y=df['Y house price of unit area']
    reg = LinearRegression().fit(X_train, Y)

    model_filename = 'reg_model.joblib'
    return
