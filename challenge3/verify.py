import hashlib

EXPECTED_HASH = "1058d02b1f3dec85780ce836c1892a2c9cd168fef887b84f2851129d3cffc5c1"

def check_flag(user_input):
    h = hashlib.sha256(user_input.encode()).hexdigest()
    return h == EXPECTED_HASH

if __name__ == "__main__":
    flag = input("Enter the flag: ").strip()
    if check_flag(flag):
        print("Correct! 🎉")
    else:
        print("Incorrect. Try again.")

