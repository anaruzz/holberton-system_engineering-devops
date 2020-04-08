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
$new_config = "\trewrite \^\/redirect_me\/\$ https:\/\/www.youtube.com\/watch\?v=QH2-TGUlwu4 permanent\;"
$conf_file = "/etc/nginx/sites-enabled/default"
$server = "0,/server\s+\{/s//& \n"

exec {'redirect_me':
provier => shell,
command => 'sudo sed -i -E "${server}${new_config}/" $conf_file',
}
