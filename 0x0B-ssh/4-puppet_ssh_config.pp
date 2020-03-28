# Changes SSH config file
exec {'~/.ssh/holberton':
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path    => '/bin/',
  }
