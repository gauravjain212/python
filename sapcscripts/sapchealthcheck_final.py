from subprocess import Popen, PIPE, check_output, STDOUT
import ConfigParser, os
from os.path import exists as file_exists
import datetime
import pexpect
#os.environ['LINES'] = "25"
#os.environ['COLUMNS'] = "80"

def execute_external_cmd(cmd,f_out):
    f_out.write('-- '+str(cmd)+' command start\n\n')
    child.sendline(cmd)
    child.expect("PL-3:~ #")
    output=child.before
    f_out.write(output+'\n')
    f_out.write('-- '+str(cmd)+' command end\n\n\n\n')

def execute_cliss(server,cmd,f_out):
    f_out.write('-- '+str(cmd)+' command start\n\n')
    child.sendline(cmd)
    child.expect(">")
    output=child.before
    f_out.write(output+'\n')
    f_out.write('-- '+str(cmd)+' command end\n\n\n\n')

def execute_cmd(cmd):
    process = Popen(cmd,shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stderr, stdout

current_datetime =datetime.datetime.now()
current_date= current_datetime.strftime('%Y%m%d')
out_file="output_{}.txt".format(current_date)
if file_exists(out_file):
   os.remove(out_file)
f_out=open(out_file,'w')
configur = ConfigParser.ConfigParser()
configur.read('config.ini')
noraml_cmd=configur.items('normal')
print(noraml_cmd)
for cmds in noraml_cmd:
    cmd = cmds[1]
    print(cmd)
    error, output = execute_cmd(cmd)
    if len(error) == 0:
        f_out.write('-- '+str(cmd)+' command start\n\n')
        f_out.write(output+'\n')
        f_out.write('-- '+str(cmd)+' command end\n\n\n\n')
    else:
        f_out.write('-- '+str(cmd)+' :Command Failed\n\n')
        f_out.write(error+'\n')
        f_out.write('-- '+str(cmd)+' command end\n\n\n\n')

connection_error="Connection to COM failed."
sucess= ">"
#os.environ['LINES'] = "25"
#os.environ['COLUMNS'] = "80"        
cliss_cmd=configur.items('cliss')
child = pexpect.spawn('ssh SC-1')
#os.environ['LINES'] = "25"
#os.environ['COLUMNS'] = "80"
child.setwinsize(44,157)
child.expect('SC-1:~ #')
child.sendline('cliss')
child.delaybeforesend = None
i = child.expect([connection_error,sucess])

if i==0:
    print("connection to SC-1 Failed")
    child = pexpect.spawn('ssh SC-2')
    #rows, cols = map(int, os.popen('stty size', 'r').read().split())
    child.setwinsize(44,157)
    child.expect('SC-2:~ #')
    child.sendline('cliss')
    i = child.expect([connection_error,sucess])
    if i==1:
        server="SC-2:~ #"
        for cmds in cliss_cmd:
            cmd = cmds[1]
            print(cmd)
            execute_cliss(server,cmd,f_out)
        child.sendline('exit')
        child.expect(server)
elif i==1:
    print("connection Success")
    server="SC-1:~ #"
    for cmds in cliss_cmd:
        cmd = cmds[1]
        print(cmd)
        execute_cliss(server,cmd,f_out)
    child.sendline('exit')
    child.expect(server)

child = pexpect.spawn('ssh PL-3')
child.expect('PL-3:~ #')
external_cmd=configur.items('external')
for cmds in external_cmd:
    cmd = cmds[1]
    print(cmd)
    execute_external_cmd(cmd,f_out)
f_out.close()