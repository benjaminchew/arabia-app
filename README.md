# arabia


Set Up Python 3.7 Virtual Environment
---------------

* Clone the code from github.
```
    git clone https://github.com/72L/arabia.git
```

* (if not already) Download a version of Python 3: https://www.python.org/downloads/

* (if not already) Install pip: https://pip.pypa.io/en/stable/installing/

* install virtualenv:
```
    pip install virtualenv
```

* make a `~/.virtualenvs` directory if it does not already exist:
```
    mkdir ~/.virtualenvs
```

* Get out of any virtualenv you may be in currently (`deactivate`).
```
    cd ~/.virtualenvs
    virtualenv -p python3 arabia
    source ~/.virtualenvs/arabia/bin/activate

```

* Go back to the arabia directory
```
    cd
    cd [path to arabia]
```

* Install required packages
```
    pip install --upgrade pip
    pip install -r requirements.txt
```

* Login on Heroku
```
    heroku login -i
```

* Add heroku as git remote
```
    heroku git:remote -a arabia
```


Remember to activate environment for every new Terminal tab
---------------
```
    source ~/.virtualenvs/arabia/bin/activate
```


Testing Locally
---------------

* Start server
```
    python app.py
```

* Navigate to http://127.0.0.1:5000/

* If testing API, ping http://127.0.0.1:5000/[api_endpoint]


Deploy to Heroku
---------------

```
    git push heroku master
```

* Navigate to http://arabia.herokuapp.com/

* If testing API, ping http://arabia.herokuapp.com/[api_endpoint]


Running Jupyter Notebooks
---------------

* First time install:
```
    pip install jupyter[notebook]
```

* Navigate to notebooks directory and start notebook server
```
    cd notebooks/
    jupyter notebook
```

Set up Expo
---------------

* Sign up for Expo

* Download Expo Client on your mobile device (https://docs.expo.io/versions/latest/get-started/installation/?redirected#2-mobile-app-expo-client-for-ios)

* First time install Node.js (https://nodejs.org/en/)

* First time install:
```
    npm install expo-cli --global
```

* Sign in to Expo
```
    expo login
```

Work on Expo App
---------------

* Start server in app directory
```
    cd expoapp/arabia
    npm start
```

* Use the camera app to take picture of QR code, which will open Expo app

