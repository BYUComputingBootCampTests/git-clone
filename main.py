import door
import key


def main():
    keylist = [key.Key("red", 3), key.Key("blue", 4), key.Key("white", 1)]
    castle_door = door.SecretDoor(keylist)
    castle_door.key_guess()


if __name__ == "__main__":
    main()
