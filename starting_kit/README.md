# Starting kit for Insects Classification Challenge

This challenge uses a Dataset from **MUSÉUM NATIONAL D’HISTOIRE NATURELLE**
    
The dataset coniststs of total 290,000 images and each image belongs to one of the following classes

1. Bee
2. Wasp
3. Other insect
4. Butterfly insect

    
This challenge is about creating and predicting a Machine Learning model and train it with the data provided to classify the images into the mentioned 5 categories. 


### Phases
This challenge conists of two phases:  

1. `Development Phase`
In this phase you can train a model and submit at most 20 submissions per day to check the score of your model and to see how good your model is performing. Once you are satisfied with your performance then you can try the Final Phase.
    
2. `Final Phase`
In this phase you can submit only once so it is advised to do it when you are ready for the final submission.
    
    

### References and credits: 

1. MUSÉUM NATIONAL D’HISTOIRE NATURELLE (https://www.mnhn.fr/)
2. SPIPOLL (https://www.spipoll.org/)      
3. Université Paris Saclay (https://www.universite-paris-saclay.fr/)
4. ChaLearn (http://www.chalearn.org/)


### Prerequisites:
Install Anaconda Python 3.6.6 


### Usage:

(1) If you are a challenge participant:

- The file README.ipynb contains step-by-step instructions on how to create a sample submission for the Bees and Wasps Image Classification challenge. 
At the prompt type:
jupyter-notebook README.ipynb

- modify sample_code_submission to provide a better model or you can also write your own model in the jupyter notebook.

- zip the contents of sample_code_submission (without the directory, but with metadata), or

- download the public_data and run (double check you are running the correct version of python):

  `python ingestion_program/ingestion.py public_data sample_result_submission ingestion_program sample_code_submission`

then zip the contents of sample_result_submission (without the directory).

(2) If you are a challenge organizer and use this starting kit as a template, ensure that:

- you modify README.ipynb to provide a good introduction to the problem and good data visualization

- sample_data is a small data subset carved out the challenge TRAINING data, for practice purposes only (do not compromise real validation or test data)
