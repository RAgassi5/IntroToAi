goalColors = []


def init_goal_for_search(goal_blocks) -> None:
    global goalColors
    goalColors = []

    parts = goal_blocks.split(',')
    for part in parts:
        goalColors.append(int(part))


class color_blocks_state:

    def __init__(self, blocks_str, **kwargs):
        """
        Initializes state from a string. Blocks are stored as an immutable
        tuple of tuples for efficient hashing.
        """
        # Removed redundant string storage (self.currentState)

        tokens = blocks_str.replace("(", "").replace(")", "").split(",")
        blocks_list = []

        # Build the block state
        for i in range(0, len(tokens), 2):
            visible = int(tokens[i])
            hidden = int(tokens[i + 1])
            blocks_list.append((visible, hidden))

        # Store as a tuple (immutable/hashable)
        self.currentBlocks = tuple(blocks_list)

    @classmethod
    def from_tuple(cls, blocks_tuple: tuple):
        """Helper to create a new state object directly from a tuple of blocks."""
        # This bypasses the string parsing for efficiency during neighbor generation
        instance = cls.__new__(cls)
        instance.currentBlocks = blocks_tuple
        return instance

    def __lt__(self, other):
        """Allows comparison of state objects (needed for heap stability)."""
        return self.currentBlocks < other.currentBlocks

    def __hash__(self) -> int:
        """Allows the state object itself to be used as a key in hash maps."""
        return hash(self.currentBlocks)

    @staticmethod
    def is_goal_state(_color_blocks_state) -> bool:
        global goalColors
        visible_list = [block[0] for block in _color_blocks_state.currentBlocks]
        return goalColors == visible_list

    def get_neighbors(self):
        neighbors = []
        # Convert immutable tuple back to a mutable list for neighbor generation
        blocks_list = list(self.currentBlocks)
        n = len(blocks_list)

        # 1. Operator: Spin (Flip)
        for i in range(n):
            new_blocks = blocks_list[:]
            visible, hidden = new_blocks[i]
            new_blocks[i] = (hidden, visible)

            new_state_tuple = tuple(new_blocks)
            neighbors.append((color_blocks_state.from_tuple(new_state_tuple), 1))

            # 2. Operator: Flip (Segment Reverse)
        for i in range(n):
            new_blocks = blocks_list[:]
            self.reverse_segment(new_blocks, i)

            new_state_tuple = tuple(new_blocks)
            neighbors.append((color_blocks_state.from_tuple(new_state_tuple), 1))

        return neighbors

    def get_state_str(self) -> tuple:
        """Returns the hashable tuple of tuples, used as the key for A* maps."""
        return self.currentBlocks

    def blocks_to_string(self, blocks):
        """Helper function for printing/debugging (not used for hashing)."""
        parts = [f"({v},{h})" for v, h in blocks]
        cubes_str = ",".join(parts)
        return cubes_str

    def reverse_segment(self, blocks, i):
        start = i
        end = len(blocks) - 1

        while start < end:
            blocks[start], blocks[end] = blocks[end], blocks[start]
            start += 1
            end -= 1