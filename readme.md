# How to install the project
Create a virtual environment
```
virtualenv -p python environment
```
Activate the virtual environment
```
source environment/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
Create a .env
```
cp example.env .env
```
Edit the new .env file.

Run migrations
```
python src/api/manage.py migrate
```
Run the project
```
python src/api/manage.py runserver
```