import cffi
import importlib
import pytest

def makedeadbandlib():
    source_code = open("../src/deadband/deadband.c").read()
    includes = open("../src/deadband/deadband.h").read()

    includes = includes.replace(r'#include <stdint.h>',"")
    source_code = source_code.replace(r'#include "deadband.h"', includes)

    ffibuilder = cffi.FFI()
    ffibuilder.cdef("""
                    """ 
                    + includes)
    ffibuilder.set_source("_DBND", source_code)
    ffibuilder.compile()

    module = importlib.import_module("_DBND")
    return module

mod_DBND = makedeadbandlib()
modffi = mod_DBND.ffi
modlib = mod_DBND.lib

@pytest.mark.parametrize("max",range(0,250))
@pytest.mark.parametrize("min",range(0,250))
@pytest.mark.parametrize("hysteresis", range(95,100))
def test_deadband_init(max,min,hysteresis):
    teststruct = modffi.new("struct DBND_struct *")
    testOK = modlib.DBND_initDeadband(teststruct , max, min, hysteresis)
    
    goldeneval1 = bool(max-hysteresis >= min)
    eval2 = testOK == 0

    assert goldeneval1 == eval2 
