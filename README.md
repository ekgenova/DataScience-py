# DataScience-py
with pandas and jupyter

#### DataProcessing.py
- processing csv file 'Wine_Data_unclean' to be fit for classification. ID tables removed and column 'variety_and_region' which includes multiple values within it has been split.
- extracted in new csv file 'Wine_Data_clean'

#### KNN.py
- performing K Nearest Neighbour on 'BreastCancerData.csv'
- headers never initialised for data set so the headers are actually the first row of values...
- multiple dataframes created from the initial one - without ID, without classification, only the first 450 records (for training), normalised dataset (between 0-1)
- calculates K value, indexes the datasets into arrays, then splits them to perform a prediction
- prediction is compared to the original classifications and a confusion matrix/classification report is presented

#### BreastCancerKNNExample.r
- example above done in R
