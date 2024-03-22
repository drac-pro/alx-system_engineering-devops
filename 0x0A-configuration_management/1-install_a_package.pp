#Install flask

exec { 'install pip3':
  command => 'apt-get install -y python3-pip',
  unless  => 'which pip3',
  path    => ['/bin', '/usr/bin'],
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install pip3']
}
