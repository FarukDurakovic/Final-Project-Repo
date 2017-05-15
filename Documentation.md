# Documentation of Final-Project-Repo, By Faruk Durakovic

## Introduction

 * To future classes, this will be my documentation of what all the files required for an AWS Flask webserver!

## Dockerfile

 * What Dockerfile does is it allows us to use the linux system of unbuntu xenial that the AWS Flask Webserver runs off of.

 * The Dockerfile also contains the essential install and update commands such as: RUN apt-get install -f -y python3.

 * Finally, the COPY . /src and WORKDIR /src are commands that copy the contents from the directory into the docker image and selcet which directory to copy to.

## UNH698.py

 * The unh698.py file holds the information about the html files you are going to be using for your website.

 * In the first few lines you have the imports such as: from flask import Flask and from flask import render_template.

 * app = Flask(__name__) is used to find where to import the file information from.

 * The next three code blocks are defining the methods for the three different webpages, specifically that ones I labeled Main_Page and Sub_Page1 and 2.

 * The file block is an if statement that runs a debug if the file that was imported shared the same "__main__" name.
 
 * ![unh698.py image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File1.PNG)
 
## UNH698_test.py

 * The unh698_test.py file is where the the testing occurs... duh!

 * More specifically, in the class labeled FlaskrTestCase, it imports unittest testcase as well as the previous unh698.py file that has our html webpage information.

 * The first two commands, SetUp and TearDown, import the information needed for a specific unit test and then reset it for the next unit test respectively.

 * The next code block, test_home_page, checks to see if the desired assert, or word/phrase/sequence, is found in the desired location.

 * The next four code blocks, specifically the test_link... and test_my_topic..., search to see if the desired link name is inside their search locations and see if the desired link destination page has the desired text respectively.

 * For example, the code in: def test_my_topic1(self): / rv = self.app.get('/Sub_Page1') / assert b'Here Either...' in rv.data, is creating a testcase for my first topic, which is Sub_Page1, then the rv or return value sets self.app.get to be the link to my Sub_Page1, and finally the assert looks the the text "Here Either..." which is a phrase used in the Sub_Page.html file.

 * ![unh698_test.py image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File2.PNG)
 
## run_test.sh

 * This is a simple one.

 * This sh file is a Linux executable file that prints the phrase "Running Flask Unit Tests" when the executable runs.

## docker-compose.test.yml

 * This file is also simple.

 * The sut: stands for system under test, the build: . runs the command bash ./run_test.sh from the previous file.

## Main_Page.html and Sub_Page1 and 2

 * Each of the html files look relatively similar, however there slight differences in what they do.

 * In Main_Page.html, <!DOCTYPE html> states that the file is an html file.

 * The two <html>'s are the contents of the html file.

 * The <title>'s display the title of the page, in this case UNH698 Website.

 * The <body>'s reference what is shown on screen on those webpages.

 * And finally, the <a href=...> ... </a> define the link that will appear in the url bar as well as the name that will appear onscreen in the actual webpage. In this case, the url will display .../Sub_Page1, and the webpage will have a link that says Faruks Topic #1 which will take me to Sub_Page1.

 * The only things different in the Sub_Page html files is that instead of using the <a href=...> ... </a>, you can just type anything between the two <body> fields and the test will appear onscreen!
 
 * ![Main_Page image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File6.PNG)
 
 * ![Sub_Page1 image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File7.PNG)
 
 * ![Sub_Page2 image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File8.PNG)

## deploy-website-production/staging.yml

 * What these files do is allow the webpages to be run from specific snapshots in your code based on what tag you used for them. 

 * In case you don't know what a tag is, when you reach a certain point in your code that it can sufficiently do a task, you can do a git command that sets a sort of waypoint that tags that milestone in the code. Then the tag can be referenced in your github account when you look through it, or you can set your website to run based off of where that tag is in your as an example.

 * The name is what is printed on screen when the command is initially executed.

 * The hosts is set to local host so that you can access the server locally through the machine running it.

 * The variables are the name of the environment, in this case stagin, the image version, which is the tag you chose, the host port is the port you use to access it, and the container port is the port Flask uses view the server.

 * The roles is a subfolder that contains a main.yml file that is referenced and has information for this code.

 * ![Production image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File5.PNG)
 
 * ![Staging image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File4.PNG)

## configure-host.yml

 * This file configures your local machine to run docker, simple enough.

## ansible.cfg

 * This is the list of hosts, which only contains the localhost.

## main.yml

 * There are four different main.yml files so I will go over them in order as they appear.

 * The first main.yml sets values for the unh698 role. 

 * It sets the image to be the dockercloud repository of your choice, and sets the command to be python3 unh698.py, which runs unh698.py through python.

 * The next main.yml does several things.

 * It has 3 functions which are as follows: Ensure python docker-py package is installed, Start/Restart the unh698 container, and verify that the webserver is running.

 * The first command is done by using the pip command which downloads installs the latest version of docker-py.

 * The second command gets its values from the unh698 file and places the in the correct positions. It also gets the port information from the files.

 * Finally, the last command sets the url to be used to verify that the webserver is running.

 * The next main.yml updates the cache of the server every 1.8 seconds.

 * The final main.yml file includes a list of tasks that are needed to set up the docker service. Those tasks being install.yml, user.yml, and service.yml.

## user.yml

 * What this file does is adds a user to the linux group on the host.

 * The name: "{{ student_username}}" portion of this takes the username given by the command: ansible-playbook configure-host.yml -v --extra-vars "student_username=fdurakovic" and sets the username to be that name.

## service.yml 

 * This is a very simple file.

 * It ensures that the docker service is started.

 * The line says state references that state of being that the service is expected to be.

## install.yml

 * This file does five different things.

 * First, it installs the docker dependencies needed to run everything.

 * The second command sets up the docker repository key that is used to access the server.

 * The third command gets the release version of ubuntu that is running and registers it as release.

 * The fourth command adds the docker repo that you had chosen in the first main.yml file.

 * The final command installs the latest version of docker community edition by downloading the docker-ce package.

## prometheus_metrics.py

 This is the final file to be documented. 

 * This file does the "math" of the website to see how long it has been running and how many times the page has been accessed.

 * This file is very similar to the unh698.py file as it has functions used to collect the data that is being input into the system.
 
 * ![Prometheus Metrics image](https://github.com/FarukDurakovic/Final-Project-Repo/blob/master/images/File3.PNG)
