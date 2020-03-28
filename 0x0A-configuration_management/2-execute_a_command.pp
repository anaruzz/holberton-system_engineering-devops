# Execute a command
exec { 'pkill':
  command => 'pkill --full killmenow',
  path    => '/usr/bin/',
}
