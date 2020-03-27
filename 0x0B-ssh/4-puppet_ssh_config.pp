# Changes SSH config file
file_line {'~/.ssh/config':
ensure  => 'present',
path    => '~/.ssh/config',
mode    => '0744',
  content => 'Host 35.237.161.240\nUser ubuntu\IdentityFile ~/.ssh/holberton\nPasswordAuthentication no'
}
