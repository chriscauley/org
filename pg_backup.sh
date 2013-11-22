for d in disney nrgher pmrg turtlebadges;
do
    pg_dump $d --username=postgres>backup_$d
done;
