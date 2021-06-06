# script to export data_clean, recreate db + reload data
echo "step 0: rename previous export files "
rename .\data_archive\db.json  db_%time:~0,2%%time:~3,2%%time:~6,2%_%date:~-10,2%%date:~-7,2%%date:~-4,4%.txt
echo "step 1: export data ........."
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > ./data_archive/db.json
echo "step 2: delete current database file........."
rem rm -rf db.sqlite3 && rm -rf main/migrations
del /f /q db.sqlite3
del /f /q main\migrations\*
echo "step 3: generate migrations"
python manage.py makemigrations main
echo "step 4: run migrations"
python manage.py migrate
echo "step 5: reload previous data"
python manage.py loaddata ./data_archive/db.json
echo "step 6: create superusers"
python manage.py createsuperuser