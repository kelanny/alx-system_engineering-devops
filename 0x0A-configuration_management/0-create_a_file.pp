# Ensure the /tmp/school directory exists.

file { '/tmp':
    ensure => 'directory',
}

# Create the file with specified content, permission
# owner and group.

file { '/tmp/school':
    ensure  => 'file',
    content => 'I love Puppet and dogs. How about that.',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
