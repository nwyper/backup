#! /usr/bin/env python

import subprocess

sources = [
    'nwyper@remote:/home/nwyper',
    'nwyper@remote:/etc'
]

path = '.'

print 'Backing up into "%s"' % path

for i in sources:
  print 'Synchronizing from "%s"' % i
  command = \
      "rsync -aRzv --delete -e 'ssh -i /home/nwyper/.ssh/id_dsa' %s %s" % \
      (i, path)
  process =  subprocess.Popen(command, shell=True)
  process.wait()
  
