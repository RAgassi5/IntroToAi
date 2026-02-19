from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq


##implement the A* Method##

def create_open_set():
    open_set = {"heap": [], "dict": {}}
    return open_set


def create_closed_set():
    closed_set = {}
    return closed_set


def add_to_open(vn, open_set):
    # state_str is now the memory-efficient tuple key
    state_str = vn.state.get_state_str()
    open_set["dict"][state_str] = vn
    heapq.heappush(open_set["heap"], vn)


def open_not_empty(open_set) -> bool:
    return len(open_set["heap"]) > 0


def get_best(open_set):
    # This loop efficiently discards "zombie" nodes (worse paths)
    while len(open_set["heap"]) > 0:
        best = heapq.heappop(open_set["heap"])

        state_str = best.state.get_state_str()

        # If not in dict, it's a zombie node, discard it (O(1) discard fix)
        if state_str not in open_set["dict"]:
            continue

        del open_set["dict"][state_str]
        return best

    return None


def add_to_closed(vn, closed_set):
    state_str = vn.state.get_state_str()
    closed_set[state_str] = vn.g


def duplicate_in_open(vn, open_set):
    state_str = vn.state.get_state_str()

    if state_str not in open_set["dict"]:
        return False

    existing = open_set["dict"][state_str]

    # If old path is equal or better → reject new node
    if existing.g <= vn.g:
        return True

    # New path is better: Remove the old node from the dictionary (O(1) update fix)
    del open_set["dict"][state_str]
    return False


def duplicate_in_closed(vn, closed_set):
    state_str = vn.state.get_state_str()

    if state_str not in closed_set:
        return False

    oldG = closed_set[state_str]

    # if old path is equal or better → reject new
    if oldG <= vn.g:
        return True

    # new path is better → remove old and allow insertion (reopening)
    del closed_set[state_str]
    return False


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")

    print(path[-1].state.state_str)


def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if color_blocks_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None