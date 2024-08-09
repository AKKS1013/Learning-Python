CODES = {
  'A': 'Y',
  'B': 'P',
  'C': 'W',
  'D': 'X',
  'E': 'U',
  'F': 'S',
  'G': 'T',
  'H': 'Z',
  'I': 'O',
  'J': 'R',
  'K': 'Q',
  'L': 'V',
  'M': 'N',
  'N': 'M',
  'O': 'I',
  'P': 'B',
  'Q': 'K',
  'R': 'J',
  'S': 'F',
  'T': 'G',
  'U': 'E',
  'V': 'L',
  'W': 'C',
  'X': 'D',
  'Y': 'A',
  'Z': 'H',
  ' ': ' ',
}

msg = input("Message: ").upper()
nmsg = ""
for letter in msg:
  nmsg += CODES[letter]
print(nmsg)
