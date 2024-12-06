#	'ensure that formatted text option in draw.io is disabled everywhere'

all: scanner

scanner: scanner.drawio.json generated.py
	python3 main.py . - "" main scanner.drawio.json

generated.py: ../../rt/generated.py
	cp ../../rt/generated.py ./generated.py

scanner.drawio.json: ../scanner.drawio ../scanner.drawio.json
	(cd ..; make)
	cp ../scanner.drawio.json .

## house-keeping

clean:
	rm -rf *.json
	rm -rf *~
	rm -rf __pycache__

# python3 -m venv ./rt
# source rt/bin/activate
# pip3 install websockets
