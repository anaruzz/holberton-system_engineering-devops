# Script that Installs and configures HAproxy

package {'install nginx':
ensure => present,
}

service {'start nginx':
ensure  => running,
}

exec {'configure and restart':
provider => shell,
command  => 'host=$(hostname); sudo sed -i -e "/sendfile/i \\\tadd_header X-Served-By \"$host\";" /etc/nginx/nginx.conf && sudo service nginx restart',
}
