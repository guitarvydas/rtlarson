#	'ensure that formatted text option in draw.io is disabled everywhere'

ARG=""

strippeddown: scanner.drawio.json rtpy0d.py
	python3 main.py . 0D/python ${ARG} 'main' scanner.drawio.json

full: scanner.drawio.json
	python3 main-full.py . 0D/python ${ARG} 'main' scanner.drawio.json

scanner3.drawio.json:
	./0D/das2json/das2json scanner3.drawio

scanner.drawio.json:
	./das2json/mac/das2json-x86_64 scanner.drawio

rtpy0d.py : ../rt/rtpy0d.py
	cp ../rt/rtpy0d.py .


#########

# to install required libs, do this once
install-js-requires:
	npm install ohm-js yargs prompt-sync
