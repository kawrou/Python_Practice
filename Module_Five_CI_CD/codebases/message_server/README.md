Practicing how to wrap a simple web application with a database into containers and deploy them to a toy cloud hosting system that was provided by makers. 

Made use of:
FLASK
DOCKER
EXOFRAME

exoframe.json config files are not being pushed to Github as they contain POSTGRES passwords. 

Config files includes:
database name
hostname which is the name in the cloud environment
environment variable
volume 

web application connection to database
Domain name
port


---UPDATE---
exoframe.json added to git as config files are free of postgres password
Used Exoframe to store the secret in its secrets database. 
It will use it when it sees the placeholder "@alangardiner-postgres-password"