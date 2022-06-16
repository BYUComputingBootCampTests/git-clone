import random


class Door:
    def __init__(self, key):
        self.key = key
        self.locked = True

    def unlock(self, trial_key):
        if self.locked and self.key == trial_key:
            self.locked = False

    def lock(self, trial_key):
        if not self.locked and self.key == trial_key:
            self.locked = True


class SecretDoor(Door):
    def __init__(self, keylist):
        randomKey = random.choice(keylist)
        self.keylist = keylist
        super().__init__(randomKey)

    def key_guess(self):
        print(
            "You are confronted with a locked door. You need to unlock it to proceed."
        )
        print(f"Before you are laid {len(self.keylist)} keys: ")
        for index, i in enumerate(self.keylist):
            print(f"\t{index}: {i}")
        key_guessed = False
        while not key_guessed:
            print("Guess a key by entering its number")
            try:
                trial_key = self.keylist[int(input())]
                self.unlock(trial_key)
                if not self.locked:
                    key_guessed = True
                else:
                    print("The key jostles in the lock, but it fails to open the door.")
            except Exception as e:
                print("Invalid guess!")
        print("You guessed it!")
