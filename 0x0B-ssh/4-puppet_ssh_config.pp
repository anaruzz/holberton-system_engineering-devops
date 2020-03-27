# Changes SSH config file
file_line { ~/.ssh/holberton:
  ensure            => present,
  path              => '~/.ssh/config',
  match_for_absence => true,
  mode    => '0744',
  content => 'Host 35.237.161.240\nUser ubuntu\IdentityFile ~/.ssh/holberton\nPasswordAuthentication no'
}
