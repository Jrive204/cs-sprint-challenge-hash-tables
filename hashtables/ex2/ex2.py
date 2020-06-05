#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    flights = {}
    route = [None] * length  # set up our route list with enough slots
    for i in range(0, length):
        current = tickets[i]
        # the starting location is the key and the destination is the value
        flights[current.source] = current.destination
    # set first flight in arr to flight w/ source "NONE"
    print(flights, "\n - --- Flights Dict - ---")
    route[0] = flights["NONE"]
    print(route[0], 'departion')
    route[1] = flights[route[0]]  # found by following the i - 1 hint in read me
    print(route[1], 'first layover')
    if length > 2:
        for i in range(2, length):
            # the `i`th location in the route can be found by checking the hash
            # table for the `i-1`th location
            print(i, route[i - 1])
            route[i] = flights[route[i - 1]]
    return route


if __name__ == "__main__":
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
               ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    result = reconstruct_trip(tickets, 10)
    print(result)
