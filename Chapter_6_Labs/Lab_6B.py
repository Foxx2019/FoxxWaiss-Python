print('YOU HAVE BEEN BIRTHED!!!')
weekends = {'Jan' : [6,7,13,14,20,21,27,28,'yeet','yeet'], 'Feb' : [3,4,10,11,17,18,24,25,'yeet','yeet'], 'Mar' : [3,4,10,11,17,18,24,25,31,'yeet'], 'Apr' : [1,7,8,14,15,21,22,28,29,'yeet'], 'May' : [5,6,12,13,19,20,26,27,'yeet','yeet'], 'Jun' : [2,3,9,10,16,17,23,24,30,'yeet'], 'Jul' : [1,7,8,14,15,21,22,28,29,'yeet'], 'Aug' : [4,5,11,12,18,19,25,26,'yeet','yeet'], 'Sept' : [1,2,8,9,15,16,22,23,29,30], 'Oct' : [6,7,13,14,20,21,27,28,'yeet','yeet'], 'Nov' : [3,4,10,11,17,18,24,25,'yeet','yeet'], 'Dec' : [1,2,8,9,15,16,22,23,29,30]}
monthlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
month = input("What is your month of birth? (first three letters) - ")
day = int(input("What day? - "))
print("So your 2018 birthday is "+str(monthlist.index(month)+1)+"/"+str(day)+"/18")
if day == weekends[month][0] or day == weekends[month][1] or day == weekends[month][2] or day == weekends[month][3] or day == weekends[month][4] or day == weekends[month][5] or day == weekends[month][6] or day == weekends[month][7] or day == weekends[month][8] or day == weekends[month][9]:
    print("Your birthday's on a weekend this year, HUZZAH! may you live another year.")
else:
    print("Your birthday's not on a weekend in this great year of 2018")
