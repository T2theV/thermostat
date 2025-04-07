import cffi
import importlib
import pytest

ffi = cffi.FFI()

includes = open("../src/deadband/deadband.h").read()
includes = includes.replace(r'#include <stdint.h>',"")
ffi.cdef("""
void setGate(int value);
""" +
includes)

tb = ffi.dlopen("./gating.so",ffi.RTLD_GLOBAL)
C = ffi.dlopen("./deadband.so")

@pytest.mark.parametrize("max",range(0,5))# 250))
@pytest.mark.parametrize("min",range(0,5))#250))
@pytest.mark.parametrize("hysteresis", range(1,3))#10))
def test_deadband_init_1(max,min,hysteresis):
    tb.setGate(1)
    teststruct = ffi.new("struct DBND_struct *")
    testOK = C.DBND_initDeadband(teststruct , max, min, hysteresis)
    
    goldeneval1 = bool(max-hysteresis >= min)
    eval2 = testOK == 0

    assert goldeneval1 == eval2 

@pytest.mark.parametrize("max",range(0,5))# 250))
@pytest.mark.parametrize("min",range(0,5))#250))
@pytest.mark.parametrize("hysteresis", range(1,3))#10))
def test_deadband_init_2(max,min,hysteresis):
    tb.setGate(0)
    teststruct = ffi.new("struct DBND_struct *")
    testOK = C.DBND_initDeadband(teststruct , max, min, hysteresis)
    
    goldeneval1 = bool(max-hysteresis >= min)
    eval2 = testOK == 0

    assert goldeneval1 == eval2 
