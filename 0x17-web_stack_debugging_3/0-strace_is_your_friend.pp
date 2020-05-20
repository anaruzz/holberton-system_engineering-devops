# fixe a line in a configuration file
exec {'configurate file':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
provider => 'shell',
}