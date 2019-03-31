import re


class ValidException(Exception):
    pass


class Valid():
    def validate(self, sentence):
        if sentence == "":
            raise ValidException("invalid sentence")
        match = re.match("(\s*[a-z]+\s*[a-z]*)*", sentence)
        if match == None:
            raise ValidException("invalid sentence")
        else:
            words = sentence.split(" ")
            for word in words:
                match = re.match("[a-z]+", word)
                if match == None:
                    raise ValidException("invalid sentence")
                if len(word) < 3:
                    raise ValidException("invalid sentence")
