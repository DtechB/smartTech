<p align="center">
  
  <h1 align="center">SmartTech / Smart Technology</h1>
  
  <p align="center">
    <i style="margin-top: 10px; display: block;">
    A unique website with many features that introduces users to the latest phones and leads them to the best with the best offer.
    </i>
  </p>
  
  <hr style="border: 1px solid #00ff00ff;">
</p>

![](sample%20pic/main.png)

## ⚙️ Config the project
### After cloning project in your computer first of all you should make venv for this project.
```
python -m venv venv
```
Now you should activate your venv.
So in the main root of project you should type this command in your Terminal or Console:
### In Linux/macOS:
```
source venv/bin/activate
```
### In windows:
```
./venv/Scripts/activate
```

### After activating venv you should install the <b>requirements.txt</b> packages. So type this command in your Terminal or Console:
```
pip install -r requirements.txt
```

### Then rename env.sample to .env and fill up empty fields (email, password, google auth)
for more details about google auth please read this [Docs](https://support.google.com/googleapi/answer/6158862?hl=en).

## ⚙️ Config the database
### In smartTech/settings.py in databse section import your own information (USER, PASSWORD) and create database called smarttech in your local databse

### If config all above then type this command in your Terminal or Console:
```
python manage.py migrate
```

Configuration of database almost done.

### After migrate and create tables in databse then insert data to your smarttech database 
go to folder /smartTech Data/ and insert data based on the following pattern:
<ul>
  <li>smarttech_mainpage_smartphone.sql</li>
  <li>smarttech_mainpage_smartphonedescription.sql</li>
  <li>smarttech_mainpage_smartphoneimgurl.sql</li>
  <li>smarttech_mainpage_offer.sql</li>
  <li>smarttech_mainpage_post.sql</li>
  <li>smarttech_mainpage_postdescription.sql</li>
</ul>

## 🏁 Run the project
### Run the project by typing this command in your Terminal or Console:
```
python manage.py runserver
```

### if you didn't see any errors congratulations, you ran the project correctly ✅
### Now copy/paste this address in your browser URL bar:
```
http://127.0.0.1:8000/
```
OR
```
http://localhost:8000/
```

### If you want to access database by admin default of django type this command in your Terminal or Console:
```
python manage.py createsuperuser
```
and then set username and password and go to http://localhost:8000/admin finally login and enjoy

### POINT: If in windows python command doesn't work try with py

## Sample view of this website
### Login page
![](sample%20pic/login.png)

### Smartphone page
![](sample%20pic/phones.png)

### Blog page
![](sample%20pic/blog.png)

### Profile page
![](sample%20pic/account.png)

### Comparison page
![](sample%20pic/comparison.png)
