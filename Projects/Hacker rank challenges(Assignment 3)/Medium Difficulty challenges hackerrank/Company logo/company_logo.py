#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

class OrderedCounter(Counter):
    pass

if __name__ == '__main__':
    [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

