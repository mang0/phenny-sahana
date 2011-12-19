INSTALLATION & CONFIGURATION:

1) Run ./phenny - this creates a default config file
2) Edit ~/.phenny/default.py
3) Run ./phenny - this now runs phenny with your settings

LOGGING:

On first run, phenny will create a directory in which to store logs (by defult, ~/.phenny/logs/). This is editable in the /modules/loggy.py file, line 34.

The bot will log all channels it's a user of, unless otherwise specified in /modules/loggy.py.

GREETING: Data stored about nicks which have already been greeted is stored as a sqlite3 database (nick-server.greet.db).

The greet module sends a welcome NOTICE message to users the first time they join a channel. This welcome message is stored in ~/.phenny/nick-server.greet.txt. The first line of this file is the welcome message, with %s replaced by the new users nick - (Do not remove %s from the message.)

The subsequent lines in the file are a list of nicks to ping when a new user joins the channel for the first time. By defult this is OFF, with no nicks in the ping list. Add ONE nick per line, and make sure there are no trailing newlines or whitespaces after the pinglist nicks (if ON) or after the welcome message (if OFF).

Data stored about nicks which have already been greeted is stored as an sqlite3 database (nick-server.greet.db). Only remove this file if you want to start over with which nicks have been greeted and which nicks haven't.

OTHER:

See Phenny's creator's page on all other phenny commands:

http://inamidst.com/phenny/

Enjoy!

-- 
Jacob Warring Eytle, http://www.fruitbowlstudios.blogspot.com/p/about-me.html
