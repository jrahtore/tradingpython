from pyomo.environ import *
from bulk_update_or_create import BulkUpdateOrCreateQuerySet
import bulk_update_or_create
from .models import UserTransaction
import pandas as pd

import datetime

def test():
    print('HELLO')
