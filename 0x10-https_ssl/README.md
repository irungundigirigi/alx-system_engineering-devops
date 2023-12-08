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
## No loophole in your web traffic
A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

Requirements:

    This should be transparent to the user
    HAproxy should return a 301
    HAproxy should redirect HTTP traffic to HTTPS
    Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)

The file 100-redirect_http_to_https must be your HAproxy configuration file

Example:

sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$

