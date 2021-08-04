import csv
from operator import itemgetter


def leaderboard_data(data_input):
   with open('score_keep.csv', 'a', newline='') as csvfile:
      wr = csv.writer(csvfile, dialect='excel')
      wr.writerow(data_input)

         
def sort_score_list():
   with open('score_keep.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    unsorted_data = []
    change_toInt = []
    for row in readCSV:
      change_toInt = [row[0], row[1], row[2], row[3]]
      unsorted_data.append(change_toInt)
      
#     print(unsorted_data)
#     print(sorted(unsorted_data, key=itemgetter(3), reverse=True))
      
   sorted_list = sorted(unsorted_data, key=itemgetter(3), reverse=True)
   return sorted_list

      
def reset_score_sheet():
   f = open('score_keep.csv', "w+")
   f.close()
   

liste = ['name1', 5, 1, 13.58]
list2 = ['name2', 6, 2, 10.2]

leaderboard_data(liste)
leaderboard_data(list2)

print(sort_score_list())

#reset_score_sheet()