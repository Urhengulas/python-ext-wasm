from wasm import Instance, Value
import os

__dir__ = os.path.dirname(os.path.realpath(__file__))

bytes = open(__dir__ + '/memory.wasm', 'rb').read()
instance = Instance(bytes)
pointer = instance.call('return_hello')

memory = instance.memory_view(pointer)
nth = 0;
string = '';

while (0 != memory.get(nth)):
    string += chr(memory.get(nth))
    nth += 1

print('"' + string + '"') # "Hello, World!"
