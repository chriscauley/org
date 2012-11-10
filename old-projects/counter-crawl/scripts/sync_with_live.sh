rsync -avz -e ssh webapp@iac.mouthwateringmedia.com:/home/webapp/django-projects/iac/static/uploads/ ../static/uploads/

scp webapp@iac.mouthwateringmedia.com:/home/webapp/django-projects/iac/scripts/backups/d1.dump backups/d1.dump

dropdb iac --username=postgres
createdb iac --username=postgres
createlang plpgsql iac --username=postgres
psql iac --username=postgres< backups/d1.dump