# Machine Learning API using FastAPI
The project was to Develop a Machine Learning API (Application Programming Interface) using FastAPI.


## Introduction

In this project we first build and train our four models which is used to develop the ML API using the FastAPI.

In this project, the aim is to create an API that might be requested to interact with a ML model. This is an interesting solution when you want to keep the model architecture secret or to make the model available to users already having an API. By creating an API, and deploying it, the model can receive request using the internet protocol as presented by the illustration below.


## Description

1.  Build a ML model to predict the [Sepsis](https://www.kaggle.com/datasets/chaunguynnghunh/sepsis?select=README.md)(**Data set here**), 

2.  Build an API using Fast API, to embed the ML model built.

## Setup

Install the required packages from the requirements.txt to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version higher than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI
  Live Demo:

  FastAPI:
 
  - Go to your browser at the following address, to explore the api's documentation :
        
      http://127.0.0.1:8000/docs

![Alt text](<pics/Screenshot 2024-04-07 202420.png>)

To view the fastAPI in the dockerhub follow link:

* [Dockerhub](https://hub.docker.com/repository/docker/qochieng/sepssis-api/general)





## Resources
Here are some ressources you would read to have a good understanding of FastAPI :
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)




## Author
Quintor Ochieng'

* [LinkedIn](https://www.linkedin.com/in/quintor-ochieng)

* [github](https://github.com/qochieng/Career_Accelerator_P5-ML_API)

## License
MIT