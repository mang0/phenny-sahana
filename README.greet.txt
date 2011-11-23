The greet module creates a file (nick-server.greet.txt) in the .phenny folder in your home directory.

The first line of this file is the message that new users are greeted with. %s is substituted with the user's nick.

All subsequent lines are nicks to ping when a new user joins. To avoid pinging anyone, ensure that the file is
only one line long, with no trailing newline.

======
Data stored about nicks which have already been greeted is stored as a sqlite3 database (nick-server.greet.db).
