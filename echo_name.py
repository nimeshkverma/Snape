#!/usr/bin/python

import pprint

name = raw_input("What\'s your name?\n")
name = name.strip()
#pprint.pprint(ranu)
#exit()
flag = 1;
while flag :	
	if not name:
		name = raw_input("What\'s your name?\n")
		name = name.strip()
	else :
		flag = 0
data = { 
"a" : '''
 AA  
A  A 
AAAA 
A  A 
A  A     
''',
"b" : '''
BBBB  
B   B 
BBBB  
B   B 
BBBB      
''',
"c" : '''
 CCC 
C    
C    
C    
 CCC     
''',

"d" : '''
DDD  
D  D 
D  D 
D  D 
DDD      
''',

"e" : '''
EEEE 
E    
EEE  
E    
EEEE     
''',

"f" : '''
FFFF 
F    
FFF  
F    
F        
''',

"g" : '''
 GGG  
G     
G  GG 
G   G 
 GGG      
''',

"h" : '''
H  H 
H  H 
HHHH 
H  H 
H  H      
''',

"i" : '''
III 
 I  
 I  
 I  
III     
''',

"j" : '''
    J 
    J 
    J 
J   J 
 JJJ      
''',

"k" : '''
K  K 
K K  
KK   
K K  
K  K      
''',

"l" : '''
L    
L    
L    
L    
LLLL     
''',

"m" : '''
M   M 
MM MM 
M M M 
M   M 
M   M      
''',

"n" : '''
N   N 
NN  N 
N N N 
N  NN 
N   N     
''',

"o" : '''
 OOO  
O   O 
O   O 
O   O 
 OOO      
''',

"p" : '''
PPPP  
P   P 
PPPP  
P     
P         
''',

"q" : '''
 QQQ   
Q   Q  
Q   Q  
Q  QQ  
 QQQQ       
''',

"r" : '''
RRRR  
R   R 
RRRR  
R R   
R  RR     
''',

"s" : '''
 SSS  
S     
 SSS  
    S 
SSSS      
''',

"t" : '''
TTTTTT 
  TT   
  TT   
  TT   
  TT       
''',

"u" : '''
U   U 
U   U 
U   U 
U   U 
 UUU      
''',

"v" : '''
V     V 
V     V 
 V   V  
  V V   
   V        
''',
"w" : '''
W     W 
W     W 
W  W  W 
 W W W  
  W W   
''',

"x" : '''
X   X 
 X X  
  X   
 X X  
X   X     
''',

"y" : '''
Y   Y 
 Y Y  
  Y   
  Y   
  Y        
''',

"z" : '''
ZZZZZ 
   Z  
  Z   
 Z    
ZZZZZ      
'''
}
res = ''
for i in name :
	if i == ' ' :
		res = res + '\n'
	else :
		res = res + data[i]
print res
exit()
