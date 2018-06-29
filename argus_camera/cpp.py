# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_argus_camera_cpp', [dirname(__file__)])
        except ImportError:
            import _argus_camera_cpp
            return _argus_camera_cpp
        if fp is not None:
            try:
                _mod = imp.load_module('_argus_camera_cpp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _argus_camera_cpp = swig_import_helper()
    del swig_import_helper
else:
    import _argus_camera_cpp
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _argus_camera_cpp.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _argus_camera_cpp.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _argus_camera_cpp.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _argus_camera_cpp.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _argus_camera_cpp.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _argus_camera_cpp.SwigPyIterator_equal(self, x)

    def copy(self):
        return _argus_camera_cpp.SwigPyIterator_copy(self)

    def next(self):
        return _argus_camera_cpp.SwigPyIterator_next(self)

    def __next__(self):
        return _argus_camera_cpp.SwigPyIterator___next__(self)

    def previous(self):
        return _argus_camera_cpp.SwigPyIterator_previous(self)

    def advance(self, n):
        return _argus_camera_cpp.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _argus_camera_cpp.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _argus_camera_cpp.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _argus_camera_cpp.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _argus_camera_cpp.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _argus_camera_cpp.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _argus_camera_cpp.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _argus_camera_cpp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_argus_camera_cpp.WIDTH_IDX_swigconstant(_argus_camera_cpp)
WIDTH_IDX = _argus_camera_cpp.WIDTH_IDX

_argus_camera_cpp.HEIGHT_IDX_swigconstant(_argus_camera_cpp)
HEIGHT_IDX = _argus_camera_cpp.HEIGHT_IDX

_argus_camera_cpp.ONE_SECOND_NANOS_swigconstant(_argus_camera_cpp)
ONE_SECOND_NANOS = _argus_camera_cpp.ONE_SECOND_NANOS
class ArgusCameraConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ArgusCameraConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ArgusCameraConfig, name)
    __repr__ = _swig_repr
    __swig_getmethods__["DEFAULT_DEVKIT_CONFIG"] = lambda x: _argus_camera_cpp.ArgusCameraConfig_DEFAULT_DEVKIT_CONFIG
    if _newclass:
        DEFAULT_DEVKIT_CONFIG = staticmethod(_argus_camera_cpp.ArgusCameraConfig_DEFAULT_DEVKIT_CONFIG)
    __swig_setmethods__["mDeviceId"] = _argus_camera_cpp.ArgusCameraConfig_mDeviceId_set
    __swig_getmethods__["mDeviceId"] = _argus_camera_cpp.ArgusCameraConfig_mDeviceId_get
    if _newclass:
        mDeviceId = _swig_property(_argus_camera_cpp.ArgusCameraConfig_mDeviceId_get, _argus_camera_cpp.ArgusCameraConfig_mDeviceId_set)
    __swig_setmethods__["mSourceClipRect"] = _argus_camera_cpp.ArgusCameraConfig_mSourceClipRect_set
    __swig_getmethods__["mSourceClipRect"] = _argus_camera_cpp.ArgusCameraConfig_mSourceClipRect_get
    if _newclass:
        mSourceClipRect = _swig_property(_argus_camera_cpp.ArgusCameraConfig_mSourceClipRect_get, _argus_camera_cpp.ArgusCameraConfig_mSourceClipRect_set)
    __swig_setmethods__["mStreamResolution"] = _argus_camera_cpp.ArgusCameraConfig_mStreamResolution_set
    __swig_getmethods__["mStreamResolution"] = _argus_camera_cpp.ArgusCameraConfig_mStreamResolution_get
    if _newclass:
        mStreamResolution = _swig_property(_argus_camera_cpp.ArgusCameraConfig_mStreamResolution_get, _argus_camera_cpp.ArgusCameraConfig_mStreamResolution_set)
    __swig_setmethods__["mVideoConverterResolution"] = _argus_camera_cpp.ArgusCameraConfig_mVideoConverterResolution_set
    __swig_getmethods__["mVideoConverterResolution"] = _argus_camera_cpp.ArgusCameraConfig_mVideoConverterResolution_get
    if _newclass:
        mVideoConverterResolution = _swig_property(_argus_camera_cpp.ArgusCameraConfig_mVideoConverterResolution_get, _argus_camera_cpp.ArgusCameraConfig_mVideoConverterResolution_set)
    __swig_setmethods__["mFrameDurationRange"] = _argus_camera_cpp.ArgusCameraConfig_mFrameDurationRange_set
    __swig_getmethods__["mFrameDurationRange"] = _argus_camera_cpp.ArgusCameraConfig_mFrameDurationRange_get
    if _newclass:
        mFrameDurationRange = _swig_property(_argus_camera_cpp.ArgusCameraConfig_mFrameDurationRange_get, _argus_camera_cpp.ArgusCameraConfig_mFrameDurationRange_set)
    __swig_setmethods__["mSensorMode"] = _argus_camera_cpp.ArgusCameraConfig_mSensorMode_set
    __swig_getmethods__["mSensorMode"] = _argus_camera_cpp.ArgusCameraConfig_mSensorMode_get
    if _newclass:
        mSensorMode = _swig_property(_argus_camera_cpp.ArgusCameraConfig_mSensorMode_get, _argus_camera_cpp.ArgusCameraConfig_mSensorMode_set)

    def getOutputSizeBytes(self):
        return _argus_camera_cpp.ArgusCameraConfig_getOutputSizeBytes(self)

    def getNumChannels(self):
        return _argus_camera_cpp.ArgusCameraConfig_getNumChannels(self)

    def __init__(self):
        this = _argus_camera_cpp.new_ArgusCameraConfig()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _argus_camera_cpp.delete_ArgusCameraConfig
    __del__ = lambda self: None
ArgusCameraConfig_swigregister = _argus_camera_cpp.ArgusCameraConfig_swigregister
ArgusCameraConfig_swigregister(ArgusCameraConfig)

def ArgusCameraConfig_DEFAULT_DEVKIT_CONFIG():
    return _argus_camera_cpp.ArgusCameraConfig_DEFAULT_DEVKIT_CONFIG()
ArgusCameraConfig_DEFAULT_DEVKIT_CONFIG = _argus_camera_cpp.ArgusCameraConfig_DEFAULT_DEVKIT_CONFIG

class ArgusCamera(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ArgusCamera, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ArgusCamera, name)
    __repr__ = _swig_repr
    __swig_getmethods__["createArgusCamera"] = lambda x: _argus_camera_cpp.ArgusCamera_createArgusCamera
    if _newclass:
        createArgusCamera = staticmethod(_argus_camera_cpp.ArgusCamera_createArgusCamera)
    __swig_destroy__ = _argus_camera_cpp.delete_ArgusCamera
    __del__ = lambda self: None

    def read(self, rgba):
        return _argus_camera_cpp.ArgusCamera_read(self, rgba)

    def __init__(self):
        this = _argus_camera_cpp.new_ArgusCamera()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
ArgusCamera_swigregister = _argus_camera_cpp.ArgusCamera_swigregister
ArgusCamera_swigregister(ArgusCamera)

def ArgusCamera_createArgusCamera(config, info=None):
    return _argus_camera_cpp.ArgusCamera_createArgusCamera(config, info)
ArgusCamera_createArgusCamera = _argus_camera_cpp.ArgusCamera_createArgusCamera

# This file is compatible with both classic and new-style classes.


