#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value # creating an instance with the attribute called value 

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) is str:
      self._value = value
    else:
      self._value = ""
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    
    value= self.value.replace("?",".")
    print(value)
    updated_value =value.replace("!",".")
    split_value = updated_value.split('.')
    print(split_value)
    sentences = []
    for value in split_value:
      if value != "":
        sentences.append(value)
    return len(sentences)
  

