#puppet script
exec { 'increase_nginx_ulimit':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => ['/usr/local/bin', '/bin', '/usr/bin'],
    unless => 'grep -q "4096" /etc/default/nginx',
}

#Restart_nginx
exec { 'restart_nginx':
   command => 'service nginx restart',
   path   => ['usr/sbin', '/sbin'],
}