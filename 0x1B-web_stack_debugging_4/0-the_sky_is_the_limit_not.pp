# Increases the amount of requests an nginx server can handle


# Increases the Ulimit of default file
exec { 'fix-for-nginx':
    # Modify the ULIMIT value
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    # Specify the path for the sed command
    path    => '/usr/local/bin/:/bin/',
}

#  Restart nginx
exec { 'restart-nginx':
    # Restart nginx services
    command => '/etc/init.d/nginx restart',
    # Specify the path to the init.d script
    path    => '/etc/init.d/',
}
