class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        self.posts = 'Hello, world!'
        self.posts = 'Had a great day at the park!'
        self.posts = "What's up, Natalie? How are you?"
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print(f"{self.username}'s posts:")
        for i, posts in enumerate(self.posts, 1):
            print(f"{i}. {posts}")

def main():
    profile = SocialMediaProfile("Johndoe")  # Tworzymy profil użytkownika
    profile.add_post("Hello, world!")  # Dodajemy post
    profile.add_post("Had a great day at the park!")  # Dodajemy kolejny post
    profile.add_post("What's up, Natalie? How are you?")  # Dodajemy jeszcze jeden
    profile.show_posts()  # Wyświetlamy wszystkie posty


if __name__ == "__main__":
    main()