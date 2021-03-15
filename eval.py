import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction
import math

"""
    --------------------------------------------------------------
"""

BUBBLE = "34"
SPEECH_IN = "1446"
SPEECH_OUT = 1314


COMMAND = "!eval "


COLOR_IN = "@A17676@"
COLOR_OUT = "@1F808E@"
COLOR_ERROR = "@E10230@"

"""
    --------------------------------------------------------------
"""


extension_info = {
    "title": "Eval",
    "description": COMMAND,
    "version": "2.0",
    "author": "Lande"
}

ext = Extension(extension_info, sys.argv)
ext.start()


def speech(message):
    (text, color, index) = message.packet.read('sii')

    if text.startswith(COMMAND):
        message.is_blocked = True
        calc = text[6:]
        if calc:
            try:
                result = str(eval(calc))
                ext.send_to_client('{l}{h:'+SPEECH_IN+'}{i:0}{s:"'+COLOR_IN+' Input : '+str(calc)+' "}{i:0}{i:'+BUBBLE+'}{i:0}{i:0}')
                ext.send_to_client('{l}{h:'+SPEECH_IN+'}{i:0}{s:"'+COLOR_OUT+' Output : '+result+' "}{i:0}{i:'+BUBBLE+'}{i:0}{i:0}')
            except:
                ext.send_to_client('{l}{h:'+SPEECH_IN+'}{i:0}{s:"'+COLOR_ERROR+' Something wrong "}{i:0}{i:'+BUBBLE+'}{i:0}{i:0}')
        else:
            ext.send_to_client('{l}{h:'+SPEECH_IN+'}{i:0}{s:"'+COLOR_ERROR+' No arg "}{i:0}{i:'+BUBBLE+'}{i:0}{i:0}')


ext.intercept(Direction.TO_SERVER, speech, SPEECH_OUT)
