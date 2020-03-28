# Creates a file
file { '/tmp/holberton':
  ensure  => present,
  path    => '/tmp/holberton',
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
}
