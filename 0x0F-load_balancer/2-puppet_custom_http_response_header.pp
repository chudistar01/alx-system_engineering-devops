#ubuntu server setup

exec { 'update system':
       command => '/usr/bin/apt-get update',
}

package { 'nginx':
	  ensure => 'installed',
	  require => Exec['update system'],
}

file {'/var/www/html/index.html':
	ensure => 'present',
	content => 'Hello World!',
	require => Package['nginx'],
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://github.com/chudistar01/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell',
	require => Package['nginx'],
}

exec { 'HTTP header':
       command => 'sed -i "25i\		add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
       provider => 'shell',
       require => Exec['redirect_me'],
}

service { 'nginx':
	  ensure => running,
	  enable => true,
	  require => Package['nginx']
}