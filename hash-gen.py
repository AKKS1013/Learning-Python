def hashtag(words):
  h = "#"
  for word in words.split():
    word = word.lower()
    word = word[0].upper() + word[1:]
    h += word
    
  return h
