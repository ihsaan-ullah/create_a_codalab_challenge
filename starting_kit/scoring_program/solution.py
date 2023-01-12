import os
from os.path import isfile
import numpy as np
import pandas as pd
import json
from sklearn.model_selection import train_test_split


# ================ Small auxiliary functions =================

def read_solutions(data_dir):
    ''' Function to read the Labels from CSV files'''


    #----------------------------------------------------------------
    # Settings
    #----------------------------------------------------------------
    JSON_PATH = os.path.join(data_dir,"info.json")
    CSV_PATH = os.path.join(data_dir,"labels.csv")
    
    #Check JSON file
    if not os.path.isfile(JSON_PATH):
        print('[-] JSON file Not Found')
        print('Make sure your dataset is in this format: https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat')
        return

    #Check CSV file
    if not os.path.isfile(CSV_PATH):
        print('[-] CSV file Not Found')
        print('Make sure your dataset is in this format: https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat')
        return 
    

    #----------------------------------------------------------------
    # Read JSON
    #----------------------------------------------------------------
    f = open (JSON_PATH, "r")
    info = json.loads(f.read())


    #----------------------------------------------------------------
    # Load CSV
    #----------------------------------------------------------------
    data_df = pd.read_csv(CSV_PATH)
        
    
    

    #----------------------------------------------------------------
    # Check Columns in CSV
    #----------------------------------------------------------------
    csv_columns = data_df.columns





    #Category 
    if not info["category_column_name"] in csv_columns:
        print('[-] Column Not Found : ' + info["category_column_name"])
        return


    #----------------------------------------------------------------
    # Settings from info JSON file
    #----------------------------------------------------------------

    # category column name in csv
    CATEGORY_COLUMN = info["category_column_name"]

    
        

    data_df['label_cat'] = data_df[CATEGORY_COLUMN].astype('category')


    
    train_data, test_data = train_test_split(
        data_df, test_size=0.5, 
        random_state=420, shuffle=True, 
        stratify=data_df[CATEGORY_COLUMN]
    )
    print("###-------------------------------------###")
    print("### Total solutions : ",  data_df.shape[0])
    print("### Train solutions : ", train_data.shape[0])
    print("### Test solutions : ", test_data.shape[0])
    print("###-------------------------------------###\n\n")
    
    
    train_solution =  np.asarray(train_data['label_cat'].cat.codes.values)
    test_solution = np.asarray(test_data['label_cat'].cat.codes.values)
    
    solutions = [train_solution, test_solution]
    solution_names = ['train', 'test']
    
    print("###-------------------------------------###")
    print("### Solutions files are ready!")
    print("###-------------------------------------###\n\n")
    
    return (solution_names,solutions)


