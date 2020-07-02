# increase number of limited open files in a server
exec { 'change_number':
  command =>'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/g" /etc/default/nginx',
  path    =>['/usr/bin', '/bin'],
}
exec {'reload_nginx':
  command =>'sudo service nginx reload',
  path    =>['/usr/bin', '/bin'],
}
exec {'restart_nginx':
  command =>'sudo service nginx restart',
  path    =>['/usr/bin', '/bin'],
}
