#!/usr/bin/env python3

from anagram import Anagram

if __name__ == '__main__':
    detector = Anagram("listen")
    words = ["enlists", "google", "inlets", "banana"]

    # This lets you test the match() method inside ipdb
    import ipdb; ipdb.set_trace()

    # Example call (run this inside ipdb):
    # detector.match(words)
