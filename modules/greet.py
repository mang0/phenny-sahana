#!/usr/bin/env python
"""
greet.py - Phenny Sahana-Eden Greet Module
(c) 2011 Nolan Lum <nol888@gmail.com>
"""

import os, re
import sqlite3

def setup(self):
    fn = self.nick + '-' + self.config.host + '.greet.db'
    fn = os.path.join(os.path.expanduser('~/.phenny'), fn)

    self.g_conn = sqlite3.connect(fn)
    self.g_conn.execute("""CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(60) PRIMARY KEY)""")

    fn = self.nick + '-' + self.config.host + '.greet.txt'
    fn = os.path.join(os.path.expanduser('~/.phenny'), fn)
    if not os.path.exists(fn):
        try: f = open(fn, 'w')
        except OSError: pass
        else:
            f.write('Welcome to #sahana-eden, %s!\nptressel')
            f.close()

    try:
        f = open(fn, 'r')
        self.g_greet = f.readline().strip()
        self.g_pingList = []
        line = f.readline()

        while line:
            self.g_pingList.append(line.strip())
            line = f.readline()
    except OSError: pass

def f_join(phenny, input):
    if input.nick == phenny.nick:
        return

    cur = phenny.g_conn.cursor()
    cur.execute("SELECT name FROM users WHERE name = ?", (input.nick,))
    if not cur.fetchone():
        phenny.msg(input.sender, phenny.g_greet % (input.nick))
        if phenny.g_pingList:
            phenny.msg(input.sender, ', '.join(phenny.g_pingList) + ': ping');
        cur.execute("INSERT INTO users VALUES (?)", (input.nick,))
        phenny.g_conn.commit()

f_join.priority = 'low'
f_join.event = 'JOIN'
f_join.rule = r'(.*)'
f_join.thread = False
