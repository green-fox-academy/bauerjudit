class MySuperString(object):
    def __init__(self, greet):
        self.greet = greet

    def reverse(self):
        n = len(self.greet)
        reversed = ""
        for i in range(n):
            reversed = self.greet[i] + reversed
            print(reversed)
        return reversed

    def implement(self, char):
        count = 0
        for i in self.greet:
            if char == i:
                count +=1
        return count

    def repl(self):
        changed = ""
        for i in self.greet:
            if i == " ":
                changed = changed + "_"
            else:
                changed = changed + i
        return changed

    def average(self):
        aver = 0
        x = len(self.greet)
        for n in self.greet:
            aver = aver + n
        aver = aver / x
        return aver
