# Script that Installs and configures nginx


package { 'nginx':
ensure => present,
}

service {'start nginx':
ensure  => running,
}

exec {'configure and restart':
provider => shell,
command  => 'host=$(hostname);nl="\\\tadd_header X-Served-By \"$host\";";sudo sed -i -e "/sendfile/i $nl" /etc/nginx/nginx.conf;sudo service nginx restart',
}
