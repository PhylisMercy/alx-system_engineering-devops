# script to execute a command using puppet
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

