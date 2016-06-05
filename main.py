#!/usr/bin/env python

import logging
from listener import Listener

def main():
  logging.basicConfig(filename='/var/log/executioner/executioner.log', level=logging.INFO, format='%(asctime)s %(message)s')
  listener = Listener()
  listener.start()

if __name__ == "__main__":
  main()
