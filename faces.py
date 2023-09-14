def main():
    special_char = '.<>()!@#$%^&*_+=-:;[]}{'
    x = input("Enter: ")
    print(x.strip(special_char), convert(x))

def convert(emoji):
    all_letters = "AaBbCcDdEeFfGgHhIiJjKk\
                    LlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

    if emoji.strip(all_letters) == ':)':
        emoji = '\U0001f604'
        return emoji
    elif emoji.strip(all_letters) == ':(':
        emoji = '\U0001F641'
        return emoji
        
main()