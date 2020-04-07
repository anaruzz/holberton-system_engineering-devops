# Script that Installs and configures nginx


package { 'nginx':
ensure => present,
}

service {'start nginx':
ensure  => running,
}

exec {'configure and restart':
provider => shell,
command  => 'sed -i -e "/sendfile/i \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
}
