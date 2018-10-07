# aravali_codefundo
An Open Source System Prototype to predict, prevent, or manage the impact of natural disasters. This is for codefundo++ 2018.

Synopsis :

CWC, a national body, has a flood forecasting network of 175 stations across India (india-wris.nrsc.gov.in/wrpinfo/index.php?title=CWC_National_Flood_Forecasting_Network ). According to the figures, an average of 5000 forecasts classified into 4 categories are issued every year. When there are a lot of false warnings, it creates unnecessary panic among citizens and widespread chaos for preparedness like moving army, relief, and money. Since, floods are linked to artificial and natural disasters like cyclones in the BOB, rainfall, level of water in reservoirs and unprecedented release, broken drainage systems. If we can aggregare historical actual events (cyclones, landslides etc.) from news APIs with historical data collected by IMD & other depts, poor prediction resulting from false positives can be greatly reduced. 

During an emergency, alert systems in non-local languages and alerts via news aired on television is not adequate. Despite penetration of the internet, traditional SMS with accurate status, predictions, and safety precautions in regional anguages is necessary. 

Using feedback from the community in real-time can be used as surrogate sensors to gather additional data. For ex: if alert from a community regarding rising water levels in streets is received, immediate action or weatehr data analysis can be made.

Finally, real-time measurements from sensors and gauges will have greater weightage.

SOLUTION

ARAVALI is based on (A)gg(R)egated (A)rri(V)al of (L)atent (I)nformation to: 

1) Improve predictions (in time and accuracy) by combining IMD historical datasets and actua news of a flood or cyclone, damage to infrastructure, loss of life etc.
2) Disseminate alerts via SMS and IVRS (NLP) in regional languages to concerned demographics/territories

Prototype:

We make use of Azure for cloud-based Computing, Azure Storage solutions for data, newsapi's API for datamining, way2sms API for SMS services, Bing translator API for regiona language translation. We use Python + it's libraries for coding, Scikit-Learn or Azure ML for machine learning.

FUTURE WORK
Include community feedback to improve resuts. Better NLP for IVRS.
