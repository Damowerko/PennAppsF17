import numpy as np

braille_a = np.array([[1, 0], [0, 0], [0, 0]])
braille_b = np.array([[1, 0], [1, 0], [0, 0]])
braille_c = np.array([[1, 1], [0, 0], [0, 0]])
braille_d = np.array([[1, 1], [0, 1], [0, 0]])
braille_e = np.array([[1, 0], [0, 1], [0, 0]])
braille_f = np.array([[1, 1], [1, 0], [0, 0]])
braille_g = np.array([[1, 1], [1, 1], [0, 0]])
braille_h = np.array([[1, 0], [1, 1], [0, 0]])
braille_i = np.array([[0, 1], [1, 0], [0, 0]])
braille_j = np.array([[0, 1], [1, 1], [0, 0]])
braille_k = np.array([[1, 0], [0, 0], [1, 0]])
braille_l = np.array([[1, 0], [1, 0], [0, 0]])
braille_m = np.array([[1, 1], [0, 0], [1, 0]])
braille_n = np.array([[1, 1], [0, 1], [1, 0]])
braille_o = np.array([[1, 0], [0, 1], [1, 0]])
braille_p = np.array([[1, 1], [1, 0], [1, 0]])
braille_q = np.array([[1, 1], [1, 1], [1, 0]])
braille_r = np.array([[1, 0], [1, 1], [1, 0]])
braille_s = np.array([[0, 1], [1, 0], [1, 0]])
braille_t = np.array([[0, 1], [1, 1], [1, 0]])
braille_u = np.array([[1, 0], [0, 0], [1, 1]])
braille_v = np.array([[1, 0], [1, 0], [1, 1]])
braille_w = np.array([[0, 1], [1, 1], [0, 1]])
braille_x = np.array([[1, 1], [0, 0], [1, 1]])
braille_y = np.array([[1, 1], [0, 1], [1, 1]])
braille_z = np.array([[1, 0], [0, 1], [1, 1]])
braille_num = np.array([[0, 1], [0, 1], [1, 1]])

braille_dict = {
    'a': braille_a,
    'b': braille_b,
    'c': braille_c,
    'd': braille_d,
    'e': braille_e,
    'f': braille_f,
    'g': braille_g,
    'h': braille_h,
    'i': braille_i,
    'j': braille_j,
    'k': braille_k,
    'l': braille_l,
    'm': braille_m,
    'n': braille_n,
    'o': braille_o,
    'p': braille_p,
    'q': braille_q,
    'r': braille_r,
    's': braille_s,
    't': braille_t,
    'u': braille_u,
    'v': braille_v,
    'w': braille_w,
    'x': braille_x,
    'y': braille_y,
    'z': braille_z,
    '#': braille_num,
    '1': braille_a,
    '2': braille_b,
    '3': braille_c,
    '4': braille_d,
    '5': braille_e,
    '6': braille_f,
    '7': braille_g,
    '8': braille_h,
    '9': braille_i,
    '0': braille_j
}

def translate(char):
    if char in braille_dict:
        return(braille_dict[char])
    else:
        return(None)

def translate_word(word):
    for letter in word:
        if not letter in braille_dict:
            return(None)
    word_array = list(word)
    final_word = ""
    for index in range(len(word_array)):
        if word_array[index].isnumeric():
            if index == 0:
                final_word += "#"
            else:
                if not word_array[index - 1].isnumeric():
                    final_word += "#"
        final_word += word_array[index]

        retVal = braille_dict[final_word[0]]
        for index in range(len(final_word)):
            if not index == 0:
                np.hstack((retVal, braille_dict[final_word[index]]))
        return(retVal)




