#!/usr/bin/env puppet
# Change the OS configuration so that it is possible to login with the holberton user and
# open a file without any error message.

exec { 'increase-hard-file-limit-for-holberton-user':
  command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}

exec { 'increase-soft-file-limit':
  command  => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}
