# install and configures nginx

package { 'nginx':
  ensure => installed
}

file_line { 'redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://github.com/drac-pro permanent;',
  require => Package['nginx']
}

file_line { 'custom_header':
  ensure  => 'present',
  path    => '/etc/nginx/nginx.conf',
  after   => 'http {',
  line    => "add_header X-Served-By \"${hostname}\";",
  require => Package['nginx']
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
