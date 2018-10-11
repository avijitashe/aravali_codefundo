# aravali_codefundo
ARAVALI makes predictions better and alerts more relevant. An Open Source System Prototype to predict, prevent, or manage the impact of natural disasters. This is for codefundo++ 2018.

Synopsis :

CWC, a national body, manages a flood forecasting network of 175 stations across India. IMD, another national body, handles cyclone and rainfall warnings, currently involved with “Titli”. As per data from 2009, roughly 5000 forecasts classified into 4 categories are issued every year during flood season. Even before IMD was established, cyclone warning systems are in place since 1865 that has a 4 stage system in place today. The alerts are issued 1-2 days in advance currently. When there are a lot of false warnings, it creates unnecessary panic and widespread chaos for preparedness like moving army, evacuation, arranging shelters. People on the move, in the seas need to take precautions, cancel travel, return to coast, move to high grounds and more. During an emergency, generic alerts in non-regional languages via websites, news and radio is not adequate today. We can assist them better.

## What are you planning to build?
We have data for past 100 years from these bodies and news (e.g. The-Hindu) archives. Today, social media is a huge source of data for future. If we can combine the available historical records of actual events (cyclones, landslides, loss of life, infrastructure, trajectory etc.) from news APIs with historical sensor data collected by IMD & other depts, and fuse the two together, poor prediction resulting from false positives can be greatly reduced and latent structures can be learned. If we can aggregate data from Tweets (social media with permissions) real-time updates can make alerts more relevant.

Despite penetration of the internet traditional SMS (no internet) with regular relevant status updates, predictions, and safety precautions in regional languages is necessary.

The real-time measurements from satellite, sensors and gauges offer greater weightage.
Finally, using feedback from the community via helpline/SMS in real-time can be used as surrogate sensors to gather additional data. For ex: Pings on rising water levels in streets or mud flow 

## How does it work?
ARAVALI is based on (A)gg(R)egated (A)rri(V)al of (L)atent (I)nformation to:
1. Improve predictions (in time and accuracy) by combining predictions from curated fused data (above) and aggregated real-time public social media and sensor systems from IMD, CWC etc.
2. Monitor the data from social media posts – tune – update database
3. Disseminate relevant alerts via SMS and Phone IVR (NLP) assistance in regional languages to concerned demographics/territories 

## What technologies are you using?
We make use of Azure Functions for serverless architecture, Azure Storage solutions, newsapi's API for datamining, tweepy API for updates, way2sms API for SMS services, translator and transliteration API for alerts, analysis, and DSVM for machine learning.  C#, Python and R.

## What dataset (s) are you using?
IMD (https://data.gov.in/catalogs/ministry_department/ministry-earth-sciences)
Create custom dataset 

## How users can get started with the project?
To contribute clone the repo, prepare credentials for APIs, and submit updates. Note: API policies are subject to change

Future Works: Learn trajectory of cyclones and floods from historical data. Better NLP for IVRS alerts and assistance. 
Keywords: social media, cyclone, flood, API, predictions, machine learning, alerts

