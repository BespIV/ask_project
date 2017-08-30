sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE USER 'admin'@'localhost'"
sudo mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('pass111')"
sudo mysql -uroot -e "CREATE DATABASE mybase"
sudo mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'@'localhost'"
