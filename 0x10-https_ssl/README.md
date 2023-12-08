## 0-world wide web
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

    Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
    Add the subdomain lb-01 to your domain, point it to your lb-01 IP
    Add the subdomain web-01 to your domain, point it to your web-01 IP
    Add the subdomain web-02 to your domain, point it to your web-02 IP
    Your Bash script must accept 2 arguments: 
## Haproxy SSL Termination
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

Requirements:

    HAproxy must be listening on port TCP 443
    HAproxy must be accepting SSL traffic
    HAproxy must serve encrypted traffic that will return the / of your web server
    When querying the root of your domain name, the page returned must contain Holberton School
    Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)

