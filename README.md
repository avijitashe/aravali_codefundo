# aravali_codefundo
ARAVALI makes predictions better and alerts more relevant. An Open Source System Prototype to predict, prevent, or manage the impact of natural disasters. This project is developed for hackathon codefundo++ 2018.

ARAVALI is based on (A)gg(R)egated (A)rri(V)al of (L)atent (I)nformation to:
1. Improve predictions (in time and accuracy) by combining predictions from curated data (offline) and aggregated real-time public social media and sensor systems from IMD, CWC etc. 
2. Monitor keywords from social media posts – update database (online)
3. Disseminate relevant alerts via SMS and Phone IVR (NLP) assistance in regional languages to concerned demographics/territories

Synopsis :

CWC, a national body, manages a flood forecasting network of 175 stations across India. IMD, another national body, handles cyclone and rainfall warnings, currently involved with “Titli”. As per data from 2009, roughly 5000 forecasts classified into 4 categories are issued every year during flood season. Even before IMD was established, cyclone warning systems are in place since 1865 that has a 4 stage system in place today. The alerts are issued 1-2 days in advance currently. When there are a lot of false warnings, it creates unnecessary panic and widespread chaos for preparedness like moving army, evacuation, arranging shelters. People on the move, in the seas need to take precautions, cancel travel, return to coast, move to high grounds and more. During an emergency, generic alerts in non-regional languages via websites, news and radio is not adequate today. We can assist them better.

## What are you planning to build?
We have data from IMD and news (e.g. The-Hindu) archives for the past 100 years. We have huge amount of data generated by social media today. If we can combine the available historical records of actual events (cyclones, landslides, loss of life, infrastructure, trajectory etc.) from news APIs with historical sensor data collected by IMD & other depts, and fuse the two together, poor prediction resulting from false positives can be greatly reduced and latent patterns can be learned. If we can aggregate data from Tweets (social media with permissions) real-time updates can make alerts more relevant.

Secondly, despite the penetration of internet, traditional SMS (no internet) with regular relevant status updates, predictions, and safety precautions in regional languages is necessary. If we can do this, a larger audience can be reached.

The real-time measurements from satellite, sensors and gauges always offer greater weightage. They are complementary.

Finally, using feedback from the community via helpline/SMS in real-time can be used as surrogate sensors to gather additional data. For ex: Pings on rising water levels in streets or mud flow 

The front-end is a web application, while back-end does computing. The end-user interacts offline.

## How does it work?
1. Avaiable datasets from IMD is collected
2. newsapi API collects cyclone related figures like casualties, inches of rain, days of rain, people evacuated, shelters, expenses etc.
3. Data is analysed, cleaned and fused
4. Posts, tweets, news are monitored online, databse is updated
5. Messages are composed with updates, forecast, damage etc
6. During an alert, alerts are send via SMS to selected phone numbers, IVR is enabled


## What technologies are you using?
We make use of Azure Functions for serverless architecture, Azure Storage solutions, newsapi's API for datamining, tweepy API for updates, way2sms API for SMS services, translator and transliteration API for alerts, analysis, and DSVM for machine learning.  C#, Python and R.

## What dataset (s) are you using?
1. IMD (https://data.gov.in/catalogs/ministry_department/ministry-earth-sciences)
2. IMD (https://www.kaggle.com/rajanand/rainfall-in-india)
3. Create custom dataset 

## How users can get started with the project?
To contribute clone the repo, prepare credentials for APIs, and submit updates. 

Note: API policies are subject to change

Future Works: 
1. Learn trajectory of cyclones and floods from historical data. 
2. Emergency calls without network authentication (SIM) coverage 
3. Better NLP for IVRS alerts and assistance. 

