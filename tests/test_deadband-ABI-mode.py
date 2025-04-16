import cffi
import pytest

ffi = cffi.FFI()

includes = open("../src/deadband/deadband.h").read()
includes2 = open("test_build_c/gating.h").read()
includes = includes + includes2
includes = includes.replace(r'#include <stdint.h>',"")
includes = includes.replace(r'#ifndef GATING_H_',"")
includes = includes.replace(r'#define GATING_H_',"")
includes = includes.replace(r'#endif  // GATING_H_',"")

ffi.cdef("""
""" +
includes)

testing = ffi.dlopen("./gating.so",ffi.RTLD_GLOBAL)
C = ffi.dlopen("./deadband.so",ffi.RTLD_GLOBAL)

@pytest.mark.parametrize("max",range(0,3))#250))
@pytest.mark.parametrize("min",range(0,3))#250))
@pytest.mark.parametrize("hysteresis", range(1,10))
def test_deadband_init(max,min,hysteresis):
    teststruct = ffi.new("struct DBND_struct *")
    testing.setGatingStatus(0);
    testOK = C.DBND_initDeadband(teststruct , max, min, hysteresis)

    goldeneval1 = bool(max-hysteresis >= min)
    eval2 = testOK == 0

    assert goldeneval1 == eval2 

@pytest.mark.parametrize("max",range(0,3))#250))
@pytest.mark.parametrize("min",range(0,3))#250))
@pytest.mark.parametrize("hysteresis", range(1,10))
def test_deadband_init_1(max,min,hysteresis):
    teststruct = ffi.new("struct DBND_struct *")
    testing.setGatingStatus(1)
    testOK = C.DBND_initDeadband(teststruct , max, min, hysteresis)

    assert testOK == -128