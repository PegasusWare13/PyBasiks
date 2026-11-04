class Scoreboard:
    def __init__(self,score):
        self.__score = score
    def get_score(self):
        return self.__score

    
s1 = Scoreboard(0)
print(s1.get_score())
