#!/usr/bin/env python

#startup on start
# setup GPIO 
# watch for a button to be pressed
#if not loop back

#button was pressed
#start wireless network

# collect the files into an archive

#wait for it to connect to the adhoc network 
# you did configure that right?

#connected now
#get our IP address from connection

#take the first 3 octets x.y.z
# append .1

# run a scan from .1 to .255 looking for alive hosts
# create a collection of these

# walk through each open host looking for the open port
# create a collection of these

# walk through this list and attempt a handshake
# if we get one, connect, transfer the archive

# move onto the next host (should we do this?)

# delete the archive
# shutdown the wifi
# go back to monitoring for the button press
