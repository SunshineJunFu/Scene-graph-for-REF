#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 22:36:02
# @Author  : Jun Fu (fujun@mail.ustc.edu.cn)



import os 




def sentence2sg(sentence='man'):


    # print("java sceneParser \"%s\"  tmp" % "young man" )

    os.system("java sceneParser \"%s\"  tmp" % sentence)

    with open('./tmp.txt', 'r') as f:
        lines = f.readlines()
        rl = []
        for i in range(2, len(lines)):
            # case: no relationship #
            if i==2:
                if lines[i] == '\n':
                    # print('no relationship')
                    i = 6
                    break
            #case: have relationship #
            line = lines[i].rstrip('\n').split(' ')

            if len(line) > 1:    
                line =  list(filter(lambda t: t!="", line))
                line[0] = line[0].split('-')[0]
                line[-1] = line[-1].split('-')[0]
                rl.append(line)

            else:
                i = i+4
                break

        attr = {} 
        j = i
        while j < len(lines): # last line \n
            # case: no node #
            if lines[j] =='\n':
                break 

            # case: have node #
            line = lines[j].rstrip('\n').split(' ')
            key = line[0].split('-')[0]

            # check whether have attribute or not #
            k = j + 1
            while k < len(lines):
                if attr.get(key) == None:
                    attr[key] = []

                if lines[k] == '\n': # last line
                    break 

                next_line = lines[k].rstrip('\n').split(' ')
                next_line =  list(filter(lambda t: t!="", next_line)) 
                next_line = next_line[0].split('-')

                if next_line[0]== '':
                    # have attribute 
                    attr[key].append(next_line[1])
                    k = k + 1 # to check next lines
                else:
                    # no attribute or end attribute#
                    break 

            j = k 

    
        print(rl, attr)      

if __name__ == '__main__':

    # case 1: only one node and some attributes #
    sentence2sg('blue yellow man')

    # case2: no node and no relationship #
    sentence2sg('man')

    # case3:  no attribute and have relationship #
    sentence2sg('a man with ball')       

    # case3:  have attribute and have relationship #
    sentence2sg('a handsome man with a silver ring is holding a phone')       