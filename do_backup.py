#! /usr/bin/env python

import subprocess

sources = [
    'nwyper@remote:/home/nwyper',
    'nwyper@remote:/etc'
]

dst = '.'

print 'Backing up into "%s"' % dst

for src in sources:
  print 'Synchronizing from "%s"' % i
  command = ("rsync -aRzv --delete -e 'ssh -i /home/nwyper/.ssh/id_dsa' {} {}"
          .format(src, dest))

  process =  subprocess.Popen(command, shell=True)
  process.wait()
  
