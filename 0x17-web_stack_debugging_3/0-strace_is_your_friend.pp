# puppet script to fix apache2 returning 500

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
