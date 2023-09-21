import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

tranform_factors = {'Feature 1': [295.3, 304.4], 'Feature 2': [305.7, 313.7], 'Feature 3': [1181.0, 2825.0], 'Feature 4': [5.8, 75.4], 'Feature 5': [0.0, 251.0]}

def transform_test_data(ip_data):
  column_names = ['Type', 'Feature 1', 'Feature 2', 'Feature 3', 'Feature 4', 'Feature 5']
  if ip_data[0] == 'H':
    ip_data[0] = 0
  elif ip_data[0] == 'M':
    ip_data[0] = 2
  else:
    ip_data[0] = 1
  for i in range(1,len(ip_data)):
    ip_data[i] = (ip_data[i] - tranform_factors[column_names[i]][0])/(tranform_factors[column_names[i]][1] - tranform_factors[column_names[i]][0])
  df = pd.DataFrame([ip_data], columns=column_names)
  return df

def get_prediction_cpuid(data):
    converted_data = []
    for i in range(1,len(data)-2):
        if i < 2:
            converted_data.append(data[i])
        else:
            converted_data.append(float(data[i]))
    df = transform_test_data(converted_data)
    return load_predict(df)

def load_predict(df):
    pickled_model = pickle.load(open('./models/gbmodel.pkl', 'rb'))
    output = pickled_model.predict(df)
    return output[0]