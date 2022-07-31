# **Amazon_HackOn 2022**

## Customer trust

One of the key elements to increase customer stickiness and trust with the Amazon brand is delivering the right product to the right customer at the right time. This involves identifying and removing counterfeit products off the shelf. We tried to tackle this problem precisely and introduce a new product renting feature to increase customer retentivity.

P.S. - The models because of their size cannot be uploaded here so they have been uploaded to Google Driven,links to what have been given below

# Objective

Increasing customer retention and trust with the Amazon brand by identifying and removing counterfeit products off the shelf and introducing short term renting of goods.

# Applications

A lot of the counterfeit goods have very similar logos, texture, color compared to the original ones but there are few subtle changes (e.g. slightly modified logos, similar sounding brand names). We will use image processing models to detect those subtle changes. We will train the model to predict the counterfeit items. On top of that, counterfeit goods generally have high ratings but low number of comments and a lot of those comments are from sock puppet accounts. We will train an NLP model to predict how many of the comments look suspicious and then from that data we can predict the chances of the product being a counterfeit one. Also we will take into account the activity of the reviewers to find out which one of them might be bots or sock puppets.

# **Implementation**

We used a Faster RCNN object detector to crop the logo region, we further applied a classifier model on this cropped image to find the brand most similar to the given image.  . Finally we applied SIFT algorithm to find out whether the product was  a fake one or a real one. For comment and sentiment  analysis, we will use the Roberta based GPT 2 model.

Finally, we will host these models on AWS and then use a Flutter based webapp/app to use these features. We will provide an easy to use API for the same.

# Techstack

* HTML,CSS
* AWS
* Pytorch
* SQL database
* Flask
* Jupyter Notebook

# What comes after...

After the event is over, we can utilize this idea and turn this into a full fledged app. We also aim to generalize the counterfeit product removal model so that it can detect any counterfeit product for other sites as well. We will also work on expanding our sphere by adding feedback on the goods collected from other social media platforms. We will extend these features for renting and reselling of used goods as well.
With further fine tuning of our DL models we can achieve better accuracy which can drastically reduce counterfeit products and increase customer trust with our platform ensuring retentivity.

