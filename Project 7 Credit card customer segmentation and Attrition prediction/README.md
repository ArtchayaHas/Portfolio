## Project 7 Credit card customer segmentation and Attrition prediction 

**Application** 

  Customer segmentation is a crucial process that helps a company learn about its customers. As each customer segment has different needs, identifying which group the customer belongs to is valuable information for the company. This knowledge aids the company in providing appropriate services to customers in each section.
  
  Additionally, understanding the pattern of customer attrition can help the company reduce the attrition rate and retain customers.

**Projec details** 

The data was acquired from Kaggle by using opendatasets library. 

**1. Exploratory data analysis**

Null data and relation among features were checked first.
And correlation heatmap was plot. 

![rsz_1screenshot_20230224_090919](https://user-images.githubusercontent.com/123642022/221204664-3ebee238-81d2-45b6-8d8e-ad3f99627f99.png)

**2. Customer segmentation**

PyCaret library was used for clustering and classification (in the next part). 

The customer was clusterred into 4 groups as shown.


![Screenshot_20230224_093658](https://user-images.githubusercontent.com/123642022/221205279-490baeca-b6cc-4644-9d24-bca179f3ff33.png)

From the data each customer cluster has characteristics as following;
- Cluster 0: Most are married with low income even they had varies educational levels. They have low purchasing power and low credit score (Utirization ratio).  

- Cluster 1: Most are single with high income. They have high purchasing power and great credit score. This group might represent upper class people or upper-middle class.

- Cluster 2: Most are married with low income. Although they didn't have much income, from average credit limit and credit score, they seem to have better money management when comparing with cluster 0 group. 

- Cluster 3: Most are married with high income. This group might be represent middle to upper-middle class who has moderate purchasing power and good credit score. 


**3. Attrition prediction**

From PyCaret, Light gradient boosting was the best model for classification. With 99.33% accuracy on test data. 


Here is a ROC graph of the model.

![Screenshot_20230224_095719](https://user-images.githubusercontent.com/123642022/221210589-74450283-14c3-424c-b188-07841b07456d.png)


Also, feature importance can be acquired as shown; 

![rsz_screenshot_20230224_095319](https://user-images.githubusercontent.com/123642022/221209705-d47209af-aefe-4548-b62a-53206c1df92a.png)

This model can be used for detect the customers who have high risk for attrition and the data can be applied for creating some offers for the target before they decided to drop out.  


