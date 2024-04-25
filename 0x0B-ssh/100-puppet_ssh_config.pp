# Ensure the SSH client configuration file exists

file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
    Host 388261-web-01
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
  ",
}
