FROM library/postgres
COPY init.sql /docker-entrypoint-initdb.d/ 
COPY init1.sql /docker-entrypoint-initdb.d/