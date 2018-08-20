from __future__ import print_function
import sys
import pexpect

# probe username / Device to ping
_username = sys.argv[1]
_probe = sys.argv[2]
_ip = sys.argv[3]

ip_reachable = '{} is alive'.format(_ip)
ip_unreachable = '{} is unreachable'.format(_ip)
my_password = sys.argv[4]
command = "ssh {}@localhost -p {}".format(_username,_probe)
response = "Enter passphrase for key '/home/antons/.ssh/id_rsa': "
ping_command = 'fping {}'.format(_ip)

child = pexpect.spawn(command)
child.expect(response)
if child.match:
    child.sendline(sys.argv[4])

child.expect("Welcome to")
i = child.sendline(ping_command)
child.expect([ip_reachable, ip_unreachable])
print(child.after)
