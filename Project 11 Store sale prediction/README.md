## Project 11 Store sale prediction 

**Application**

Using time series analysis for sales prediction can forecast the trends in the sale of items and estimate the number of items that will be sold in the future. This helps stores effectively regulate their stock of items, reducing the loss of overstocking or understocking and minimizing the cost of labor.


**Project details**

The data was acquired from Kaggle by using opendatasets library. 

**1. Exploratory data analysis**

Null data was checked.
The sale of each store according to the product type was visulized. 

**2. Data preprocessing**

The time features were created and the train data was splitted to train and validation set.

**3. Modelling**

XGBoost Regressor was trained and RMSE on training and validation set was calculated.
RMSE on validation set is 29.74.

The feature importance was visualized. 


![Screenshot 2023-03-09 132005](https://user-images.githubusercontent.com/123642022/223941179-2a384918-57a6-4f50-b9fc-ec6939b3da09.png)

**4. Future prediction**

The test data was used for future sale prediction.

Here is an example of store 1 product 1 sale prediction.


![Screenshot 2023-03-09 132018](https://user-images.githubusercontent.com/123642022/223941470-6ae95763-73fe-4a3b-9a0e-d3436309ba75.png)
