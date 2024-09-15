## Lab #3 - Creating & Connecting to a Postgres DB
### Pre-Lab
1. Open your `cmpt221` repository in Github and click `sync fork` > `update branch`

2. Open your `cmpt221` repository in VSCode and open your terminal. Please refer to README.md for instructions on how to do this. 
3. In your terminal, issue a git switch to switch to the main branch:
    ```bash
    # switch to main branch
    git switch main
    ```
4. Issue a git pull to pull any changes from your remote repository into your local repository
    ```bash
    git pull --no-edit
    ```
5. Create a branch for lab 3
    ```bash
    git checkout -b "lab-3" 
    ```

### Lab
In order to connect to a database, you need to _have_ a database. We'll be creating our database in Postgres, so go ahead and download pgAdmin4: https://www.pgadmin.org/download/

Open the application and follow the set-up instructions. You'll have to set a password for the user `postgres`. **Remember this password.** Once you're set up, you can create your database by following these instructions:

1. Click on the `Servers` dropdown, then the `PostgreSQL 16` dropdown.

2. Right click on `Databases`, click `Create`, then click `Database`

3. Name the database `marist` and leave the owner as `postgres`. Click `Save`

Now that you have a database, you have to connect it to your code. We'll be using `Flask` and `SQLAlchemy` to connect our database. 

`Flask` is a micro web framework. A web framework enables developers to write web applications without having to worry about low-level things (such as protocols). Flask is considered a micro web framework because it doesn't require specific tools and libraries, and doesn't have the features a typical web framework (like django) would have. However, flask supports extensions, like SQLAlchemy, that can add some of the features that other web frameworks provide inherently.

`SQLAlchemy` is a database toolkit for python. As an object relational mapper (ORM), SQLAlchemy converts python objects into database objects. It also enables developers to insert, manipulate, and delete data in a database by executing SQL from python modules and scripts.

Flask and SQLAlchemy are both python packages that need to be installed with `pip`.

First things first, though... you need a virtual environment. Create a virtual environment in the `lab-3` directory using the same steps you followed in lab 2:

Navigate to your lab-3 directory using the `cd` command
```bash
cd /labs/lab-3
```

and create your virtual environment
```bash
# create virtual environment
virtualenv .venv
# or use this command if you get a command not found error
python3 -m virtualenv .venv
```

Once you have created your virtual environment and you see the `.venv` directory in your lab-3 folder, activate your virtual environment using whatever command worked for you in lab2 
```bash
# mac
. .venv/bin/activate

# windows
source .venv/Scripts/activate
# or 
.venv/Scripts/activate.bat
# or 
.venv/Scripts/activate.ps1
```

You'll know your virtual environment is activated when you see `(.venv)` in your terminal.
```bash
(.venv) calistaphippen@calistas-mac lab-3 %
```

I've gone ahead and provided you with the requirements.txt file for this lab. All you need is to run a `pip install`, and all the python packages you need (flask, sqlalchemy, psycopg2, dotenv) will be installed.

```bash
pip install -r requirements.txt
```

**IMPORTANT**: If you run the code in this lab while your virtual environment is not activated, _it will fail_.

To connect to your new database, you'll have to provide the database name, the database owner, and your password. 

We are using the database owner `postgres`, and the database you created earlier is named `marist`.

However, you don't necessarily want this information available for the world to see (especially your password). To hide this information, create a `.env` file.

**A `.env` file is a hidden file used to store configuration settings and environment variables that you don’t want shared/seen in your code.** When you create and use a `.env` file, you have to make sure that `.env` is included in your `.gitignore`. I've already done this for you, but if you want to take a look, check out line 27 in the repo .gitignore file.

Create a new file in the lab-3 directory and name it `.env`. Copy and paste the following code into your .env file, replacing \<your password> with the password you created when you went through the pgAdmin4 set up steps and \<your name> with your full name.

```bash
db_name = marist
db_owner = postgres
db_pass = <your password>
name = <your name>
```
These values will be substituted into the database connection code after they have imported in by the `dotenv` module.

So, you add your variables to your `.env` file and no one can see them except you. Those variables are then imported into your code using the `dotenv` package, which references the variables by their `key` (think key = value syntax).

Review the code in the `db.py` module, but do not change anything. After reviewing the code, run the `app.py` script.  

```bash
python3 app.py
# or
python app.py
```

If you have successfully connected to your database, you will see the following message in your terminal:
```bash
---------- Connection successful!
 * Serving Flask app 'db'
 * Debug mode: on
``` 

**SUBMISSION:** Lastly, create a text file named `output.txt`, then copy the success message you see in your terminal and paste it into `output.txt`.

Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace.

```bash
git add .
git commit -m "completed lab 3"
git push --set-upstream origin lab-3
# or
git push
```

Don't forget to deactivate your virtual environment!
```bash
deactivate
# or
.venv/Scripts/deactivate.bat
```