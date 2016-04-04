PY = pypy3

default:
	./update.py
	$(PY) gen-snapshot.py extensions.p
	$(PY) convert.py | sed s'/python3/$(PY)/' >allegory
	chmod +x allegory
