from __future__ import annotations


class Block:
    counter: int = 1

    def __init__(self, name_prefix: str = "block") -> None:
        self.name = f"{name_prefix}{Block.counter}"
        Block.counter += 1
        self.row = 0
        self.column = 0

        self.left_parent: Block | None = None
        self.middle_parent: Block | None = None
        self.right_parent: Block | None = None

        self.left_child: Block | None = None
        self.middle_child: Block | None = None
        self.right_child: Block | None = None

    def __str__(self) -> str:
        if self.left_child is not None:
            left = self.left_child.name
        else:
            left = None

        if self.right_child is not None:
            right = self.right_child.name
        else:
            right = None

        if self.middle_child is not None:
            middle = self.middle_child.name
        else:
            middle = None

        return f"{self.name}-> left: {left}, right: {right}, middle: {middle}"

    def repr(self) -> str:
        return self.name


block1 = Block()
block2 = Block()
block3 = Block()
block4 = Block()
block5 = Block()
block6 = Block()
block7 = Block()
block8 = Block()
block9 = Block()
block10 = Block()
block11 = Block()
block12 = Block()
block13 = Block()
block14 = Block()
block15 = Block()
block16 = Block()
block17 = Block()
block18 = Block()
block19 = Block()
block20 = Block()
block21 = Block()
block22 = Block()
block23 = Block()
block24 = Block()
block25 = Block()
block26 = Block()
block27 = Block()
block28 = Block()
block29 = Block()
block30 = Block()
block31 = Block()
block32 = Block()
block33 = Block()
block34 = Block()
block35 = Block()
block36 = Block()

block = block1
block.left_parent = None
block.middle_parent = None
block.right_parent = None
block.left_child = block2
block.middle_child = None
block.right_child = block17

block = block2
block.left_parent = None
block.middle_parent = None
block.right_parent = block1
block.left_child = None
block.middle_child = block3
block.right_child = None

block = block3
block.left_parent = None
block.middle_parent = block2
block.right_parent = None
block.left_child = None
block.middle_child = block4
block.right_child = None

block = block4
block.left_parent = None
block.middle_parent = block3
block.right_parent = None
block.left_child = block5
block.middle_child = None
block.right_child = block7

block = block5
block.left_parent = None
block.middle_parent = None
block.right_parent = block4
block.left_child = None
block.middle_child = block6
block.right_child = None

block = block6
block.left_parent = None
block.middle_parent = block5
block.right_parent = None
block.left_child = None
block.middle_child = None
block.right_child = block9

block = block7
block.left_parent = block4
block.middle_parent = None
block.right_parent = None
block.left_child = None
block.middle_child = block8
block.right_child = None

block = block8
block.left_parent = None
block.middle_parent = block7
block.right_parent = None
block.left_child = block9
block.middle_child = None
block.right_child = None

block = block9
block.left_parent = block6
block.middle_parent = None
block.right_parent = block8
block.left_child = block10
block.middle_child = None
block.right_child = block11

block = block10
block.left_parent = None
block.middle_parent = None
block.right_parent = block9
block.left_child = None
block.middle_child = None
block.right_child = block15

block = block11
block.left_parent = block9
block.middle_parent = None
block.right_parent = None
block.left_child = block12
block.middle_child = None
block.right_child = block13

block = block12
block.left_parent = None
block.middle_parent = None
block.right_parent = block11
block.left_child = None
block.middle_child = None
block.right_child = block14

block = block13
block.left_parent = block11
block.middle_parent = None
block.right_parent = None
block.left_child = block14
block.middle_child = None
block.right_child = None

block = block14
block.left_parent = block12
block.middle_parent = None
block.right_parent = block13
block.left_child = block15
block.middle_child = None
block.right_child = None

block = block15
block.left_parent = None
block.middle_parent = None
block.right_parent = block14
block.left_child = None
block.middle_child = block16
block.right_child = None

block = block16
block.left_parent = None
block.middle_parent = block15
block.right_parent = None
block.left_child = None
block.middle_child = None
block.right_child = block34

block = block17
block.left_parent = block1
block.middle_parent = None
block.right_parent = None
block.left_child = block18
block.middle_child = None
block.right_child = block28

block = block18
block.left_parent = None
block.middle_parent = None
block.right_parent = block17
block.left_child = block19
block.middle_child = None
block.right_child = block25

block = block19
block.left_parent = None
block.middle_parent = None
block.right_parent = block18
block.left_child = block20
block.middle_child = None
block.right_child = block22

block = block20
block.left_parent = None
block.middle_parent = None
block.right_parent = block19
block.left_child = None
block.middle_child = block21
block.right_child = None

block = block21
block.left_parent = None
block.middle_parent = block20
block.right_parent = None
block.left_child = None
block.middle_child = None
block.right_child = block24

block = block22
block.left_parent = block19
block.middle_parent = None
block.right_parent = None
block.left_child = None
block.middle_child = block23
block.right_child = None

block = block23
block.left_parent = None
block.middle_parent = block22
block.right_parent = None
block.left_child = block24
block.middle_child = None
block.right_child = None

block = block24
block.left_parent = block21
block.middle_parent = None
block.right_parent = block23
block.left_child = None
block.middle_child = None
block.right_child = block27

block = block25
block.left_parent = block18
block.middle_parent = None
block.right_parent = None
block.left_child = None
block.middle_child = block26
block.right_child = None

block = block26
block.left_parent = None
block.middle_parent = block25
block.right_parent = None
block.left_child = block27
block.middle_child = None
block.right_child = None

block = block27
block.left_parent = block24
block.middle_parent = None
block.right_parent = block26
block.left_child = None
block.middle_child = None
block.right_child = block29

block = block28
block.left_parent = block17
block.middle_parent = None
block.right_parent = None
block.left_child = block29
block.middle_child = None
block.right_child = None

block = block29
block.left_parent = block27
block.middle_parent = None
block.right_parent = block28
block.left_child = None
block.middle_child = block30
block.right_child = None

block = block30
block.left_parent = None
block.middle_parent = block29
block.right_parent = None
block.left_child = block31
block.middle_child = None
block.right_child = block32

block = block31
block.left_parent = None
block.middle_parent = None
block.right_parent = block30
block.left_child = None
block.middle_child = None
block.right_child = block33

block = block32
block.left_parent = block30
block.middle_parent = None
block.right_parent = None
block.left_child = block33
block.middle_child = None
block.right_child = None

block = block33
block.left_parent = block31
block.middle_parent = None
block.right_parent = block32
block.left_child = block34
block.middle_child = None
block.right_child = None

block = block34
block.left_parent = block16
block.middle_parent = None
block.right_parent = block33
block.left_child = None
block.middle_child = block35
block.right_child = None

block = block35
block.left_parent = None
block.middle_parent = block34
block.right_parent = None
block.left_child = None
block.middle_child = block36
block.right_child = None

block = block36
block.left_parent = None
block.middle_parent = block35
block.right_parent = None
block.left_child = None
block.middle_child = None
block.right_child = None


def walk(top_node: Block | None, bottom_node: Block) -> bool:
    if top_node is None:
        return False

    if top_node is bottom_node:
        print(top_node)
        return True

    left_depth = walk(top_node.left_child, bottom_node)
    middle_depth = walk(top_node.middle_child, bottom_node)
    right_depth = walk(top_node.right_child, bottom_node)

    if left_depth or middle_depth or right_depth:
        print(top_node)

    return left_depth or middle_depth or right_depth


def total_depth(root: Block | None) -> int:
    if root is None:
        return 0
    left_depth = total_depth(root.left_child)
    middle_depth = total_depth(root.middle_child)
    right_depth = total_depth(root.right_child)
    return 1 + max(left_depth, middle_depth, right_depth)


def node_max_depth(top_node: Block | None, bottom_node: Block) -> int:
    if top_node is None:
        return -999999999999

    if top_node is bottom_node:
        return 1

    left_depth = node_max_depth(top_node.left_child, bottom_node)
    middle_depth = node_max_depth(top_node.middle_child, bottom_node)
    right_depth = node_max_depth(top_node.right_child, bottom_node)
    return 1 + max(left_depth, middle_depth, right_depth)


def pad_nodes(root: Block, top_node: Block, bottom_node: Block):
    top_depth = node_max_depth(root, top_node)
    bottom_depth = node_max_depth(root, bottom_node)

    num_padding = bottom_depth - top_depth - 1

    if num_padding == 0:
        return

    if top_node.left_child is not None:
        direction = "left"

    elif top_node.right_child is not None:
        direction = "right"

    working_node = top_node
    for i in range(num_padding):
        pad = Block("pad")

        working_node.left_child = None
        working_node.middle_child = pad
        working_node.right_child = None

        pad.left_parent = None
        pad.middle_parent = working_node
        pad.right_child = None

        working_node = pad

    # Do we left or right pad at the end?
    if direction == "left":
        working_node.left_child = bottom_node
        bottom_node.right_parent = working_node

    elif direction == "right":
        working_node.right_child = bottom_node
        bottom_node.left_parent = working_node


def find_paths(root: Block):
    # Helper function to find paths recursively
    def find_paths_recursive(node: Block | None, current_path, all_paths):
        if node is None:
            return

        # Add the current node to the path
        current_path.append(node)

        # If it's a leaf node, add the path to the list of all paths
        if (
            node.left_child is None
            and node.middle_child is None
            and node.right_child is None
        ):
            all_paths.append(list(current_path))
        else:
            # Recur for left, middle, and right children
            find_paths_recursive(node.left_child, current_path, all_paths)
            find_paths_recursive(node.middle_child, current_path, all_paths)
            find_paths_recursive(node.right_child, current_path, all_paths)

        # Remove the current node from the path (backtracking)
        current_path.pop()

    # List to store all paths
    all_paths = []

    # Call the helper function with initial parameters
    find_paths_recursive(root, [], all_paths)

    return all_paths


def assign_layers(root: Block | None) -> list[list[Block]]:
    if not root:
        return []

    visited = []
    layers: list[list[Block]] = []
    queue: list[tuple[Block, int]] = [(root, 0)]  # (node, layer)

    while queue:
        node, layer = queue.pop()

        if layer == len(layers):
            layers.append([])

        if node not in visited:
            layers[layer].append(node)
            visited.append(node)

        if node.left_child:
            queue.append((node.left_child, layer + 1))
        if node.middle_child:
            queue.append((node.middle_child, layer + 1))
        if node.right_child:
            queue.append((node.right_child, layer + 1))

    return layers


def get_branch_nodes(root: Block | None) -> list[Block]:
    if root is None:
        return []

    result = []
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
        else:
            continue

        # Check if the node has both left and right children
        if node.left_child is not None and node.right_child is not None:
            result.append(node)

        # Add children to the stack for further processing
        if node.left_child is not None:
            stack.append(node.left_child)
        if node.middle_child is not None:
            stack.append(node.middle_child)
        if node.right_child is not None:
            stack.append(node.right_child)

    return result


def get_end_of_branch(branching_node: Block) -> Block | None:
    "Left side"
    walk_node: Block | None = branching_node.left_child
    left_side_end_branch_Nodes: list[Block] = []
    while True:

        if (
            walk_node is not None
            and walk_node.left_child is not None
            and walk_node.right_child is not None
        ):
            walk_node = get_end_of_branch(walk_node)

        if walk_node is None:
            break

        if walk_node.middle_child is not None:
            walk_node = walk_node.middle_child
        else:
            if walk_node.left_child is not None:
                left_side_end_branch_Nodes.append(walk_node.left_child)
                walk_node = walk_node.left_child

            elif walk_node.right_child is not None:
                left_side_end_branch_Nodes.append(walk_node.right_child)
                walk_node = walk_node.right_child

            else:
                break

    "right side"
    walk_node: Block | None = branching_node.right_child
    right_side_end_branch_Nodes: list[Block] = []
    while True:

        if (
            walk_node is not None
            and walk_node.left_child is not None
            and walk_node.right_child is not None
        ):
            walk_node = get_end_of_branch(walk_node)

        if walk_node is None:
            break

        if walk_node.middle_child is not None:
            walk_node = walk_node.middle_child
        else:
            if walk_node.left_child is not None:
                right_side_end_branch_Nodes.append(walk_node.left_child)
                walk_node = walk_node.left_child

            elif walk_node.right_child is not None:
                right_side_end_branch_Nodes.append(walk_node.right_child)
                walk_node = walk_node.right_child

            else:
                break
    common = [
        item
        for item in left_side_end_branch_Nodes
        if item in right_side_end_branch_Nodes
    ]

    if len(common) == 0:
        return None
    else:
        return common[0]


print([node.repr() for node in get_branch_nodes(block1)])
quit()

paths = find_paths(block1)

complete_pairs = []
for path in paths:
    item1 = path.pop(0)
    while len(path) != 0:
        item2 = path.pop(0)

        pair = f"{item1.repr()},{item2.repr()}"

        if pair not in complete_pairs:
            pad_nodes(block1, item1, item2)

        complete_pairs.append(pair)

        item1 = item2

layers = assign_layers(block1)

layers = [[block.repr() for block in layer] for layer in layers]
for layer in layers:
    layer.reverse()
