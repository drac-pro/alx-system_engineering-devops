# set up your client SSH configuration file so that you can connect to a server without typing a password

file_line { 'ssh key file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}

file_line { 'Deny password authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}
