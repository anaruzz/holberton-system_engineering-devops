# increase number of limited open files in a server
exec { 'change_limit':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/15/3000/g' /etc/default/nginx; sudo service nginx restart",
provider => 'shell',
}
