# Cherry Powdery Mildew detector

## Table of Contents

1. [Background](#background)
2. [Project Dataset](#project-dataset)
3. [Business Requirements](#business-requirements)
4. [Hypothesis and Validation](#hypothesis-and-validation)
5. [Implementation](#rationale-for-data-visualizations-and-ml-tasks)
6. [ML Business case](#ml-business-case)
7. [Dashboard Design](#dashboard-design)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Technologies used](#main-data-analysis-and-machine-learning-libraries)
11. [Credit](#credit)

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

## Hypothesis and validation

### Hypothesis

* Infected leaves have clear marks differentiating them from the healthy leaves.

### Validation

* We suspect cherry leaves affected by powdery mildew have clear marks, typically the first symptom is a light-green, circular
  lesion on either leaf surface, then a subtle white cotton-like growth develops in the infected area.

### Observation

* An image montage shows the difference between a healthy leaf and an infected one.

* The difference between average and variability images shows that affected leaves display more more white powdery looking patches around the center of the leaf

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

#### Page 1: Quick Project Summary

* Quick Project Summary

![Quick Project Summary](https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/612ed4c2-47b9-4ba3-90d0-78df436a5092)

#### Page 2: Leaves Visualiser

* Difference between average and variability

![Difference between average and variability image](https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/350e4d95-2546-46a4-bc61-7bfcfb5fc07e)

* Difference between average infected and avearge healthy leaves

![Difference between average infected and avearge healthy leaves](https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/28ad7d9a-8b77-4f28-a254-083f34b5ecdb)

* Image montage

<img width="614" alt="Screenshot 2024-01-18 at 07 04 18" src="https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/6f01089a-502c-4f40-933c-b317895ea2f3">
#### Page 3: Powdery Mildew detector

#### Page 4: Project Hypothesis

* Hypothesis and validation

<img width="765" alt="Screenshot 2024-01-18 at 07 19 30" src="https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/b273838d-0893-4fa9-be55-b5d9a792a68d">

#### Page 5: ML Performance Metrics

* Images distribution per data set and label
  
<img width="528" alt="Screenshot 2024-01-18 at 07 18 28" src="https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/47873145-b83a-42cb-8138-8abcea1e54b8">

* Model Accuracy
  
<img width="550" alt="Screenshot 2024-01-18 at 07 18 47" src="https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/58c43bb1-3967-4cb5-8c44-cc4979d01273">

* Model Loss

<img width="499" alt="Screenshot 2024-01-18 at 07 19 02" src="https://github.com/Flora-King/Mildew_Detection_pjkt/assets/106548101/ff30dd9b-88eb-48e4-b643-0dda962ee3c2">

## Unfixed Bugs

* tThere are no un fixed bugs

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

## Credit

#### Code, content and media

* The code template I used to start this project was provided by code institute as part of this course's material.
* I also repurposed the code provided during the Malaria Detector Walkthrough project since the projects are so similar to create content for this project. I followed along the  
  malaria detector tutorial video series in order to create and complete the jupyter notebooks and streamlit dashboard.
* The content on the summary page of the streamlit app was source from [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew).
* I frequently searched through queries on stackoverflow for guidance on how to get rid of the bugs i encountered
* I searched and reviewed code queries liste don code institute Slack

## Acknowledgements

* Thanks to [Code Institute](https://codeinstitute.net/global/) and my one-off session mentor Precious Ijege.
