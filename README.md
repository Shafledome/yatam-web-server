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
