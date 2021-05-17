.PHONY: all clean extension $(CMAKE_BUILD_DIR)/ds3patch

CMAKE_BUILD_DIR = modengine_extension_build
CMAKE_SOURCE_DIR = src/modengine_extension

SRC_DIR = src
DIST_DIR = dist
PYTHON ?= python
CMAKE ?= cmake
CP ?= cp
STEAMWORKS_SDK ?= H:\\Development\workspace\sdk
MODENGINE_SDK ?= H:\Development\workspace\dark-souls-3\modengine2\installroot
EMEVD_SOURCES = $(wildcard src/event/*.py)
EMEVD_BINARIES = $(EMEVD_SOURCES:$(SRC_DIR)/%.py=$(DIST_DIR)/%.emevd.dcx)

all: $(EMEVD_BINARIES) extension
extension: $(CMAKE_BUILD_DIR)/ds3patch

$(EMEVD_BINARIES): $(DIST_DIR)/%.emevd.dcx: $(SRC_DIR)/%.py
	@echo Compiling $@ from $<
	$(PYTHON) compile.py --source $< --output $@

$(CMAKE_BUILD_DIR)/build.ninja: $(CMAKE_SOURCE_DIR)/CMakeLists.txt
	$(CMAKE) \
 		-DCMAKE_PREFIX_PATH="$(MODENGINE_SDK)\share\cmake" \
 		-DSTEAMWORKS_SDK="$(STEAMWORKS_SDK)" \
 		-S $(<D) -B $(@D) -G "Ninja"

$(CMAKE_BUILD_DIR)/ds3patch: $(CMAKE_BUILD_DIR)/build.ninja
	ninja -C $(@D) $(@F)
	@-mkdir "dist\native"
	$(CP) "$(CMAKE_BUILD_DIR)\ds3patch.dll" "dist\native\ds3patch.dll"