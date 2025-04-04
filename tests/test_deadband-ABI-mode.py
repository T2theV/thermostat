import cffi
import importlib
import pytest

ffi = cffi.FFI()

includes = open("../src/deadband/deadband.h").read()
includes = includes.replace(r'#include <stdint.h>',"")
ffi.cdef("""
""" +
includes)

C = ffi.dlopen("./deadband.so")

@pytest.mark.parametrize("max",range(0,10)) #250))
@pytest.mark.parametrize("min",range(0,10)) #250))
@pytest.mark.parametrize("hysteresis", range(1,3)) #10))
def test_deadband_init(max,min,hysteresis):
    teststruct = ffi.new("struct DBND_struct *")
    testOK = C.DBND_initDeadband(teststruct , max, min, hysteresis)
    
    goldeneval1 = bool(max-hysteresis >= min)
    eval2 = testOK == 0

    assert goldeneval1 == eval2 
