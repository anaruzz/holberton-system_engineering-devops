# Script that Installs and configures nginx

# Update packages and install nginx
exec {'update packages, install nginx':
path    => '/usr/bin/:/usr/sbin/:/bin/',
command => 'sudo apt-get -y update && sudo apt-get -y install nginx',
}

# Change index page
exec {'change default index page content':
provider => shell,
command  => 'echo "Holberton School" > /var/www/html/index.nginx-debian.html && sudo service nginx restart',
}

#start nginx
exec {'start nginx':
path    => '/usr/bin/:/usr/sbin/:/bin/',
command => 'sudo service nginx start',
}

#place redirect function
exec {'redirect_me':
provier => shell,
command => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/watch\?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
