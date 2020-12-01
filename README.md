# My Website

These are the files related to the website I built for myself. 

The original is a simple Django/Bootstrap website hosted in Heroku. This is represented in the Website folder, whose files are unchanged from the Heroku distribution

Link: https://luna-mcbride.herokuapp.com/

I have since put this site into a docker container and hosted it in EC2 (utilizing ECS, CloudFront, and S3). The files I used/majorly changed in order to do this are held within the Docker-Specific folder. I specifically changed some things from the code to put it here (ie changing the cloudfront link, etc). Besides the Settings.py (which replaces the original here), these files were in the folder next to manage.py for me to get it to work. I am leaving them separate specifically because they will not be able to post to EC2 and similar sites without the login credentials (these are in a .env file that I did not add for obvious reasons). I just want to show off the building of the dockerfile and the docker compose.

Link: http://ec2-54-149-77-78.us-west-2.compute.amazonaws.com:8000/
