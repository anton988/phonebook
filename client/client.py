import socket


def send_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode())
        response = s.recv(1024).decode()
        return response


def add_contact(host, port, contact_info):
    request = f"ADD {contact_info}"
    return send_request(host, port, request)


def remove_contact(host, port, contact_id):
    request = f"REMOVE {contact_id}"
    return send_request(host, port, request)


def search_contact(host, port, query):
    request = f"SEARCH {query}"
    return send_request(host, port, request)


def view_contact(host, port, contact_id):
    request = f"VIEW {contact_id}"
    return send_request(host, port, request)


def main():
    host = 'localhost'
    port = 12345

    while True:
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Search contact")
        print("4. View contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone = input("Enter phone number: ")
            note = input("Enter note: ")
            contact_info = f"{name},{surname},{phone},{note}"
            response = add_contact(host, port, contact_info)
            print(response)
        elif choice == '2':
            contact_id = input("Enter contact ID: ")
            response = remove_contact(host, port, contact_id)
            print(response)
        elif choice == '3':
            query = input("Enter search query: ")
            response = search_contact(host, port, query)
            print(response)
        elif choice == '4':
            contact_id = input("Enter contact ID: ")
            response = view_contact(host, port, contact_id)
            print(response)
        elif choice == '5':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
