# increase number of limited open files in a server
exec { 'change_number':
  command =>'sed -i \'s/15/5000/g\' etc/default/nginx',
  path    =>['/bin'],
}
exec {'reload_nginx':
  command =>'service nginx restart',
  path    =>['/bin'],
}
