import re


class ValidException(Exception):
    pass


class Valid():
    def validate(self, pattern, location):
        errors = ""
        if pattern not in ["block", "tub", "blinker", "beacon", "spaceship"]:
            errors += "invalid pattern\n"
        match = re.match("[0-7],[0-7]", location)
        if match == None:
            errors += "invalid position"
        if errors:
            raise ValidException(errors)
