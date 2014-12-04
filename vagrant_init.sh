echo "creating user 'vagrant'"
sudo -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'password';"

echo "creating database 'farmerbrown'"
sudo -u postgres /usr/bin/createdb --echo --owner=vagrant farmerbrown

echo "migrating models"
sudo -u vagrant python /projects/farmtest/manage.py migrate
sudo -u vagrant python /projects/farmtest/manage.py makemigrations

echo "populating database"
#sudo -u vagrant psql farmerbrown < /projects/farmerbrown.sql
sudo -u vagrant python /projects/farmtest/manage.py populate

echo "creating superuser 'admin' for django admin panel, default password = 'password'"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'password')" | python /projects/farmtest/manage.py shell

