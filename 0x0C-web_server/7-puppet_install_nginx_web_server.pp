#setup ubuntu

exec { 'update system':
       command => '/usr/bin/apt-get update',
}

package { 'nginx':
        ensure => 'installed',
	require => Exec['update system'],
}

file { '/var/www/html/index.html':
       ensure  => file, 
       content => 'Hello World!',
       require => Package['nginx'],
}

exec { 'redirect_me':
       command => '/bin/sed -i \'/listen 80 default_server/a \ \ \ rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;\' /etc/nginx/sites-available/default',
       provider => 'shell',
       require  => Package['nginx'],
       notify   => Service['nginx'],
}

service { 'nginx':
        ensure => running,
	enable => running,
	subscribe => Exec['redirect_me'],

}