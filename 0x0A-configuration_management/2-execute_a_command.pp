# 2-execute_a_command.

# Execute pkill to terminate a process called killmenow
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
}
