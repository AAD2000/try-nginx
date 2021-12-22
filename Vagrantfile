# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.define "nginx_host" do |nginx_host|
    nginx_host.vm.network "private_network", ip: "127.0.0.1"
    nginx_host.vm.network "forwarded_port", guest: 80, host: 80
    nginx_host.vm.provision "shell", inline: <<-SHELL
        echo "
        127.0.0.1 hello.world
        127.0.0.1 www.hello.world
        127.0.0.1 ex.py
        127.0.0.1 www.ex.py" >> /etc/hosts
  	    apt-get install -y nginx
  	    apt-get install fcgiwrap
        mkdir -p /var/www/hello.world/public_html
        chown -R www-data:www-data /var/www/hello.world/public_html
        sudo chmod 755 /var/www
  	  SHELL
  	nginx_host.vm.provision "file", source: "index.html", destination: "/tmp/index.html"
  	nginx_host.vm.provision "file", source: "hello.world", destination: "/tmp/hello.world"
  	nginx_host.vm.provision "shell", inline: <<-SHELL
  	        mv /tmp/index.html /var/www/hello.world/public_html/
  	        mv /tmp/hello.world /etc/nginx/sites-available/
            ln -s /etc/nginx/sites-available/hello.world /etc/nginx/sites-enabled/hello.world
            nginx -t
            service nginx restart
      	  SHELL
  	nginx_host.vm.provision "file", source: "ex.py", destination: "/tmp/ex.py"
  	nginx_host.vm.provision "file", source: "ex.py.conf", destination: "/tmp/ex.py.conf"
  	nginx_host.vm.provision "shell", inline: <<-SHELL
      	    mv /tmp/ex.py.conf /etc/nginx/sites-available/
            ln -s /etc/nginx/sites-available/ex.py.conf /etc/nginx/sites-enabled/ex.py.conf
            nginx -t
            service nginx restart
          SHELL
  end
end
