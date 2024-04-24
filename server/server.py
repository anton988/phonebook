import socket

contacts = {}


def add_contact(contact_info):
    global contacts
    contact_id = len(contacts) + 1
    contacts[contact_id] = contact_info
    return f"Contact added with ID: {contact_id}"


def remove_contact(contact_id):
    global contacts
    if int(contact_id) in contacts:
        del contacts[int(contact_id)]
        return "Contact removed successfully"
    else:
        return "Contact not found"


def search_contact(query):
    global contacts
    results = []
    for contact_id, contact_info in contacts.items():
        if query.lower() in contact_info.lower():
            results.append((contact_id, contact_info))
    if results:
        return "\n".join([f"ID: {result[0]}, Info: {result[1]}" for result in results])
    else:
        return "No contacts found"


def view_contact(contact_id):
    global contacts
    if int(contact_id) in contacts:
        return f"ID: {contact_id}, Info: {contacts[int(contact_id)]}"
    else:
        return "Contact not found"


def handle_request(request):
    parts = request.split(' ', 1)
    action = parts[0]
    if action == 'ADD':
        return add_contact(parts[1])
    elif action == 'REMOVE':
        return remove_contact(parts[1])
    elif action == 'SEARCH':
        return search_contact(parts[1])
    elif action == 'VIEW':
        return view_contact(parts[1])
    else:
        return "Invalid request"


def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr}")
                data = conn.recv(1024).decode()
                response = handle_request(data)
                conn.sendall(response.encode())


if __name__ == "__main__":
    main()
