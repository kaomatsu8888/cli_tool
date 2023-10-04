from config import User

initial_users = [{"name": "Bob", "age": 15}, {"name": "Tom", "age": 57}, {"name": "Ken", "age": 73}]


def add_initial_users():
    # 初期のユーザーリストをデータベースに追加
    for user_data in initial_users:
        user, created = User.get_or_create(name=user_data["name"], defaults={"age": user_data["age"]})
        if created:
            print(f"Added initial user: {user.name}")


def show_menu():
    # メニューを表示する関数
    print("\n===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")


def show_users():
    # データベースからすべてのユーザー情報を取得して表示
    for user in User.select():
        print(f"Name: {user.name} Age: {user.age}")


def add_user():
    name = input("New user name > ")
    age = int(input("New user age > "))
    User.create(name=name, age=age)  # データベースに新しいユーザーを追加
    print(f"Add new user: {name}")


def main():
    add_initial_users()  # 初期ユーザーをデータベースに追加 else後 show_menu削除
    show_menu()  # アプリケーション起動時にメニューを表示 
    while True:
        command = input("\nYour command > ").upper()
        if command == "S":
            show_users()
        elif command == "A":
            add_user()
        elif command == "Q":
            print("Bye!")
            break
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
