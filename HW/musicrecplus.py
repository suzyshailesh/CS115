'''
I pledge my honor that I have abided by the Stevens Honor System.
Susmitha Shailesh working with Rohan Rao
11/11/2018
'''

pref_file = "musicrecplus.txt"

from cs115 import *

def loadUsers(txt):
    '''Loads txt file and adds the information from txt file into a dictionary'''
    dct = {}
    try:
        file = open(txt, 'r')
        for line in file:
            line = line.replace('\n','')
            user, artists = line.split(':')
            dct[user] = artists.split(',')
    except:
        file = open(txt, 'w')
    file.close()
    return dct

def main(txt):
    '''main function. displays first prompt and moves user on to menu'''
    dct = loadUsers(txt)
    user = input("Enter your name (put a $ symbol after your name " +\
                 "if you wish your preferences to remain private):\n")
    if user not in dct:
        dct = enterPreferences(user, dct, txt)
    menu(user, dct, txt)

def menu(user, dct, txt):
    '''endless while loop of displaying menu options and calls various functions
    based on user input'''
    while(True):
        choice = input(\
                    "Enter a letter to choose an option:\n" + \
                    "e - Enter preferences\n" + \
                    "r - Get recommendations\n" + \
                    "p - Show most popular artists\n" + \
                    "h - How popular is the most popular\n" + \
                    "m - Which user has the most likes\n" + \
                    "q - Save and quit\n")
        if choice == 'e':
            dct = enterPreferences(user, dct, txt)
        elif choice == 'r':
            #rec = get_recomendations(user, dct)
            rec = getRec(user, dct)
        elif choice == 'p':
            popArtist(dct)
        elif choice == 'h':
            popLvl(dct)
        elif choice == 'm':
            mostLikes(user, dct)
        elif choice == 'q':
            try:
                savePreferences(user, dct, pref_file, dct[user])
                break
            except:
                break

def getRec(user, dct):
    '''find the closest match of a PUBLIC user, and share new artists with them'''
    publicUsers = []
    users = dct.keys()
    for member in users:
        if member[-1] != '$':
            publicUsers.append(member)
    bestMatch = []
    matchScore = 0
    userPrefs = dct[user]
    '''Find best match'''
    for member in publicUsers:
        prefs = dct[member]
        if prefs != userPrefs:
            matches = i = j = 0
            while i < len(prefs) and j < len(userPrefs):
                if prefs[i] == userPrefs[j]:
                    matches += 1
                    i += 1
                    j += 1
                elif prefs[i] > userPrefs[j]:
                    j += 1
                else:
                    i += 1
            if matches > matchScore:
                matchScore = matches
                bestMatch = [member]
            elif matches == matchScore:
                bestMatch += [member]
    '''Find differences'''
    newArtists = []
    for match in bestMatch:
        i = j = 0
        difference = []
        prefs = dct[match]
        while i < len(prefs):
            if j < len(userPrefs):
                if prefs[i] == userPrefs[j]:
                    i += 1
                    j += 1
                elif prefs[i] > userPrefs[j]:
                    j += 1
                else:
                    difference += [str(prefs[i])]
                    i += 1
            else:
                difference += prefs[i:]
                break
        newArtists += difference
    '''print out recommended artists'''
    newArtists = list(set(newArtists))
    
    newArtists.sort()
    if len(newArtists) == 0:
        print("No recommendations available at this time")
    for artist in newArtists:
        print(artist)

def popArtist(dct):
    '''prints the artist that most users have included in
    their preferences'''
    artists = []
    for user in dct:
        if user[-1] != '$':
            artists += dct[user]
    maxCount = [[],0]
    for artist in artists:
        instances = filter(lambda x: x == artist, artists)
        artistCount = [[artist], len(instances)]
        if artistCount[1] > maxCount[1]:
            maxCount = artistCount
        elif artistCount[1] == maxCount[1]:
            maxCount[0] += artistCount[0]
        artists = filter(lambda x: x != artist, artists)
    if len(maxCount[0]) == 0:
        print("Sorry, no artists found")
    for name in maxCount[0]:
        print(name)

def popLvl(dct):
    '''prints the amount of users prefer the artist that
    is the most popular'''
    artists = []
    for user in dct:
        if user[-1] != '$':
            artists += dct[user]
    maxCount = 0
    for artist in artists:
        instances = filter(lambda x: x == artist, artists)
        artistCount = len(instances)
        if artistCount > maxCount:
            maxCount = artistCount
        artists = filter(lambda x: x != artist, artists)
    if maxCount == 0:
        print("Sorry, no artists found")
    print(maxCount)

def mostLikes(user, dct):
    '''prints which user has the most preferences'''
    publicUsers = []
    users = dct.keys()
    for member in users:
        if member[-1] != '$':
            publicUsers.append(member)
    maxLikes = [[str(user)], len(dct[user])]
    for member in publicUsers:
        if len(dct[member]) > maxLikes[1]:
            maxLikes = [[member], len(dct[member])]
        elif len(dct[member]) == maxLikes[1]:
            maxLikes[0] += [member]
    if len(maxLikes[0]) == 0:
        print("Sorry, no user found")
    else:
        for name in maxLikes[0]:
            print(name)

def enterPreferences(user, dct, txt):
    '''allows user to input new list of artist preferences'''
    artists = []
    newArtist = input("Enter an artist that you like (Enter to finish):\n").title()
    while(newArtist != ''):
        artists += [newArtist]
        newArtist = input("Enter an artist that you like (Enter to finish):\n").title()
    artists.sort()
    dct[user] = artists
    savePreferences(user, dct, txt, artists)
    return dct
    
def savePreferences(user, dct, txt, artists):
    '''saves the file'''
    file = open(txt, 'w')
    sortedUsers = sorted(dct.keys())
    for user in sortedUsers:
        newLine = str(user) + ':' + ','.join(dct[user])
        file.write(newLine + '\n')
    file.close()  
                 
if __name__ == "__main__":
    '''main function'''
    main(pref_file)
