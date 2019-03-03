#!/bin/bash
export DBNAME=<enter_your_db_name_here>
export DBUSER=<enter_your_db_user_here>
export DBPASS=<enter_your_db_user_pass_here>
psql -U postgres -c "DROP DATABASE $DBNAME;"
psql -U postgres -c "DROP ROLE $DBUSER;"
psql -U postgres -c "CREATE DATABASE $DBNAME;"
psql -U postgres -c "CREATE USER $DBUSER WITH PASSWORD '$DBPASS';"
psql -U postgres -c "ALTER ROLE $DBUSER SET client_encoding TO 'utf8';"
psql -U postgres -c "ALTER ROLE $DBUSER SET default_transaction_isolation TO 'read committed';"
psql -U postgres -c "ALTER ROLE $DBUSER SET timezone TO 'UTC';"
python manage.py makemigrations
python manage.py migrate
cp ./data.sql /tmp/data.sql
psql -U bankuser -d bankdb -a -f '/tmp/data.sql'
rm /tmp/data.sql
