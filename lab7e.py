class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''Return a string representation for the object self using '.' instead of ':' '''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
