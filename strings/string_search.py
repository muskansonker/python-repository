#find--> find will give the substring starting index.
# index--> it will give error if the sub string not found
# rfind--> reverse find is same as the find().

msg="The quick brown fox jumped over the lazy dog."
idx=msg.find('own')
if idx!=1:
    print(f'Found "own" at index {idx}')
else:
    print('Not Found "own"')

idx=msg.find('owl')
if idx!=1:
    print(f'found "owl" at index {idx}')
else:
    print('Not found "owl"')

idx= msg.rfind('brown',11)
print(idx)

