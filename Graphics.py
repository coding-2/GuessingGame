class Graphics(object):
    guess =  ''
    def startup(self):
        print ("Welcome to Guesser!")

    def guess(self):
        guess = input("Guess a letter")
        return guess

    def main(self, incorrect_guesses, correct_guesses):
        for i in range(len(correct_guesses)):
            print(correct_guesses[i], end ="")

        print(len(incorrect_guesses))