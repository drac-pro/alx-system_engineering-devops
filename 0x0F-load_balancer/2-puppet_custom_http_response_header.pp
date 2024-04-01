# install and configures nginx

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Package['install Nginx']
}

package { 'nginx':
  ensure => installed
}

file_line { 'custom_header':
  ensure  => 'present',
  path    => '/etc/nginx/nginx.conf',
  after   => 'http {',
  line    => "add_header X-Served-By \"${hostname}\";",
  require => Package['nginx'],
  before  => Service['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
