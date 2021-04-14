"""This program will append an ID to the end of each song lyric text file. 
Each ID corresponds to the ID for the respective song in the MySQL database."""

import os
from pprint import pprint

def append_to_file(file, id):
	"""Append ID to last line of the song lyric file"""
	with open(file, 'a+') as file_obj:
		file_obj.write(f'\nSong ID: {id}')


def get_filedict(directory):
	"""Use directory (folder) of song names for respective year
	to create dictionary that we can sort later to ensure that we 
	give each song the correct ranking."""
	dir_dict = {}
	for entry in os.scandir(directory):
		if entry.is_file():
			song = entry.path[len(directory)+1:]
			per_index = song.index('.')
			rank = int(song[0: per_index])
			dir_dict[rank] = entry.path
	return dir_dict


def transfer_to_list(songlist, songdict):
	"""Append the song dictionary values (the paths) to the list in order."""
	for i in sorted (songdict):
		songlist.append(songdict[i])

#All of the directories. There was probably an easier way to do this, but this worked.
directory1 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2006'
directory2 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2007'
directory3 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2008'
directory4 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2009'
directory5 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2010'
directory6 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2011'
directory7 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2012'
directory8 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2013'
directory9 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2014'
directory10 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2015'
directory11 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2016'
directory12 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2017'
directory13 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2018'
directory14 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2019'
directory15 = r'/Users/kennycastle/Documents/GSU Spring 21/Software Engineering CTW/Project/2020'

dict1 = (get_filedict(directory1))
dict2 = (get_filedict(directory2))
dict3 = (get_filedict(directory3))
dict4 = (get_filedict(directory4))
dict5 = (get_filedict(directory5))
dict6 = (get_filedict(directory6))
dict7 = (get_filedict(directory7))
dict8 = (get_filedict(directory8))
dict9 = (get_filedict(directory9))
dict10 = (get_filedict(directory10))
dict11 = (get_filedict(directory11))
dict12 = (get_filedict(directory12))
dict13 = (get_filedict(directory13))
dict14 = (get_filedict(directory14))
dict15 = (get_filedict(directory15))

songlist = []
transfer_to_list(songlist, dict1)
transfer_to_list(songlist, dict2)
transfer_to_list(songlist, dict3)
transfer_to_list(songlist, dict4)
transfer_to_list(songlist, dict5)
transfer_to_list(songlist, dict6)
transfer_to_list(songlist, dict7)
transfer_to_list(songlist, dict8)
transfer_to_list(songlist, dict9)
transfer_to_list(songlist, dict10)
transfer_to_list(songlist, dict11)
transfer_to_list(songlist, dict12)
transfer_to_list(songlist, dict13)
transfer_to_list(songlist, dict14)
transfer_to_list(songlist, dict15)

pprint(songlist)

i=1
for path in songlist:
	append_to_file(path, i)
	i+=1

