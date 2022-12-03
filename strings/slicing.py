
#s="hello Myself Muskan"
#m_name=s[6:12]
#f_name=s[:5]
#l_name=s[13:19]
#print(m_name)
#print(f_name)
#print(l_name)

name="Muskan Sonker"
fname=name[:6]
lname=name[7:]
#print(fname)
#print(lname)
#revname=name[::-1]
#print(revname)
#evenName=name[::2]
#print(evenName)
oddName=name[1::2]
#print(oddName)

msg='''The New Mexico Territory was an organized incorporated territory of the 
United States from September 9, 1850, until January 6, 1912. 
The territory was created from the U.S. provisional government of New Mexico, 
a result of Santa Fe de Nuevo México becoming part of the American frontier
after the Treaty of Guadalupe Hidalgo. It existed with varying boundaries until
the territory was admitted to the Union as the state of New Mexico. 
This illustration, created by Henry Mitchell for State Arms of the Union, published by Louis
Prang in 1876, depicts the territory's coat of arms, adopted by legislation in 1887:
"The coat of arms of the territory of New Mexico shall be the Mexican Eagle grasping a serpent in its beak,
the cactus in its talons, shielded by the American eagle with outspread wings, and grasping arrows in its talons.'''

print(" length of message is ",len(msg))
#first 100 char
print(msg[:100])
print("stop 100")
#last 200 char
print(msg[-200:])# this -200 will print till the end of -200
print("stop -200")
#every 10th char
print(msg[::10])
print("stop 10th")
#all expect first 100 char and last 100 char
print(msg[100:-100])
print("stop 100,-100")
