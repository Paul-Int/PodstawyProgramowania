import queue

customers = queue.Queue()
next_ticket = 1

while True:
    print("\n1. New customer (take ticket)")
    print("2. Serve next customer")
    print("0. Quit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        customers.put(next_ticket)
        print(f"Customer added. Ticket number: {next_ticket}")
        next_ticket += 1

    elif choice == "2":
        if not customers.empty():
            ticket = customers.get()
            print(f"Serving customer with ticket: {ticket}")
        else:
            print("No customers in queue.")

    elif choice == "0":
        break