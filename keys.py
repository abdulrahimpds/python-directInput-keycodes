# Define direct key codes for SendInput()
DK_CODE = {
    # Alphabets
    'a': 0x1E, 'A': 0x1E,
    'b': 0x30, 'B': 0x30,
    'c': 0x2E, 'C': 0x2E,
    'd': 0x20, 'D': 0x20,
    'e': 0x12, 'E': 0x12,
    'f': 0x21, 'F': 0x21,
    'g': 0x22, 'G': 0x22,
    'h': 0x23, 'H': 0x23,
    'i': 0x17, 'I': 0x17,
    'j': 0x24, 'J': 0x24,
    'k': 0x25, 'K': 0x25,
    'l': 0x26, 'L': 0x26,
    'm': 0x32, 'M': 0x32,
    'n': 0x31, 'N': 0x31,
    'o': 0x18, 'O': 0x18,
    'p': 0x19, 'P': 0x19,
    'q': 0x10, 'Q': 0x10,
    'r': 0x13, 'R': 0x13,
    's': 0x1F, 'S': 0x1F,
    't': 0x14, 'T': 0x14,
    'u': 0x16, 'U': 0x16,
    'v': 0x2F, 'V': 0x2F,
    'w': 0x11, 'W': 0x11,
    'x': 0x2D, 'X': 0x2D,
    'y': 0x15, 'Y': 0x15,
    'z': 0x2C, 'Z': 0x2C,
    # Numbers
    'num0': 0x52, '0': 0x0b, ')': 0x0b,
    'num1': 0x4F, '1': 0x02, '!': 0x02,
    'num2': 0x50, '2': 0x03, '@': 0x03,
    'num3': 0x51, '3': 0x04, '#': 0x04,
    'num4': 0x4B, '4': 0x05, '$': 0x05,
    'num5': 0x4C, '5': 0x06, '%': 0x06,
    'num6': 0x4D, '6': 0x07, '^': 0x07,
    'num7': 0x47, '7': 0x08, '&': 0x08,
    'num8': 0x48, '8': 0x09, '*': 0x09,
    'num9': 0x49, '9': 0x0a, '(': 0x0a,
    # Calculation keys
    'num/': 0xB5,
    'numdelete': 0x53,
    'num-': 0x4A,
    'num+': 0x4e,
    'num*': 0x37,
    # Arrow keys
    'up': 0xC8,
    'down': 0xD0,
    'left': 0xCB,
    'right': 0xCD,
    # Control keys
    'space': 0x39, ' ': 0x39,
    'esc': 0x01,
    'tab': 0x0F, '\t': 0x0F,
    'backspace': 0x0E, '\b': 0x0E,
    'enter': 0x1C, 'numenter': 0x9C, '\n': 0x1C, '\r': 0x1C,
    'shift': 0x2A, 'lshift': 0x2A, 'rshift': 0x36,
    'ctrl': 0x1D, 'lcrtl': 0x1D, 'rctrl': 0x9D,
    'alt': 0x38, 'lalt': 0x38, 'ralt': 0xB8,
    'win': 0xDB, 'lwin': 0xDB, 'rwin': 0xDC,
    'apps': 0xDD,
    'capslock': 0x3A,
    'numlock': 0x45,
    'scrolllock': 0x46,
    'insert': 0xD2,
    'delete': 0xD3,
    'home': 0xC7,
    'end': 0xCF,
    'pageup': 0xC9,
    'pagedown': 0xD1,
    # Function keys
    'f1': 0x3B,
    'f2': 0x3C,
    'f3': 0x3D,
    'f4': 0x3E,
    'f5': 0x3F,
    'f6': 0x40,
    'f7': 0x41,
    'f8': 0x42,
    'f9': 0x43,
    'f10': 0x44,
    'f11': 0x57,
    'f12': 0x58,
    # Symbols
    '`': 0x29, '~': 0x29,
    '-': 0x0c, '_': 0x0c,
    '=': 0x0d, '+': 0x0d,
    '[': 0x1a, '{': 0x1a,
    ']': 0x1b, '}': 0x1b,
    '\\': 0x2b, '|': 0x2b,
    ';': 0x27, ':': 0x27,
    '\'': 0x28, '"': 0x28,
    ',': 0x33, '<': 0x33,
    '.': 0x34, '>': 0x34,
    '/': 0x35, '?': 0x35
}

# Define virtual key codes for GetAsyncKeyState()
VK_CODE = {
    # Alphabets
    'a': 0x41, 'A': 0x41,
    'b': 0x42, 'B': 0x42,
    'c': 0x43, 'C': 0x43,
    'd': 0x44, 'D': 0x44,
    'e': 0x45, 'E': 0x45,
    'f': 0x46, 'F': 0x46,
    'g': 0x47, 'G': 0x47,
    'h': 0x48, 'H': 0x48,
    'i': 0x49, 'I': 0x49,
    'j': 0x4A, 'J': 0x4A,
    'k': 0x4B, 'K': 0x4B,
    'l': 0x4C, 'L': 0x4C,
    'm': 0x4D, 'M': 0x4D,
    'n': 0x4E, 'N': 0x4E,
    'o': 0x4F, 'O': 0x4F,
    'p': 0x50, 'P': 0x50,
    'q': 0x51, 'Q': 0x51,
    'r': 0x52, 'R': 0x52,
    's': 0x53, 'S': 0x53,
    't': 0x54, 'T': 0x54,
    'u': 0x55, 'U': 0x55,
    'v': 0x56, 'V': 0x56,
    'w': 0x57, 'W': 0x57,
    'x': 0x58, 'X': 0x58,
    'y': 0x59, 'Y': 0x59,
    'z': 0x5A, 'Z': 0x5A,
    # Numbers
    'num0': 0x60, '0': 0x30, ')': 0x30,
    'num1': 0x61, '1': 0x31, '!': 0x31,
    'num2': 0x62, '2': 0x32, '@': 0x32,
    'num3': 0x63, '3': 0x33, '#': 0x33,
    'num4': 0x64, '4': 0x34, '$': 0x34,
    'num5': 0x65, '5': 0x35, '%': 0x35,
    'num6': 0x66, '6': 0x36, '^': 0x36,
    'num7': 0x67, '7': 0x37, '&': 0x37,
    'num8': 0x68, '8': 0x38, '*': 0x38,
    'num9': 0x69, '9': 0x39, '(': 0x39,
    # Calculation keys
    'num/': 0x6F,
    'numdelete': 0x6E,
    'num-': 0x6D,
    'num+': 0x6B,
    'num*': 0x6A,
    # Arrow keys
    'up': 0x26,
    'down': 0x28,
    'left': 0x25,
    'right': 0x27,
    # Control keys
    'space': 0x20, ' ': 0x20,
    'esc': 0x1B,
    'tab': 0x09, '\t': 0x09,
    'backspace': 0x08, '\b': 0x08,
    'enter': 0x0D, 'numenter': 0x0D, '\n': 0x0D, '\r': 0x0D,
    'shift': 0x10, 'lshift': 0x10, 'rshift': 0x10,
    'ctrl': 0x11, 'lcrtl': 0x11, 'rctrl': 0x11,
    'alt': 0x12, 'lalt': 0x12, 'ralt': 0x12,
    'win': 0x5B, 'lwin': 0x5B, 'rwin': 0x5C,
    'apps': 0x5D,
    'capslock': 0x14,
    'numlock': 0x90,
    'scrolllock': 0x91,
    'insert': 0x2D,
    'delete': 0x2E,
    'home': 0x24,
    'end': 0x23,
    'pageup': 0x21,
    'pagedown': 0x22,
    # Function keys
    'f1': 0x70,
    'f2': 0x71,
    'f3': 0x72,
    'f4': 0x73,
    'f5': 0x74,
    'f6': 0x75,
    'f7': 0x76,
    'f8': 0x77,
    'f9': 0x78,
    'f10': 0x79,
    'f11': 0x7A,
    'f12': 0x7B,
    # Symbols
    '`': 0xC0, '~': 0xC0,
    '-': 0xBD, '_': 0xBD,
    '=': 0xBB, '+': 0xBB,
    '[': 0xDB, '{': 0xDB,
    ']': 0xDD, '}': 0xDD,
    '\\': 0xDC, '|': 0xDC,
    ';': 0xBA, ':': 0xBA,
    '\'': 0xDE, '"': 0xDE,
    ',': 0xBC, '<': 0xBC,
    '.': 0xBE, '>': 0xBE,
    '/': 0xBF, '?': 0xBF
}

# Define virtual codes for mouse input
MB_CODE = {
    'left': 0x0002,
    'right': 0x0008,
    'middle': 0x0020
}
