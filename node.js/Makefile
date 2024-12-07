#	'ensure that formatted text option in draw.io is disabled everywhere'

all: scanner

scanner: scanner.drawio.json generated.mjs
	cat generated.mjs main.mjs >scanner.mjs
	node scanner.mjs "." "-" "-" main scanner.drawio.json

generated.mjs: ../../rt/generated.mjs
	cp ../../rt/generated.mjs ./generated.mjs

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
