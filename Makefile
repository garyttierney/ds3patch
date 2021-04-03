.PHONY: all clean

SRC_DIR = src
DIST_DIR = dist
PYTHON ?= venv/Scripts/python

EMEVD_SOURCES = $(wildcard src/event/*.py)
EMEVD_BINARIES = $(EMEVD_SOURCES:$(SRC_DIR)/%.py=$(DIST_DIR)/%.emevd.dcx)

all: $(EMEVD_BINARIES)

$(EMEVD_BINARIES): $(DIST_DIR)/%.emevd.dcx: $(SRC_DIR)/%.py
	@echo Compiling $@ from $<
	$(PYTHON) compile.py --source $< --output $@
