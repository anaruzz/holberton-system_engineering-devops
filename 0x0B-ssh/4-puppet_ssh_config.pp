# Changes SSH config file
file {'~/.ssh/holberton':
ensure  => 'present',
path    => '/etc/ssh/ssh_config',
content => 'Host 35.237.161.240\nUser ubuntu\IdentityFile ~/.ssh/holberton\nPasswordAuthentication no',
}
