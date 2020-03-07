from pycrunch_tracer.api.tracing import Yoba

def d___():
    a = 1
    b = 2
    c = 3

def c___():
    a = 1
    b = 2
    d___()
    c = 3


def b___():
    a = 1
    c___()
    b = 2
    c = 3



def a___():
    a = 1
    b = 2
    b___()
    c = 3




y = Yoba()
y.start('demo_tree')

a___()

y.stop()
for (x, cmd) in enumerate(y.command_buffer):
    print(str(x+1) + ' - line:' + str(cmd.cursor.line) + ':' + str(cmd))