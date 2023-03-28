## Project 9 Transaction fraud detection

**Application**

Using machine learning to classify fraudulent transactions reduces manual effort and allows for efficient processing of large volumes of data. By adapting to real-time detection, it can help prevent financial losses for both customers and the company.



**Project details**

The data was acquired from Kaggle by using opendatasets library. 

**1. Exploratory data analysis**

Null data was checked first.
The data was visualized for identifying the features that likely to be related with fraud transaction.

**2. Data preprocessing**

A new feature, that was seemed to be related with fraud transaction, was created. 

**3. Modelling**

Because of imbalance, the data was oversampling and used for training the model according to the pipeline. 

Here is the model pipeline.

![Screenshot 2023-03-09 115129](https://user-images.githubusercontent.com/123642022/223931586-1924b12c-685c-4439-a658-8cd3bfc6fa90.png)

A mean cross validation of the model is 98.25%

**4. Prediction and Evaluation**

The model was used to predict the fraud in test dataset. Then, the confusion matrix and ROC curve were used to display model performance.  

![Screenshot 2023-03-09 123959](https://user-images.githubusercontent.com/123642022/223932225-3e34dc35-4d88-4dea-98da-e8d32b7440e3.png)
