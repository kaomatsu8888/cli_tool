# # 初期ユーザーリストを設定 CRMApplicationを削除
# users = [{"name": "Bob", "age": 15}, {"name": "Tom", "age": 57}, {"name": "Ken", "age": 73}]


# def show_users():
#     #  すべてのユーザー情報を表示
#     for user in users:
#         print(f"Name: {user['name']} Age: {user['age']}")


# def add_user():
#     #  新しいユーザーを追加する
#     name = input("New user name > ")
#     age = int(input("New user age > "))
#     users.append({"name": name, "age": age})
#     print(f"Add new user: {name}")


# def main():
#     #  メニュー表示
#     print("===== Welcome to CRM Application =====")
#     print("[S]how: Show all users info")
#     print("[A]dd: Add new user")
#     print("[Q]uit: Quit The Application")
#     print("======================================")

#     while True:
#         command = input("\nYour command > ").upper()
#         if command == "S":
#             show_users()
#         elif command == "A":
#             add_user()
#         elif command == "Q":
#             print("Bye!")
#             break
#         else:
#             print(f"{command}: command not found")


# # CRMApplicationを削除
# if __name__ == "__main__":
#     main()
