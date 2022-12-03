ques="What is the capital of India? "
oA="A. Delhi"
oB="B. Lucknow"
oC="C. Goa"
#correct='A'  .............Alternate Method

print("Welcome to the quiz")
print(ques)
print('-'*10)
print(f'a) {oA}') #f is FORMAT and 
print(f'b) {oB}') #for variable we have to use the curly braces
#print('c) {oC}') #if we remove f then it will print as it is
print(f'c) {oC}') 

ans=input('Enter your Answer: ')
if ans=="A" or ans=="a":
#if ans.upper()==correct:  .............Alternate Method
    print('Correct ✅')
else:
    print('Wrong ❌😏')
