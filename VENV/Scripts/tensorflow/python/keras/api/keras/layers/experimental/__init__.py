# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Public API for tf.keras.layers.experimental namespace.
"""

from __future__ import print_function as _print_function

import sys as _sys

from . import preprocessing
from tensorflow.python.keras.layers.einsum_dense import EinsumDense
from tensorflow.python.keras.layers.kernelized import RandomFourierFeatures

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.layers.experimental", public_apis=None, deprecation=True,
      has_lite=False)
