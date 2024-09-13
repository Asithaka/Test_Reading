import csv

steps = open('steps.csv', 'r')

st_obj = csv.reader(steps)

next(st_obj)

my_dict = {'1' : 'January',
          '2' : 'February',
          '3' : 'March',
          '4' : 'April',
          '5' : 'May',
          '6' : 'June',
          '7' : 'July',
          '8' : 'Augest',
          '9' : 'September',
          '10': 'Octomber',
          '11': 'November',          
          '12': 'December'}

my_list = ['1','2','3','4','5','6','7','8','9','10','11','12']

rows = list(st_obj)

for rec in my_list:

    counter = 0
    total   = 0
  
    for line in rows: 
                
            if  line[0] == rec:

                Month = my_dict[rec]   

                counter += 1

                total   +=  int(line[1])
            
    avg_step = total/counter

           # else:

            #    break    
              
    #print( f"{Month}"+'- ' + str(f"{avg_step: ,.2f}, {counter},{total}") )

    print( f"{Month}"+'- ' + str(f"{avg_step: ,.2f}") )







  