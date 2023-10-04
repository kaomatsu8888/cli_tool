from config import User

initial_users = [{"name": "Bob", "age": 15}, {"name": "Tom", "age": 57}, {"name": "Ken", "age": 73}]


def add_initial_users():
    # 初期のユーザーリストをデータベースに追加
    for user_data in initial_users:
        User.add_user(name=user_data["name"], defaults={"age": user_data["age"]})
        # if created:
        #     print(f"Added initial user: {user.name}")


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
    show_menu()  # アプリケーション起動時にメニューを表示
    add_initial_users()  # 初期ユーザーをデータベースに追加
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
        show_menu()  # コマンド実行後に再度メニューを表示


if __name__ == "__main__":
    main()
