# Repository for Codalab bundle for AI Challenge Creation Class

This repository is for **challenge organizers** to organize a challenge on [Codalab](https://codalab.lisn.upsaclay.fr/).

This repository has a sample starting kit which is made specially to work with this [Data Format](https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat).

***

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


4. `scoring_output`  
this directory consists of `scores.html` and `scores.txt` files. These files are used to store scores from scoring program and to load scores to the leader board



5. `sample_data`  
this directory contains the sample data or *Dataset 0* for the challenge. The dataset should be in this [Data Format](https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat).


6. `sample_code_submission`  
this directory consists of `model.py` file which has a Model Class with different functions. You have to change this file but the names of the functions should be the same. You can also keep a pre-trained model in this directory which could be used as a pre-trained model when you submit a code submission.


7. `sample_result_submission`  
this directory contains `train.predict` and `test.predict` files which are used to calculate the score. 


8. `utilities`
this is an important directory which contains `make_bundle.py` to make a bundle to be uploaded as a competition on Codalab. To run this script, use the following command:
```python make_bundle.py```

9. `logo.jpg`
    this image is the logo for your competition on Codalab website.

10. `README.ipynb`
This is python notebook which gives the participants a tour from data loading to code submission on Codalab.

11. `README.MD`
A readme file for an overview of the challenge


***


## Instructions about datasets
The challenge consists of two phases:
    - `Data Phase 1`
    - `Data Phase 2`


This challenge is designed for a triplet of datasets:
    - `Dataset 0`
    - `Dataset 1`
    - `Dataset 2`

`Dataset 0` will be used as a `sample_data`. `Dataset 1` will be used in `Data Phase 1` and `Dataset 2` will be used in `Data Phase 2`. 


***




## ⚠️ Note
The data should be in this format: [Data Format](https://github.com/ihsaan-ullah/meta-album/tree/master/DataFormat)  
You can ignore the *SUPER_CATEGORIES* in the data format for this competition. Check the `sample_data` provided in this [Starting Kit](starting_kit/) for reference.



