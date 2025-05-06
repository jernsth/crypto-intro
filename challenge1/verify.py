import hashlib

EXPECTED_HASH = "cf13ab4053250dd6bbb3302a456c002f3d210ebc6252c0887661a0da8032a10a"

def check_flag(user_input):
    h = hashlib.sha256(user_input.encode()).hexdigest()
    return h == EXPECTED_HASH

if __name__ == "__main__":
    flag = input("Enter the flag: ").strip()
    if check_flag(flag):
        print("Correct! 🎉")
    else:
        print("Incorrect. Try again.")

