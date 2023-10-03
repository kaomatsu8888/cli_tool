class CRMApplication:
    def __init__(self):
        #  ユーザーリスト
        self.users = [{"name": "Bob", "age": 15}, {"name": "Tom", "age": 57}, {"name": "Ken", "age": 73}]

    def show_users(self):
        #  すべてのユーザー情報を表示
        for user in self.users:
            print(f"Name: {user['name']} Age: {user['age']}")

    def add_user(self):
        #  新しいユーザーを追加する
        name = input("New user name > ")
        age = int(input("New user age > "))
        self.users.append({"name": name, "age": age})
        print(f"Add new user: {name}")

    def run(self):
        #  メニュー表示
        print("===== Welcome to CRM Application =====")
        print("[S]how: Show all users info")
        print("[A]dd: Add new user")
        print("[Q]uit: Quit The Application")
        print("======================================")

        while True:
            command = input("\nYour command > ").upper()
            if command == "S":
                # 全メンバー見る
                self.show_users()
            elif command == "A":
                # 追加
                self.add_user()
            elif command == "Q":
                # 終了
                print("Bye!")
                break
            else:
                #  設定されたもの以外のキーを押した場合
                print(f"{command}: command not found")


if __name__ == "__main__":
    app = CRMApplication()
    app.run()
