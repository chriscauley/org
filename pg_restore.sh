for d in disney nrgher pmrg turtlebadges;
do
    createdb $d --username=postgres;
    psql --username=postgres $d < backup$d;
done;
