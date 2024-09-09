
import csv

customers = open('customers.csv', 'r')

csv_obj = csv.reader(customers)

next(csv_obj)

for rec in csv_obj:

    outfile = open('customer_country.csv','a')

    Name = rec[1] + " " + rec[2]
    Country = rec[4]
    
    outfile.write(Name+','+ Country+'\n')
        
    outfile.close()
    
 