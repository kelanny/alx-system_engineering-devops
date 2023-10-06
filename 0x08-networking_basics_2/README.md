PROJECT: 0x08. Networking basics #1
DevOps Network SysAdmin
By: Sylvain Kalache


Resources
Read or watch:

What is localhost
What is 0.0.0.0
What is the hosts file
Netcat examples
man or help:

ifconfig
telnet
nc
cut
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is localhost/127.0.0.1
What is 0.0.0.0
What is /etc/hosts
How to display your machine’s active network interfaces

TASKS: 

TASK: 0. Change your home IP
mandatory
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

localhost resolves to 127.0.0.2
facebook.com resolves to 8.8.8.8.
The checker is running on Docker, so make sure to read this
In this example we can see that:

before running the script, localhost resolves to 127.0.0.1 and facebook.com resolves to 157.240.11.35
after running the script, localhost resolves to 127.0.0.2 and facebook.com resolves to 8.8.8.8
If you’re running this script on a machine that you’ll continue to use, be sure to revert localhost to 127.0.0.1. Otherwise, a lot of things will stop working!

TASK: 1. Show attached IPs
mandatory
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

TASK: 2. Port listening on localhost
Write a Bash script that listens on port 98 on localhost.

