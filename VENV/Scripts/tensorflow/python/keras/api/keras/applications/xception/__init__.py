# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Xception V1 model for Keras.

On ImageNet, this model gets to a top-1 validation accuracy of 0.790
and a top-5 validation accuracy of 0.945.

Reference:
  - [Xception: Deep Learning with Depthwise Separable Convolutions](
      https://arxiv.org/abs/1610.02357) (CVPR 2017)


"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.keras.applications.xception import Xception
from tensorflow.python.keras.applications.xception import decode_predictions
from tensorflow.python.keras.applications.xception import preprocess_input

del _print_function

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.applications.xception", public_apis=None, deprecation=True,
      has_lite=False)