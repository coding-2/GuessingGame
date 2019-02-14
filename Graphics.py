class Graphics(object):
    guess =  ''
    def startup(self):
        print ("Welcome to Guesser")

    def guess(self):
        guess = input("Guess a letter")
        return guess

    def main(self):
