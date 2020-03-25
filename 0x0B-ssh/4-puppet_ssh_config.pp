file_line { ~/.ssh/holberton:
  ensure            => present,
  path              => '/etc/ssh/sshd_config',
  match_for_absence => true,
  mode    => '0744',
  content => 'Host 35.237.161.240\nUser ubuntu\IdentityFile ~/.ssh/holberton\nPasswordAuthentication no'
}
