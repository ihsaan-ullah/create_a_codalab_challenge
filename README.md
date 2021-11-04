# Repository for Codalab bundle for AI Challenge Creation Class

This repository is for **challenge organizers** to organize a challenge on [Codalab](https://codalab.lisn.upsaclay.fr/).

This repository has a sample starting kit which is made specially to work with this [Data Format](https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat).

## Understanding the Starting Kit

The starting kit consists of the following directories and files:

1. `html_pages` 
a directory which contains  these html files for Codalab webpage of the competition: 
    - `overview.html` : to give an overview of the challenge, description of task and credits
    - `data.html` : to describe the data to be used in this challenge
    - `evaluation.html` : details about how participants will be evaluated  
    - `rules.html` :  Terms and Conditions for participating in this challenge
    
You have to change all the html files according to your competition details except `rules.html`.


2. `ingestion_program`  
this directory consists of the following files:
    - `data_io.py` : contains functions to load the data
    - `ingestion.py` : responsible for loading, running the model with the input data and to save the results in the results directory
    - `metadata` : a file required to run the code on Codalab 


3. `scoring_program`  
this directory consists of the following files:
    - `metric.txt` : a text file which consists of the name of the metric of evaluation
    - `solution.py` : to load only the solutions from the input data
    - `score.py` : responsible to compute score from the predictions made by `ingestion.py` and ground truths from `solution.py`
    - `libscores.py` : consists of pre-defined metrics 
    - `my_metric.py`: a file in which you can define your own custom metric or use any metric from a library e.g. scikit-learn
    - `metadata` : a file required to run the code on Codalab 


4. `sample_data`  
this directory contains the sample data or *Dataset 0* for the challenge. The dataset should be in this [Data Format](https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat).









