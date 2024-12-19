import pyperclip


def is_username_valid(user: str):
    bads = [None, "", " ", ".", ".."]
    if (user in bads) or (" " in user) or (not user.strip()):
        return False
    return True

def username_fixer(user: str):
    return user.replace("\n","").replace(" ", "")

def anti_duplication(userlist: list):
    return list(set(userlist))

server = 'bedwars'
extra_newlines_count = 3

usernames = []
with open("users.txt", "rt") as temp_list:
    usernames.extend([username_fixer(username) for username in temp_list.readlines() if is_username_valid(username_fixer(username))])


result = ""
for i in anti_duplication(usernames):
    result += (f'send {i} {server}\n'+extra_newlines_count*'\n')
pyperclip.copy(result)
