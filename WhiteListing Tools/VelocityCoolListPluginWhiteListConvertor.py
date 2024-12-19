def is_username_valid(user: str):
    bads = [None, "", " ", ".", ".."]
    if (user in bads) or (" " in user) or (not user.strip()):
        return False
    return True

def username_fixer(user: str):
    return user.replace("\n","").replace(" ", "")

def anti_duplication(userlist: list):
    return list(set(userlist))

def main():
    new_whitelist = []
    with open("Temp.txt", "rt") as temp_list:
        new_whitelist.extend([username_fixer(username) for username in temp_list.readlines() if is_username_valid(username_fixer(username))])
    
    with open("Permanet.txt", "rt") as perm_list:
        new_whitelist.extend([username_fixer(username) for username in perm_list.readlines() if is_username_valid(username_fixer(username))])
    
    print(f"Totally {len(new_whitelist)} users and {len(anti_duplication(new_whitelist))} after deduplication")   
 
    with open("whitelist.json", "wt") as export:
        export.write('["'+'","'.join(anti_duplication(new_whitelist))+'"]')
        
main()