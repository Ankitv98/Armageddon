from CardCreator import *
from CardSender import *
from InformationSave import *

import _thread

_thread.start_new_thread(CardSender, ())
_thread.start_new_thread(InfoSave, ())
CardCreator()