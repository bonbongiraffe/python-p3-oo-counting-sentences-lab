#!/usr/bin/env python3

class MyString:
  def __init__( self, value="" ):
    self.value = value

  def get_value( self ):
    return self._value 
  
  def set_value( self, value ):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence( self ):
    return self.value.endswith(".")

  def is_question( self ):
    return self.value.endswith("?")

  def is_exclamation( self ):
    return self.value.endswith("!")

  def count_sentences( self ):
    fixed_punctuation = self.value.replace('!!','.').replace('!','.').replace('?','.').replace('...','.')
    sentence_list = fixed_punctuation.split('.')
    print(sentence_list)
    return (len(sentence_list) - 1)

  value = property( get_value, set_value )
