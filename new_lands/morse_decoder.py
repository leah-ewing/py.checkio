"""

Decrypt the secret message using Morse code. 
- The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
- If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

>>> morse_decoder("... --- -- .   - . -..- -")
'Some text'

>>> morse_decoder("..--- ----- .---- ---..")
'2018'

>>> morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
'It was a good day'

"""

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

def morse_decoder(code):
    code = code.split(" ")
    decode = []
    
    MORSE[""] = " "
    
    for i in range(len(code)):
        decode.append(MORSE[code[i]])
            
    i = 0
    while i < len(decode):
        if decode[i] == " " and decode[i + 1] == " ":
            decode.pop(i)
        i += 1
    
    decode[0] = decode[0].upper()
    
    decode = "".join(decode)

    return decode



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")