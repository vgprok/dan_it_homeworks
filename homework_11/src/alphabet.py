class Alphabet:
	def __init__(self, lang, letters):
		self.lang = lang
		self.letters = letters
	def print(self):
		print(" ".join(self.letters))
	def letters_num(self):
		return len(self.letters)

class EngAlphabet(Alphabet):
	_letters_num = 26
	def __init__(self):
		super().__init__('En', [chr(i) for i in range(ord('A'), ord('Z') + 1)])
	def is_en_letter(self, letter):
		return letter.upper() in self.letters
	def letters_num(self):
		return EngAlphabet._letters_num
	@staticmethod
	def example():
		return "He who has a why to live can bear almost any how."

if __name__ == "__main__":
    eng_alphabet = EngAlphabet()
    print("English Alphabet Letters:")
    eng_alphabet.print()

    print("\nNumber of letters in the English alphabet:", eng_alphabet.letters_num())
    print("\nIs 'F' an English letter?", eng_alphabet.is_en_letter('F'))
    print("Is 'Щ' an English letter?", eng_alphabet.is_en_letter('Щ'))
    print("\nExample text in English:", eng_alphabet.example())