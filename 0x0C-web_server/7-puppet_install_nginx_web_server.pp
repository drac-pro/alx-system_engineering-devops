# install and configure nginx

package { 'nginx':
  ensure => installed
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://github.com/drac-pro permanent;'
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
