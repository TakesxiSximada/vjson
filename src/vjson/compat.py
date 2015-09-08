# -*- coding: utf-8 -*-
import six

if six.PY3:
    from functools import lru_cache
else:
    from functools32 import lru_cache
