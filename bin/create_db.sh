#!/bin/bash

mysql -uroot -e "CREATE DATABASE qa; CREATE USER 'qa'@'%' IDENTIFIED BY '123456'; GRANT ALL PRIVILEGES ON qa.* TO 'qa'@'%';"

