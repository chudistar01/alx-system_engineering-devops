#install flask from pip3

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask -v 2.1.0',
  unless  => '/usr/bin/pip3 freeze | grep flask | grep -q "flask==2.1.0"',
  path    => ['/usr/bin', '/bin']
}
