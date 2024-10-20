#	'ensure that formatted text option in draw.io is disabled everywhere'

D2J=./das2json/mac/das2json

all: scanner

scanner: scanner.drawio py0d.py
	${D2J} scanner.drawio
	python3 main.py . 0D/python "" main scanner.drawio.json

py0d.py: ../rt/generated-py0d.py
	cp ../rt/generated-py0d.py ./py0d.py

## house-keeping

clean:
	rm -rf *.json
	rm -rf *~
	rm -rf __pycache__

install-js-requires:
	npm install yargs prompt-sync

