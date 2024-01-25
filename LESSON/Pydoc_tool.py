#! /usr/bin/python3

'''

Pydoc ==> Python Documentation Tool
-----------------------------------

	python3 -m pydoc [FILE NAME / MODULE NAME]									--->	show documentation on shell.
	python3 -m pydoc -k [KEYWORD IN FILE / MODULE] [FILE NAME / MODULE NAME]	--->	search through documentation by keywords.
	python3 -m pydoc -n [HOST NAME] [FILE NAME / MODULE NAME]					--->	show documentation on web through desired host name (default: localhost).
	python3 -m pydoc -p [PORT NUMBER] [FILE NAME / MODULE NAME]					--->	show documentation on web through desired port number. Port no. 0 will use random unused port.
	python3 -m pydoc -b [FILE NAME / MODULE NAME]								--->	show documentation on web through localhost and port (combination of -n and -p).
	python3 -m pydoc -w [FILE NAME / MODULE NAME]								--->	show documentation on HTML and also save the file to its default directory.

'''