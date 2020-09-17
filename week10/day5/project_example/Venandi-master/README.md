# Venandi

## 1 Intro:
Venandi is my final project of the Ironhack's data analytics/scientist bootcamp. 
It is an API with 3 functionalities:
- Search Github users based in location, programming language and seniority level
- Predict the seniority of a Github user by giving the user nickname/login and also, it searches for his/her linkedin profile

## 2 Goals:
The personal goal of the project was to put in practice almost everything I have learned during this bootcamp. 
The goal of the project is to help other users or even recruiters to find programmers/engineers/analysts with a specific level of seniority, to collaborate in different projects, learn hand to hand or being hired.

## 3 Steps:
To fulfill the previous goals the next steps have been done:

- I collected a database of 50k users from Github, from different countries and different level of followers. The collection was made by using the Github API (src/gitapi.py)

- I 1st analyzed the users based in their repos characteristics (number of stars, number of forks, number of owner's repos and forked repos) alongside with the users characteristics (number of repos, number of followers and number of years in the platform). Where I found a big positive correlation between followers, forks and stars and almost no correlation with and between the other variables. After this 1st point, helped by statistics functions and KMeans Classifier, I figured out that the number of "stars" was the best characteristic to cluster users by their seniority (src/kmeans_user_repo_clustering.ipynb)

- However, as stars is not an user characteristic in the Github API, I repeated the same process with the user characteristics (number of repos, number of followers and number of years in the platform). But already knowing the importance of followers over number of repos and years. Finally, with KMeans again, I was able to classify the users in different seniority clusters based in their number of followers and repos (src/kmeans_user_clustering.ipynb)

- The next step was therefore, to predict this seniority level when an user was given. To do so I trained different multiclass algorithms, finding the Random Forest Model the one with the biggest accuracy for the purpose of the project (src/supervised_user_classification.ipynb)

- Finally, the step of finding the Linkedin user link was made with Selenium (src/scraper.py)

- Also, to show the API functionality I deployed in Heroku, except the Linkedin part

## 4 Final Output:
The final output is an API that is able to find Github users based in their seniority and also to predict their seniority by giving the user nickname/login (the funcionality of obtaining the Linkedin user link wasn't deployed due to lack of time, but will be soon, however you can see how it works in calls.ipynb, at the end)

## How it works:
- Go to https://venandi.herokuapp.com

- Add the following command to the previous url: /user/location/language/seniority/get, and replace location, language and seniority
  - Location Options: any
  - Language: any programming language
  - Seniority: junior, middle, senior, principal and architect
- Ex: https://venandi.herokuapp.com/user/madrid/javascript/principal/get
  
- Finally delete the previous command and add this one: /user/login/predict, to predict the user seniority by giving the nickname/login of an user
- Ex: https://venandi.herokuapp.com/user/diego-florez/predict
  
  ## Programming language, main modules & tools:
  - Language: Python
  - Requests, json: GitHub API (data extraction)
  - MongoDB: saving pre-classified sample
  - Pandas, Numpy, Matplotlib, Seaborn & Plotly: Data wrangling, descritiptive analytics & visualization
  - Sklearn: clustering data (K Means, PCA, t-SNE) and multiclass algos (Esemble Methods, Vector Methods, Neighbors, etc)
  - Flask: web connection
  - Selenium: LinkedIn links scraping
  - Docker Image: upload Venandi to Heroku
  - Heroku
