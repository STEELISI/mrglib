from mrglib import User, Experiment, Manager
import time
username='shareaa'
passw='89ebb3da'
u = User.User(username, passw)
retcode = u.login()
print("Logged in ", retcode, " username ", u.username)
m = Manager.Manager()
proj = m.find_project(username)
exp = m.create_experiment('testexp', proj.name, 'test description 2')
exp = m.find_experiment('testexp', proj.name)
while exp == None:
    exp = m.find_experiment('testexp', proj.name)
    time.sleep(1)
print("Experiment created")
time.sleep(10)                                                                                                                                                
rev=exp.set_model("/share/education/synflood/synflood.model")
print("Revision ", rev)
time.sleep(10)                                                                                                                                                
exp.lease()                                                                                                                                                   
print("Leased resources")                                                                                                                                     
exp.allocate()                                                                                                                                                
exp.attach()
time.sleep(60)
print("Slept and now will try")
(lines, elines) = exp.exec_on_node(username, "client", "ping -c 3 server")
for line in lines:
    print("Output is ", line)
exp.deallocate()
exp.relinquish()
exp.delete()
