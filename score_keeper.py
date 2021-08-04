import csv
from operator import itemgetter


def leaderboard_data(data_input):
   with open('score_keep.csv', 'a') as csvfile:
   
     fieldnames = ['name', 'score', 'amount', 'percent']
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         
     for row in data_input:
        writer.writerow({'name': row[0], 'score': row[1], 'amount': row[2], 'percent': row[3]})

         
def sort_score_list():
   with open('score_keep.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    unsorted_data = []
    change_toInt = []
    for row in readCSV:
      change_toInt = [row[0], int(row[1]), int(row[2]), float(row[3])]
      unsorted_data.append(change_toInt)
      
#     print(unsorted_data)
#     print(sorted(unsorted_data, key=itemgetter(3), reverse=True))
      
   sorted_list = sorted(unsorted_data, key=itemgetter(3), reverse=True)
   return sorted_list

      
def reset_score_sheet():
   f = open('score_keep.csv', "w+")
   f.close()
   

#liste = [['name1', 5, 1, 13.58], ['name2', 7, 10, 45.68], ['name3', 1, 10, 90.48]]   

#leaderboard_data(liste)

#sort_score_list()

#reset_score_sheet()