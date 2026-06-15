users   = {}   
posts   = []
post_id = 1
    

def mainmenu():
    while True:
        print("Main Menu")
        print('#1: Create a user')
        print('#2: Make a post')
        print('#3: View Feed')
        print('#4: Like posts')
        print('#5: Edit your bio')
        print('#6: Search for words')
        print('#7: Delete post')
        print('#8: Exit')
        answer = input('Enter a number 1-8:')


        print('---------------------------')


        if answer == '1':
            create_user()
        elif answer == '2':
            write_post()
        elif answer == '3':
            view_feed()
        elif answer == '4':
            like_post()
        elif answer == '5':
            edit_bio()
        elif answer == '6':
            search_feed()
        elif answer == '7':
            delete_post()
        elif answer == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please enter 1-8.")
        print('---------------------------')



 
def create_user():
    
    username = input("Choose a username: ").strip()
    bio = input("Write a short bio: ").strip()

 
    if not username:
        print("Username cannot be empty.\n")
        return
 
    if username in users:
        print(f" The username '{username}' is already taken.\n")
        return
 
    users[username] = {"bio": bio, "followers": 0}
    print(f" You're in! Account @{username} created!\n")
 
def write_post():
    
    global post_id
 
    if not users:
        print("  No users yet. Create an account first.\n")
        if not users:
            print("No users yet. Create an account first.\n")
            create_user()
            return
 
    user = input("Your username: ").strip()
 
    if user not in users:
        print(f" No account found for such username'.\n")
        return
 
    text = input("What's on your mind? ").strip()
 
    if not text:
        print("  Post cannot be empty.\n")
        return
 
    post = {
        "id":    post_id,
        "user":  user,
        "text":  text,
        "likes": 0,
    }
    posts.append(post)
    print(f" Post #{post['id']} published!\n")
    post_id += 1
 
 
 
def view_feed():

    if not posts:
        print("  (The feed is empty — write the first post!)\n")
        return
 
    print("\n" + "═" * 45)
    print("FEED")
    print("═" * 45)
 
    for post in posts:
        print(f"  [{post['id']}] @{post['user']}")
        print(f"  Posted:    {post['text']}")
        print(f"  {post['likes']} like(s)")
    print()
 
 
def like_post():
    if not posts:
        print("No posts to like yet.\n")
        return

    answer = input("Enter the post ID you want to like: ").strip()

    if not answer.isdigit():
        print("Please enter a number.\n")
        return

    target_id = int(answer)


    for post in posts:
        if post["id"] == target_id:
            post["likes"] += 1
            print(f"Liked post #{target_id}!\n")
            return
        
    
 
    print(f"No post found with ID {target_id}.\n")
 
def search_feed():
    keyword = input("Search keyword: ").strip().lower()
    results = [p for p in posts if keyword in p["text"].lower()]
    if not results:
        print("No posts found.\n")
        return
    for post in results:
        print(f"[{post['id']}] @{post['user']}: {post['text']} \n Likes: {post['likes']}")
 
 
def edit_bio():
    username = input("Your username: ").strip()
    if username not in users:
        print("User not found.\n")
        return
    print('Bio: ',  users[username]["bio"])
    users[username]["bio"] = input("New bio: ").strip()
    print("Bio updated!\n")


def delete_post():
    username = input("Your username: ").strip()

    deletion = input("Enter the post ID you want to delete: ").strip()

    if not deletion.isdigit():
        print("Please enter a number.\n")
        return

    delete_id = int(deletion)

    for post in posts:
        if post["id"] == target_id and post["user"] == username:
            posts.remove(post)
            print("Post deleted!\n")
            return
    print("Post not found or not yours.\n")
    

mainmenu()  

 
 

