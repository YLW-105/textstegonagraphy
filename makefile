help:
	@echo embedding secret message: make embed ARGS="textfile secretMessage"
	@echo extracting: make extract ARGS="coverMessage"
	@echo key: 1 space for 0s, 2 space for 1s

embed:
	@python3 embed.py $(ARGS)

extract:
	@python3 extract.py $(ARGS)
