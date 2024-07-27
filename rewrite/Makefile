#	'ensure that formatted text option in draw.io is disabled everywhere'

SRC=../orig/py0d.py
#SRC=test.py

all:
	./0D/das2json/das2json t2t.drawio
	./0D/das2json/das2json 0D/python/std/transpile.drawio
	python3 main.py . 0D/python ${SRC} main t2t.drawio.json transpile.drawio.json

#########

# to install required libs, do this once
install-js-requires:
	npm install ohm-js yargs prompt-sync
