#	'ensure that formatted text option in draw.io is disabled everywhere'

D2J=./das2json/mac/das2json

all: scanner.drawio.json

scanner.drawio.json: scanner.drawio
	${D2J} scanner.drawio

