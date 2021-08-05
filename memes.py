import requests
from textblob import TextBlob
import random

def get_three_memes():
   
    #top memepages are picked randomly
    bestmemes_pages = ['wholesomemems', 'dankmemes', 'memes', 'raimimemes', 'cleanmemes']    
    memePage = random.randint(0, len(bestmemes_pages)-1)
    subreddit_name = bestmemes_pages[memePage]
      
     
    #api request is made
    url =  'https://meme-api.herokuapp.com/gimme/' + subreddit_name + '/20'
    response = requests.get(url)
    data = response.json()
      
    
    dict_jpgups = {}
    sorted_ups = {}    
       
    #range of how many memes are called  
    for x in range(0, 15):
     
       jpgLink = data['memes'][x]['url']
       is_nsfw = data['memes'][x]['nsfw']
       title = data['memes'][x]['title']
       subreddit = data['memes'][x]['subreddit']
       ups = data['memes'][x]['ups']
       
       #if post is not nsfw it is put in a dictionary
       if is_nsfw == False:
            dict_jpgups[ups] = jpgLink
            
     
    #sorted based on ups (popularity)
    for i in sorted (dict_jpgups.keys(), reverse=True):
      sorted_ups[i] = dict_jpgups[i]

    #print(sorted_ups)
    
    final_list_memes = list(sorted_ups.values())
#     print(final_list_memes[0])
#     print(final_list_memes[1])
#     print(final_list_memes[2])

    return final_list_memes[0], final_list_memes[1], final_list_memes[2]

   
#get_three_memes()