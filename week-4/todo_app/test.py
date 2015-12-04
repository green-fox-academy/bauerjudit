import csv
with open('teszt.csv', 'w', newline='') as csvfile:
   spamwriter = csv.writer(csvfile, delimiter=' ',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
   data = [['Spam', 'Lovely Spam', 'Wonderful Spam'],['Spam', 'Lovely Spam', 'Wonderful Spam']]
   spamwriter.writerow(data)


with open('names.csv', 'w') as csvfile:
   fieldnames = ['first_name', 'last_name']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

   writer.writeheader()
   writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
   writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
   writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

   
