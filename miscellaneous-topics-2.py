### str is used to convert things into string.

## Statement       Result
## str(37)         '37'
## str(3.14)       '3.14'
## str([1,2,3])    '[1,2,3]

### int function converts something into integers.
### float function converts something into floating point number.

## Statement      Result
## int('37')       37
## float('3.14')   3.14
## int(3.14)       3
# list(range(5))   [0,1,2,3,4]
# list('abc')      ['a','b','c']

## Example 1:find palindromic numbers.
for i in range(1,500):
    s=str(i)
    if s==s[::-1]:
        print(s)

## Example 2
birthday = 'January 1, 2003'
year = int(birthday[-4:])
print('You are', 2024-year, 'years old.')

## Example 3
## By for loop.

num=(39)
digit = str(num)
answer = 0
for i in range(len(digit)):
    answer = answer + int(digit[i])
print(answer)

## By List comprehension.
num=(19)
answer = sum([int(c) for c in str(num)])
print(answer)

'''
### 10.2 Booleans
Are basic data type in programming represents by two possible values: True or False
'''
## if game_over:           ==       if game_over==True:
## while not game_over:    ==       while game_over==False:

### 10.3 Shortcuts
# Statement         Shorthand
# count=count+1      count+=1
# total=total-5      total-=5
# prod=prod*2        prod*=2
## There are also shortcut operators /=, %=, //=, and **=.
# a=0
# b=0      it's shortcut a=b=c=0
# c=0

# num=(10,20,30,40,50)
# a=num[0]=10
# b=num[1]=20
# c=num[2]=30  its shortcut is   a,b,c,d,e=1,2,3,4,5
# d=num[3]=40
# e=num[4]=50

## Shortcut with conditions.
# Statement                              Shortcut
# if a==0 and b==0 and c==0:             if a==b==c==0:
# if 1<a and a<b and b<5:                if 1<a<b<5:

# ### 10.5 Continuation(\)
# string=input('Enter string.')
# if 'a' in string or 'e' in string or 'i' in string \
#     or 'o' in string or 'u' in string:
#         print('You use \'Vowel\' letter.')

# ### 10.7 String formatting
