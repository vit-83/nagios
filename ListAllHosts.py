from pynag import Model

# Get all hosts
all_hosts = Model.Host.objects.all
for i in all_hosts:
  print i.host_name, i.contacts

