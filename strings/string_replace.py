msg='''One day while the Emperor, 
who was devoted to the worship of Apollo,
was consulting at a shrine of that god 
upon an affair of much importance, 
from the dark depths of the cavern came 
forth a voice saying, "The just who are
on the earth keep me from telling the truth. 
By them the inspiration of the Sacred Tripod
is made a lie." At once the Emperor was
stricken with consternation and asked who
these just people were. "Master," answered
one of the priests of Apollo, "they are
the Christians." This answer so enraged 
Diocletian that he rekindled his 
persecutions.
'''
#replace--> it will replace the sequence where the string find
msg2=msg.replace('the','THE')
#print(msg2)

msg3=msg.replace('of','**',3)
print(msg3)
