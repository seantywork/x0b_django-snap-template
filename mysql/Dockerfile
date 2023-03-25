FROM mysql
MAINTAINER seantywork@gmail.com

ENV MYSQL_ROOT_PASSWORD youdonthavetoknow
ENV MYSQL_HOST localhost

EXPOSE 3306

ADD ./words_alpha.csv /var/lib/mysql-files/
ADD ./init.sql /docker-entrypoint-initdb.d
     
