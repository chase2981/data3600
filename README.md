  ```
   40  pip install virtualenv
   41  virtualenv venv
   42  . venv/bin/activate
   43  git status
   44  pip install flask
   45  echo "web: gunicorn app:app" > Procfile
   46  python3 -m pip install gunicorn==20.0.4
   47  python3 -m pip freeze > requirements.txt
   48  git status
   49  git add . 
   50  git commit -am "progress"
   51  git status
   52  git push
 ```
 
 then connect repo to heroku and deploy
 
 or run
 
 ```
 flask --debug run --host=0.0.0.0 
 ```
 
 if on ec2 instance and do the security groups to allow port 5000 and visit it that way
 
 
 
 