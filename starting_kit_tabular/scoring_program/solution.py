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
    CSV_PATH = os.path.join(data_dir,"labels.csv")
    
   

    #Check CSV file
    if not os.path.isfile(CSV_PATH):
        print('[-] CSV file Not Found')
        print('Make sure your dataset is in this format: https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat')
        return 
    

    #----------------------------------------------------------------
    # Load CSV
    #----------------------------------------------------------------
    data_df = pd.read_csv(CSV_PATH)
    CATEGORY_COLUMN = 'label'
        
    
    


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
    
    
    train_solution =  np.asarray(train_data['label'].values)
    test_solution = np.asarray(test_data['label'].values)
    
    solutions = [train_solution, test_solution]
    solution_names = ['train', 'test']
    
    print("###-------------------------------------###")
    print("### Solutions files are ready!")
    print("###-------------------------------------###\n\n")
    
    return (solution_names,solutions)


