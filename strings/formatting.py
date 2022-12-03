msg="Journey Before Destination"

msg_upr=msg.upper()
msg_lwr=msg.lower()
msg_cap=msg.capitalize()
msg_ttl=msg.title()
msg_swp=msg.swapcase()
msg_cf=msg.casefold()#same as lower()

print(msg)
print(msg_upr)
print(msg_lwr)
print(msg_cap)
print(msg_ttl)
print(msg_swp)
print(msg_cf)

#Align
print(msg.ljust(100,'_'))
print(msg.rjust(100))
print(msg.center(100))

#Alignment with f-strings or PADDING
print(f"{msg.rjust(50)}")
print(f"{msg:>50}")#same as rjust
print(f"{msg:<50}")#same as ljust
print(f"{msg:^50}")#same as center

