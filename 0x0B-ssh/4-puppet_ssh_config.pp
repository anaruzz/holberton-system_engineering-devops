# Changes SSH config file
file {'~/.ssh/holberton':
ensure  => 'present',
path    => '/etc/ssh/ssh_config',
content => 'PasswordAuthentication no\nIdentityFile ~/.ssh/holberton',
}
