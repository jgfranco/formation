class Logger:
    def __init__(self):
        self.db = {}

    def shouldPrintMessage(self, timestamp, message) -> bool:
        if message not in self.db  or (self.db[message] + 10) <= timestamp:
          self.db[message] = timestamp
          return True
        
        return False

# Python Test Cases
logger = Logger()
assert logger.shouldPrintMessage(1, "foo") == True  # prints "foo"
assert logger.shouldPrintMessage(2, "bar") == True  # prints "bar"
assert logger.shouldPrintMessage(3, "foo") == False # does not print "foo"
assert logger.shouldPrintMessage(8, "bar") == False # does not print "bar"
assert logger.shouldPrintMessage(10, "foo") == False # does not print "foo"
assert logger.shouldPrintMessage(11, "foo") == True  # prints "foo"

"""
Follow Up
If the number of unique messages grows over time and this process is long running, how can we limit the amount of memory this class requires?

we can turn this into a LRU cache, were we can limit the amount of entries the database can store
"""