# Cherry Powdery Mildew detector

## Table of Contents

1. [Background](#background)
2. [Project Dataset](#project-dataset)
3. [Business Requirements](#business-requirements)
4. [Hypothesis and Validation](#hypothesis-and-validation)
5. [Implementation of the Business Requirements](#the-rationale-for-mapping-business-requirements-to-data-visualizations-and-ml-tasks)
6. [ML Business case](#ml-business-case)
7. [Dashboard Design](#dashboard-design)
8. [CRISP-DM Process](#crisp-dm-process-implementation)
9. [Bugs](#bugs)
10. [Deployment](#deployment)
11. [Technologies used](#technologies-used)
12. [Credits](#credits)

## Background

Farmy & Foods, are the client for this project and are facing a challenge where their cherry plantations have been presenting powdery mildew.
Powdery mildew is a parasitic fungal disease caused by Podosphaera clandestina in cherry trees.
When the fungus begins to take over the plants, a layer of mildew made up of many spores forms across the top of the leaves.
The disease is particularly severe on new growth, can slow down the growth of the plant and can infect fruit as well, causing direct crop loss.

The process used by Farmy & Foods to verify the presence of powdery mildew is manual. An employee spends around 30 minutes on each tree, taking a few samples of tree leaves
and verifying visually if the leaf is healthy or has powdery mildew. If there is powdery mildew, the employee spends 1 minute applying a specific compound to kill the fungus.
The company has thousands of cherry trees, located on multiple farms across the country and tie saving solution is needed.

## Project Dataset

* The dataset contains 4208 images taken from  Farmy & Foods's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).

## Business Requirements

To save time in this process, the IT team suggested an ML system that can detect instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

The client a two manin requirement:

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and validateion

### Hypothesis

* Infected leaves have clear marks differentiating them from the healthy leaves.

### Validation

* We suspect cherry leaves affected by powdery mildew have clear marks, typically the first symptom is a light-green, circular
  lesion on either leaf surface, then a subtle white cotton-like growth develops in the infected area.

### Observation

* An image montage shows the difference between a healthy leaf and an infected one.

* The difference between average and variability images shows that affected leaves display more white powdery spots around the center of the leaf

* And the image difference between average infected and average infected leaves shows no intuitive difference.

### Conclusion

* The model was able to detect such differences and learn how to differentiate and generalize in order to make accurate predictions.
  A good model trains its ability to predict classes on a batch of data without adhering too closely to that set of data.
  In this way the model is able to generalize and predict future observation reliably because it didn't 'memorize'
  the relationships between features and labels as seen in the training dataset but the general pattern from feature to labels.

## Rationale for Data Visualisations and ML tasks

## ML Business Case

* To address this challenge the IT team suggested an ML system that uses a leaf image to instantly detect if it is healthy or has powdery mildew.
A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

## Deployment

### Heroku

* The App live link is: <https://mildew-detector-pjt.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Below is a list of the libraries used in this project.

|ML Library|Version|Used for|
|:---:|:---:|:---:|
|keras |2.6.0 |setting model's hyperparamters|
|matplotlib|3.3.1 |plotting the sets' distribution|
|numpy |1.19.2 |converting to array|
|pandas |1.1.2 |creating/saving as dataframe|
|plotly |5.12.0 |plotting the model's learning curve|
|scikit-learn  |0.24.2|evaluating the model|
|seaborn |0.11.0 |plotting the model's confusion matrix|
|streamlit |0.85.0 |creating the dashboard|
|tensorflow-cpu |2.6.0|creating the model|

## CREDIT

#### Code, content and media

* The code template I used to start this project was provided by code institute as part of this course's material.
* I also repurposed the code provided during the Malaria Detector Walkthrough project since the projects are so similar to create content for this project. I followed along the  
  malaria detector tutorial video series in order to create and complete the jupyter notebooks and streamlit dashboard.
* The content on the summary page of the streamlit app was source from [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew).

## Acknowledgements

* Thanks to [Code Institute](https://codeinstitute.net/global/) and my one-off session mentor Precious Ijege.
