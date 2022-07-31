# **Amazon_HackOn 2022**

##Customer trust

One of the key elements to increase customer stickiness and trust with the Amazon brand is delivering the right product to the right customer at the right time. This involves identifying and removing counterfeit products off the shelf,

P.S. - The models because of their size cannot be uploaded here so they have been uploaded to Google Driven,links to what have been given below

# Objective

Increasing customer retention and trust with the Amazon brand by identifying and removing counterfeit products off the shelf and introducing short term renting of goods.

# Applications

A lot of the counterfeit goods have very similar logos, texture, color compared to the original ones but there are few subtle changes (e.g. slightly modified logos, similar sounding brand names). We will use image processing models to detect those subtle changes. We will train the model to predict the counterfeit items. On top of that, counterfeit goods generally have high ratings but low number of comments and a lot of those comments are from sock puppet accounts. We will train an NLP model to predict how many of the comments look suspicious and then from that data we can predict the chances of the product being a counterfeit one. Also we will take into account the activity of the reviewers to find out which one of them might be bots or sock puppets.

There are some customers who buy a product, use it for a few days and then return it. We will find the purchase return pattern of their accounts to see if they are deliberately doing this. To discourage this and increase affordability of certain goods, we will introduce a new renting system where the customer can rent an item for a specific period of time. Goods like travel equipment, expensive suits and garments, furniture etc. can be rented for a short period of time at a smaller and more affordable price. This encourages people to use different products of the same type and also we can limit the number of renting of a specific product. This will increase sales in the long run and also retain customers effectively. We will collect this data to show those specific customers more such offers.

# **Implementation**

We will keep FCN units to extract the features of the images and then pass them through transformer encoders and use that to predict the subtle changes of logo, brand name etc in the product image. For the backbone of the model and feature extraction, we will use the pretrained ResNet or Xception etc. For comment analysis, we will use the GPT 3 model. We will also use a price checking algorithm on branded products to identify if they are genuine. We will use the combined output of these models to create a trust index parameter which can be used to highlight authentic products.

For the purchase-return pattern recognition, simple machine learning models like Random Forest, Support Vector Machine etc. can be used. We will keep track of items rented and suggest similar items to our customers.

Finally, we can host these models on AWS and then use a Flutter based webapp/app to use these features. We will provide an easy to use API for the same.

# Techstack

* HTML,CSS,Bootstrap
* AWS
* Pytorch
* SQL database

# What comes after...

After the event is over, we can commercialize this idea and turn this into a full fledged app. We also aim to generalize the counterfeit product removal model so that it can detect any counterfeit product for other sites as well. We will also work on expanding our sphere by adding feedback on the goods collected from other social media platforms. We will extend these features for renting and reselling of used goods as well.

