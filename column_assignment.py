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


def get_first_branch_node(root: Block | None) -> Block | None:

    while True:
        if root is None:
            return None

        if root.left_child is not None and root.right_child is not None:
            return root

        root = root.middle_child


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


def get_left_side_sub_branches(branching_node: Block) -> list[Block]:
    walk_node: Block | None = branching_node.left_child
    branch_nodes: list[Block] = []
    while True:

        if (
            walk_node is not None
            and walk_node.left_child is not None
            and walk_node.right_child is not None
        ):
            branch_nodes.append(walk_node)
            walk_node = get_end_of_branch(walk_node)
            continue

        if walk_node is None:
            break

        if walk_node.middle_child is not None:
            walk_node = walk_node.middle_child
        elif walk_node.right_child is not None:
            break

    return branch_nodes


def get_right_side_sub_branches(branching_node: Block) -> list[Block]:
    walk_node: Block | None = branching_node.right_child
    branch_nodes: list[Block] = []
    while True:

        if (
            walk_node is not None
            and walk_node.left_child is not None
            and walk_node.right_child is not None
        ):
            branch_nodes.append(walk_node)
            walk_node = get_end_of_branch(walk_node)
            continue

        if walk_node is None:
            break

        if walk_node.middle_child is not None:
            walk_node = walk_node.middle_child
        elif walk_node.left_child is not None:
            break

    return branch_nodes


branch_node = get_first_branch_node(block1)

if branch_node is None:
    quit()

total_branches = 0
left_side = get_left_side_sub_branches(branch_node)
right_side = get_right_side_sub_branches(branch_node)

for branch_node in left_side:
    print(branch_node)


quit()
