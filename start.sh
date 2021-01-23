service cron start
python manage.py migrate
crontab <<< '# new crontab'
python manage.py crontab add
python manage.py crontab show
python manage.py runserver 0.0.0.0:8000
