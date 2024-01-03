# Step 1 : Install and Create a env fiest 



```
pip install virtualenv 
```

```
virtualenv project_env
```

# Step 2: Activate the Env.

```
env\Scripts\activate
```

# Step 3 : Install the requirements using requirements.txt file

```
pip install -r requirements.txt
```

# step 4: Migrate the db 

```
python manage.py migrate
```

# step 5 : Run the server now 

```
python manage.py runserver
```

