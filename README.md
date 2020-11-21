## How to Create Python Virtual Environment and install all dependencies in it

 1.  Having installed in Python *virtualenv:*
	 - Open command prompt and use: *pip install virtualenv*
2. Change directory to your local repository folder in the command prompt.
3. Create virtual environment: *virtualenv venv*
4. Activate virtual environment: *source venv/bin/activate*
5. Install dependencies:
	- Flask: *pip install flask*
	- Pyrebase: *pip install pyrebase*
	- Dotenv: *pip install -U python-dotenv*
	- Flask CORS: pip install -U flask-cors

## How to configure .env file with the Firebase config

1. Create new file called *env*
2. Edit file and write:
	FIREBASECONFIG =  {
		"apiKey":  "apiKey",
		"authDomain":  "authDomain",
		"databaseURL":  "databaseURL",
		"projectId":  "projectId",
		"storageBucket":  "storageBucket",
		"messagingSenderId":  "messagingSenderId",
		"appId":  "appId",
		"measurementId":  "measurementId"
	}
3. Change the words between " ": *[apiKey]* (not deleting " ") with the real configuration in YATAM Firebase page -> Configuration -> Firebase SDK snipett CDN.
4. Change filename from env to .env
5. .gitignore file would ignore this file to upload it, but do not try to add it to the commit...


## How to "Write" in the project
* Commits messages and code in English
* Code in snake_case NOT camelCase
* Use PEP-8 style guide for Python https://www.python.org/dev/peps/pep-0008/
    * Adding two empty lines before a function
    * Adding three empty lines before 'main'
    * Adding whitespace between # and text in comments
    * Removing redundant parentheses
    * Etc.
    

## Flask HTTP methods
https://pythonbasics.org/flask-http-methods/