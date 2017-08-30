sudo /etc/init.d/mysql start
mysql -u root -e "CREATE USER 'box'@'localhost'"
mysql -u root -e "SET PASSWORD FOR 'box'@'localhost' = PASSWORD('pass111')"
mysql -u root -e "CREATE DATABASE mybase"
mysql -u root -e "GRANT ALL ON mybase.* TO 'box'@'localhost'"