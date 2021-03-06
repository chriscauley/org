#!/bin/bash

export DB_BACKUP="/home/webapp/django-projects/iac/scripts/backups"

mv $DB_BACKUP/d3.dump $DB_BACKUP/d4.dump
mv $DB_BACKUP/d2.dump $DB_BACKUP/d3.dump
mv $DB_BACKUP/d1.dump $DB_BACKUP/d2.dump

pg_dump iac --username=postgres>$DB_BACKUP/latest.dump

if [ `date +u%` == 0 ]
then
    mv $DB_BACKUP/w3.dump $DB_BACKUP/w4.dump
    mv $DB_BACKUP/w2.dump $DB_BACKUP/w3.dump
    mv $DB_BACKUP/w1.dump $DB_BACKUP/w2.dump
    cp $DB_BACKUP/latest.dump $DB_BACKUP/w1.dump
fi

exit 0
