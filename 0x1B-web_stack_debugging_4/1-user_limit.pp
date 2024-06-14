# Enable user holberton to login and access files without error

# increase hard file limit for holberton user

exec { 'increase-hard-file-limit-for-holberton-user':
    command => "sed -i '/^holberton hard/s/5/60000/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/,
}

# increase soft file limit for holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
    command => "sed -i '/^holberton soft/s/4/60000/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/,
}
