# Install NginX
# With puppet

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

file_line { 'add header' :
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
