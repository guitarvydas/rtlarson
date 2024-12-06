#	'ensure that formatted text option in draw.io is disabled everywhere'

all: scanner

scanner: scanner.drawio.json py0d.py
	python3 main.py . ../0D/python "" main scanner.drawio.json

py0d.py: ../../rt/generated.py
	cp ../../rt/generated.py ./py0d.py

scanner.drawio.json: ../scanner.drawio.json
	cp ../scanner.drawio.json .

../scanner.drawio.json:
	(cd .. ; make)

## house-keeping

clean:
	rm -rf *.json
	rm -rf *~
	rm -rf __pycache__

install-js-requires:
	npm install yargs prompt-sync

