New to git, attempting to learn it using a WIP project.

Using an API key from https://newworldstatus.com/, this bot collects data for a specified world in New World. 
Selenium is also included to scrape the official page https://www.newworld.com/en-us/news for updates, and places them in an embedded message to your discord server. 

If you want to use this to kickstart your own code, you'll need to sign up for an API key from newworldstatus, as well as provide a discord bot token stored as a JSON file. 

pip3 install -r requirements 

Developed on WSL Ubuntu and VScode if that matters.


Requirements:
* Chrome 
* sudo pip3 install virtualenv
* source .venv/bin/activate
* wget https://chromedriver.storage.googleapis.com/95.0.4638.17/chromedriver_linux64.zip
* unzip chromedriver_linux64.zip -d drivers/

run qbot.py
