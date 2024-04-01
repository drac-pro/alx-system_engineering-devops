package { 'nginx':
  ensure => installed
}

file_line { 'custom_header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'http {',
  line   => 'add_header X-Served-By "$::hostname"'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
