class ReverseString:
    def reverse(self, s: str):
        return s[::-1]

stringReverser = ReverseString()
print(stringReverser.reverse("Cat"))
print(stringReverser.reverse("The Daily Byte"))
print(stringReverser.reverse("civic"))