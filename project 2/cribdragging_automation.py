import sys;
import re;
key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.',' '];
#pt = [14,6,31,30,28,12,20,3,30,8,8,7,31,23,18,18,1,4,23,31,28,8,0,0,0,15,17,15,18,15,3,8,10,3,13,21,2,28,8,30,0,26,3,1,30,21,10,28,21,1,26,25,17,4,0,26,7,5,11,29,20,8,31,5,15,10,10,6,1,0,12,15,2,31,3,29,31,17,29,7,4,9,30,8];

pairDict = {
'00000' : ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
'00001' : ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz'],
'00010' : ['ac', 'bd', 'eg', 'fh', 'ik', 'jl', 'mo', 'np', 'qs', 'rt', 'uw', 'vx'],
'00011' : ['ad', 'bc', 'eh', 'fg', 'il', 'jk', 'mp', 'no', 'qt', 'rs', 'ux', 'vw'],
'00100' : ['ae', 'bf', 'cg', 'dh', 'im', 'jn', 'ko', 'lp', 'qu', 'rv', 'sw', 'tx'],
'00101' : ['af', 'be', 'ch', 'dg', 'in', 'jm', 'kp', 'lo', 'qv', 'ru', 'sx', 'tw'],
'00110' : ['ag', 'bh', 'ce', 'df', 'io', 'jp', 'km', 'ln', 'qw', 'rx', 'su', 'tv'],
'00111' : ['ah', 'bg', 'cf', 'de', 'ip', 'jo', 'kn', 'lm', 'qx', 'rw', 'sv', 'tu'],
'01000' : ['ai', 'bj', 'ck', 'dl', 'em', 'fn', 'go', 'hp', 'qy', 'rz'],
'01001' : ['aj', 'bi', 'cl', 'dk', 'en', 'fm', 'gp', 'ho', 'qz', 'ry'],
'01010' : ['ak', 'bl', 'ci', 'dj', 'eo', 'fp', 'gm', 'hn', 'sy', 'tz'],
'01011' : ['al', 'bk', 'cj', 'di', 'ep', 'fo', 'gn', 'hm', 'sz', 'ty'],
'01100' : ['am', 'bn', 'co', 'dp', 'ei', 'fj', 'gk', 'hl', 'uy', 'vz'],
'01101' : ['an', 'bm', 'cp', 'do', 'ej', 'fi', 'gl', 'hk', 'uz', 'vy'],
'01110' : ['ao', 'bp', 'cm', 'dn', 'ek', 'fl', 'gi', 'hj', 'wy', 'xz'],
'01111' : ['ap', 'bo', 'cn', 'dm', 'el', 'fk', 'gj', 'hi', 'wz', 'xy'],
'10000' : ['aq', 'br', 'cs', 'dt', 'eu', 'fv', 'gw', 'hx', 'iy', 'jz'],
'10001' : ['ar', 'bq', 'ct', 'ds', 'ev', 'fu', 'gx', 'hw', 'iz', 'jy'],
'10010' : ['as', 'bt', 'cq', 'dr', 'ew', 'fx', 'gu', 'hv', 'ky', 'lz'],
'10011' : ['at', 'bs', 'cr', 'dq', 'ex', 'fw', 'gv', 'hu', 'kz', 'ly'],
'10100' : ['au', 'bv', 'cw', 'dx', 'eq', 'fr', 'gs', 'ht', 'my', 'nz'],
'10101' : ['av', 'bu', 'cx', 'dw', 'er', 'fq', 'gt', 'hs', 'mz', 'ny'],
'10110' : ['aw', 'bx', 'cu', 'dv', 'es', 'ft', 'gq', 'hr', 'oy', 'pz'],
'10111' : ['ax', 'bw', 'cv', 'du', 'et', 'fs', 'gr', 'hq', 'oz', 'py'],
'11000' : ['ay', 'bz', 'iq', 'jr', 'ks', 'lt', 'mu', 'nv', 'ow', 'px'],
'11001' : ['az', 'by', 'ir', 'jq', 'kt', 'ls', 'mv', 'nu', 'ox', 'pw'],
'11010' : ['is', 'jt', 'cy', 'dz', 'kq', 'lr', 'mw', 'nx', 'ou', 'pv'],
'11011' : ['it', 'js', 'cz', 'dy', 'kr', 'lq', 'mx', 'nw', 'ov', 'pu'],
'11100' : ['ey', 'fz', 'iu', 'jv', 'kw', 'lx', 'mq', 'nr', 'os', 'pt'],
'11101' : ['ez', 'fy', 'iv', 'ju', 'kx', 'lw', 'mr', 'nq', 'ot', 'ps'],
'11110' : ['gy', 'hz', 'iw', 'jx', 'ku', 'lv', 'ms', 'nt', 'oq', 'pr'],
'11111' : ['gz', 'hy', 'ix', 'jw', 'kv', 'lu', 'mt', 'ns', 'pq']
}

unComTri = {'aaj', 'jaj', 'qex', 'zhi', 'aak', 'jaz', 'qfa', 'zhb', 'aax', 'jbo', 'qff', 'zgo', 'abj', 'jbp', 'qfv', 'zgl',
	    'abk', 'jbv', 'qga', 'zge', 'acg', 'jbw', 'qge', 'zfp', 'afd', 'jcn', 'qgh', 'zfl', 'afp', 'jcp', 'qgi',
	    'zfe', 'afx', 'jcq', 'qgk', 'zfc', 'agd', 'jcr', 'qgn', 'zfb', 'agf', 'jct', 'qhe', 'zdt', 'agq', 'jda', 'qhf' 
	    'zdo', 'agv', 'jdd', 'qhn', 'zcr', 'agx', 'jdf', 'qho', 'zcp', 'ahg', 'jdg', 'qia', 'zck', 'ahk', 'jdh',
		 'qib','zcd'}

with open("./dict.txt") as myfile:
    lines = myfile.readlines()
c = 0
enwords = []
for i in range(0,len(lines)):
    if "-" in lines[i]:
        continue
    enwords.append(lines[i].strip())
    #print "'"+enwords[c]+"'"
    c+=1

def index(a):
 for i in range(0,28):
  if key[i]== a: return i;
 return -1;

import bitstring;
from bitstring import BitArray
pt = []
with open("ct3.txt") as f:
    content = f.readlines()

otherthing = [x.strip() for x in content];

for i in range(0,len(otherthing)):
    nums = otherthing[i].split();
    for j in range(0,len(nums)):
        b = BitArray(bin=nums[j]);
        pt.append(b.uint);
        numConv = str(b.uint);
        #print(nums[j]+" "+str(b.uint));
        #line += key[numConv];

from langdetect import detect

import enchant;
d = enchant.Dict("en_US")
baseword=sys.argv[1];
print("Finding: "+baseword+" - len: "+str(len(baseword)));
print("Length of text: "+str(len(pt)))
pt1 = []

for i in range(0,len(pt)):
    pt1.append(0)
word = baseword

for n in range(0,len(enwords)):
    word = baseword+enwords[n]
    print (word)

    for i in range(0,len(pt1)):
        pt1[i] = 0

    for i in range(0,len(pt)-len(word)+1):
        for j in range(0,len(word)):
            try:
                letter = key[index(word[j])^pt[i+j]]
            except IndexError:
                #print ("Error: "+str(i))
                break
            if (j == len(word)-1):
                pt1[i] = 1
    if (0):
        print "Found at pos: ",
        for i in range(0,len(pt1)):
            if (pt1[i] == 1):
                print str(i)+" ",
        print "\n"

    for i in range(0,len(pt1)):
        if (pt1[i] == 1):
            res = ""
            for j in range(0,len(word)):
                res += key[index(word[j])^pt[i+j]]
            strs = res.split()
            for x in range(0,len(strs)):
                if (d.check(strs[x])):
                    #if (len(strs[x]) == 1 and strs[x] != 'a' and strs[x] != 'i'):
                    #    continue
                    print str(i)+"-"+str(i+len(res)-1)+' "'+res+'"'+" - "+"("+strs[x]+")\n",
                    break

sys.exit()  
