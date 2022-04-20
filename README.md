# BehaviorPredator

BehaviorPredator is a scalable, fully-customizable, and integrable solution that focuses on identifying insider threats on companies of any size from medium-sized businesses to big corporations and military agencies.The solution is able to map the behaviors of employees in real-time using data inputs such as computer logs, file & folder manipulation, external device usage, email communications, incident reports, and much more!

This data is then able to be browsed and analyzed in TigerGraph. After that, the user is able to run a series of GSQL queries to identify known suspicious behaviors and expand on potential threats. Users are able to create new rules using the BehaviorPatterns. In addition to providing support for identifying known suspicious behavior, BehaviorPredator is able to identify unknown insider threats by leveraging the use of group behavior analysis with unsupervised machine learning. This gives the ability for BehaviorPredator to single out those that pose a danger to the organization.

![BehaviorPredator Infographic](https://raw.githubusercontent.com/Nate8888/TigerGraphHack/main/info.jpg)

# Graph Schema

The graph contains 10 vertices and 9 edges representing relationships between the data. The core of the graph relies on the User Vertex. A User can trigger FileEvents, ApplicationEvents, Browsing, and External Devices. In addition to that, Users have a record of Incoming Emails, Outgoing Emails, and Incident Reports. FileEvents from Users can trigger "honeypots" (traps) that indicate suspicious behavior. External Devices have a relationship with registered Devices that define a potential threat through an external device.

![BehaviorPredator Schema](https://raw.githubusercontent.com/Nate8888/TigerGraphHack/main/platform_imgs/graphschema.png)

# Data Files

|     File      | Description |
| ------------- | ------------- |
| [user.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users.csv)  | Represents the entire user base  |
| [user_files.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users_files.csv)  | Represents all file events triggered and the user that triggered it  |
| [files_honeypots.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/files_honeypot.csv)  | Represents all files that are marked as 'honeypot' traps  |
| [users_apps.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users_apps.csv)  | Represents all application events triggered and thenn user that triggered it |
| [users_browser.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users_browser.csv)  | Represents all Browsing events and all users associated with it |
| [users_incidents.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users_incidents.csv)  | Represents all incidents associated with users |
| [users_emails.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users_emails.csv)  | Represents all emails sent by users. Messages are scrambled |
| [users_external.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/graph_data/users_external.csv)  | All external devices plugged by users|
| [cat_daily.csv](https://github.com/Nate8888/TigerGraphHack/blob/main/src/cat_daily.csv)  | Dataset extracted from AppEvents, FileEvents, and Browse for anomaly detection |

# Data flow in graph schema
![Data Load Description](https://raw.githubusercontent.com/Nate8888/TigerGraphHack/main/platform_imgs/load_data.png)

# GSQL Queries

With the current installed GSQL queries, BehaviorPredator allows people to explore the entire userbase, find users with a certain threat score, find users that triggered honeypot files and exceeded a threshold of threat score, find users that sent emails with attachments with low sentiment scores, and find users who recently plugged external devices with a record of incidents. In addition to that, BehaviorPredator gives the ability to find anomalies in a group of individuals with the same role in a company using an Isolation Forest Machine Learning model.

|     File      | Description |
| ------------- | ------------- |
| [honeypot_threatscore.gsql](https://github.com/Nate8888/TigerGraphHack/blob/main/src/GSQL_queries/honeypot_threatscore.gsql)  | Able to find users that exceed a certain threat score and that have triggered a honeypot  |
| [incidents_devices.gsql](https://github.com/Nate8888/TigerGraphHack/blob/main/src/GSQL_queries/incidents_devices.gsql)  | Find users with incident reports that have plugged external devices in the past |
| [sentiment_threatscore.gsql](https://github.com/Nate8888/TigerGraphHack/blob/main/src/GSQL_queries/sentiment_threatscore.gsql)  | Find users that exceed a certain threat score and that had a negative amount of sentiment in emails with attachments  |
