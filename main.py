#!/usr/bin/env python

import logging

def main():
  logging.basicConfig(filename='/var/log/executioner/executioner.log', level=logging.INFO, format='%(asctime)s %(message)s')


if __name__ == "__main__":
  main()
