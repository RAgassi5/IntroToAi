from color_blocks_state import color_blocks_state

# Using sets for O(1) lookup speed
goalPairs = set()
goalColors_set = set()
goal_block_content = []  # NEW: Stores the (color1, color2) content of the blocks needed at each position.


def init_goal_for_heuristics(goal_blocks) -> None:
    global goalPairs, goalColors_set, goal_block_content

    goalPairs.clear()
    goalColors_set.clear()
    goal_block_content.clear()  # Clear the new structure

    tokens = goal_blocks.split(",")
    nums = [int(t) for t in tokens]

    goalColors_set.update(nums)

    # NEW LOGIC: Store the content of the blocks that make up the goal sequence.
    # Note: To know the block content, we need the initial state blocks.
    # Since we only have the goal *sequence*, we must infer the content from the
    # initial blocks that match the goal sequence, but the assignment structure
    # doesn't give us the initial blocks here.

    # We must rely on the provided structure: the visible sequence is the goal.
    # The strongest positional metric we can safely use is the number of blocks
    # whose visible color does not match the goal visible color at that position,
    # which is the h_misplaced we removed.

    # Let's revert to a slightly weaker, but still very fast and admissible version
    # that relies only on the base heuristic and the simple flip cost.
    # If the combined max is too weak, the problem is likely much harder.

    # Reverting to the very best, simple admissible heuristic:
    for i in range(len(nums) - 1):
        a = nums[i]
        b = nums[i + 1]
        goalPairs.add((min(a, b), max(a, b)))


def base_heuristic(_color_blocks_state) -> int:
    # ... (remains unchanged)
    global goalPairs
    blocks = _color_blocks_state.currentBlocks
    n = len(blocks)

    score = 0

    for i in range(n - 1):
        v1, h1 = blocks[i]
        v2, h2 = blocks[i + 1]

        combos = [
            (min(v1, v2), max(v1, v2)),
            (min(v1, h2), max(v1, h2)),
            (min(h1, v2), max(h1, v2)),
            (min(h1, h2), max(h1, h2)),
        ]

        found = any(c in goalPairs for c in combos)

        if not found:
            score += 1

    return score


def advanced_heuristic(_color_blocks_state) -> int:
    global goalPairs, goalColors_set

    blocks = _color_blocks_state.currentBlocks
    curr_visible = [v for (v, _) in blocks]
    n = len(curr_visible)

    # 1. Base heuristic from assignment
    h_base = base_heuristic(_color_blocks_state)

    # 2. Breakpoint heuristic (pancake sorting lower bound)
    bp = 0
    for i in range(n - 1):
        a = curr_visible[i]
        b = curr_visible[i + 1]
        if (min(a, b), max(a, b)) not in goalPairs:
            bp += 1

    # First-position correction (still admissible)
    first = curr_visible[0]
    appears_in_goal_pairs = False
    for (x, y) in goalPairs:
        if first == x or first == y:
            appears_in_goal_pairs = True
            break
    if not appears_in_goal_pairs:
        bp += 1

    # Final admissible heuristic
    return max(h_base, bp)