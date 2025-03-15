class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def avl_height(node):
    return -1 if node is None else 1 + max(avl_height(node.left), avl_height(node.right))
def rotate_left(r):
    u = r.right
    r.right = u.left
    u.left = r
    return u
def rotate_right(r):
    o = r.left
    r.left = o.right
    o.right = r
    return o
def avl_adjust(r):
    balance = avl_height(r.right) - avl_height(r.left)
    if balance <= -2:
        bl = avl_height(r.left.right) - avl_height(r.left.left)
        if bl <= 0:
            return rotate_right(r)
        else:
            r.left = rotate_left(r.left)
            return rotate_right(r)
    if balance >= 2:
        br = avl_height(r.right.right) - avl_height(r.right.left)
        if br >= 0:
            return rotate_left(r)
        else:
            r.right = rotate_right(r.right)
            return rotate_left(r)
    return r
def avl_insert(r, key):
    if r is None:
        return Node(key)
    if key < r.key:
        r.left = avl_insert(r.left, key)
    elif key > r.key:
        r.right = avl_insert(r.right, key)
    return avl_adjust(r)
def avl_minimum(r):
    return float('inf') if r is None else r.key if r.left is None else avl_minimum(r.left)
def avl_delete(r, key):
    if r is None:
        return None
    if key < r.key:
        r.left = avl_delete(r.left, key)
    elif key > r.key:
        r.right = avl_delete(r.right, key)
    else:
        if r.left is None:
            return r.right
        elif r.right is None:
            return r.left
        min_key = avl_minimum(r.right)
        r.key = min_key
        r.right = avl_delete(r.right, min_key)
    return avl_adjust(r)
def print_tree(r):
    if r is None:
        print("( )", end="")
        return
    if r.left is None and r.right is None:
        print(f"({r.key})", end="")
        return
    print("(", end="")
    print_tree(r.left)
    print(f"({r.key})", end="")
    print_tree(r.right)
    print(")", end="")
# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    root = None
    for i in range(7):
        root = avl_insert(root, i)
        print_tree(root)
        print()
    root = avl_delete(root, 0)
    print_tree(root)
    print()
    root = avl_delete(root, 1)
    print_tree(root)
    print()
    root = avl_delete(root, 2)
    print_tree(root)
    print()