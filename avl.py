class Node:
    def __init__(self,
                 key,
                 left_child=None,
                 right_child=None,
                 parent=None,
                 name=None,
                 **kwargs):
        self._left_child = left_child
        self._right_child = right_child
        self._parent = parent
        self._key = key
        self._height = -1

        # Tree augmentation
        self._node_count = 1
        self._name = name
        self.__dict__.update(kwargs)

    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key

    def get_height(self):
        return self._height

    def get_name(self):
        return self._name

    def set_left_child(self, node):
        self._left_child = node

    def set_right_child(self, node):
        self._right_child = node

    def set_parent(self, node):
        self._parent = node

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child

    def get_parent(self):
        return self._parent

    def get_first_valid_child(self):
        if self.get_left_child():
            return self.get_left_child()
        return self.get_right_child()

    def get_child(self, node):
        if self.get_left_child() is node:
            return self.get_left_child()
        elif self.get_right_child() is node:
            return self.get_right_child()
        else:
            return None

    def get_node_count(self):
        return self._node_count

    def set_node_count(self, node_count):
        self._node_count = node_count

    def _set_height(self, height):
        self._height = height


class AVLException(Exception):
    pass


class AVL:
    def __init__(self, root=None):
        self._root = root

    def get_root(self):
        return self._root

    def insert(self, key, **kwargs):
        new_node = Node(key, **kwargs)
        self._bubble_down_to_place(self._root, new_node)
        self._update_heights(new_node)
        self._update_node_counts(new_node)
        self._balance(new_node)

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return None

        if node.get_left_child() and node.get_right_child():
            self._remove_node_with_two_children(node)
        elif not node.get_left_child() and not node.get_right_child():
            self._remove_node_with_no_children(node)
        else:
            self._remove_node_with_one_children(node)

    def _remove_node_with_no_children(self, node):
        if self.get_root() is node:
            self._set_root(None)
        else:
            parent = node.get_parent()
            if parent.get_right_child() is node:
                parent.set_right_child(None)
                node.set_parent(None)
            else:
                parent.set_left_child(None)
                node.set_parent(None)
            self._update_heights(parent)
            self._update_node_counts(parent)
            self._balance(parent)

    def _remove_node_with_one_children(self, node):
        child = node.get_first_valid_child()

        if self.get_root() is node:
            child.set_parent(None)
            self._set_root(child)

        else:
            parent = node.get_parent()

            if parent.get_left_child() is node:
                parent.set_left_child(child)
            else:
                parent.set_right_child(child)
            child.set_parent(parent)
            self._update_heights(parent)
            self._update_node_counts(parent)
            self._balance(parent)

    def _remove_node_with_two_children(self, node):
        successor = self.get_successor(node)
        if not successor.get_left_child() and not successor.get_right_child():
            self._remove_node_with_no_children(successor)
        else:
            self._remove_node_with_one_children(successor)
        node.set_key(successor.get_key())

    def search_higher_inmediate(self, key):
        leaf = self._find_closer_leaf(self.get_root(), None, key)

        if leaf.get_key() < key:
            return self.get_successor(leaf)
        return leaf

    def search_lower_inmediate(self, key):
        leaf = self._find_closer_leaf(self.get_root(), None, key)

        if leaf.get_key() > key:
            return self.get_predecessor(leaf)
        return leaf

    def _find_closer_leaf(self, node, parent, key):
        if node is None:
            return parent

        if node.get_key() > key:
            return self._find_closer_leaf(node.get_left_child(), node, key)
        elif node.get_key() < key:
            return self._find_closer_leaf(node.get_right_child(), node, key)
        else:
            return node

    def search(self, key):
        root = self.get_root()

        if root is None:
            return None

        return self._search_node(root, key)

    def _search_node(self, node, key):
        if node is None:
            return None

        if node.get_key() < key:
            return self._search_node(node.get_right_child(), key)
        elif node.get_key() > key:
            return self._search_node(node.get_left_child(), key)
        else:
            return node

    def find_biggest(self, node=None):
        node = self.get_root() if node is None else node
        return self._get_right_most_child(node)

    def find_smallest(self, node=None):
        node = self.get_root() if node is None else node
        return self._get_left_most_child(node)

    def _get_left_most_child(self, node):
        if node.get_left_child() is None:
            return node
        else:
            return self._get_left_most_child(node.get_left_child())

    def _get_right_most_child(self, node):
        if node.get_right_child() is None:
            return node
        else:
            return self._get_right_most_child(node.get_right_child())

    def get_predecessor(self, node):
        if node is None:
            return None

        left_child = node.get_left_child()
        if left_child:
            return self._get_right_most_child(left_child)

        parent = node.get_parent()
        if parent:
            if parent.get_right_child() is node:
                return parent
            else:
                return self._find_first_turn_left(parent, node)

        return None

    def _find_first_turn_left(self, node, origin):
        if node is None:
            return None

        if node.get_right_child() is origin:
            return node

        return self._find_first_turn_left(node.get_parent(), node)

    def get_successor(self, node):
        if node is None:
            return None

        right_child = node.get_right_child()
        if right_child:
            return self._get_left_most_child(right_child)

        parent = node.get_parent()
        if parent:
            if parent.get_left_child() is node:
                return parent
            else:
                return self._find_first_turn_right(parent, node)

        return None

    def _find_first_turn_right(self, node, origin):
        if node is None:
            return None

        if node.get_left_child() is origin:
            return node

        return self._find_first_turn_right(node.get_parent(), node)

    def rank(self, key):
        node = self.search(key)
        if node is None:
            return None

        return self._get_rank(node, key)

    def _get_rank(self, node, key):
        accum = 0
        current = node
        while current:
            if current.get_key() <= key:
                accum += self._get_node_count_with_smaller_key(current)
            current = current.get_parent()
        return accum

    def _get_node_count_with_smaller_key(self, node):
        return (
            self._get_node_count(node)
            -
            self._get_node_count(node.get_right_child())
        )

    def count(self, lower_key, higher_key):
        lower_node = self.search_higher_inmediate(lower_key)
        higher_node = self.search_lower_inmediate(higher_key)
        return (
            self.rank(higher_node.get_key())
            -
            self.rank(lower_node.get_key())
            + 1
        )

    def list_nodes_in_range(self, lower_key, higher_key):
        node = self._last_common_ancestor(lower_key, higher_key)
        result = []
        self._node_list(node, lower_key, higher_key, result)
        return result

    def _node_list(self, node, lower_key, higher_key, result):
        if node is None:
            return

        key = node.get_key()
        if key >= lower_key and key <= higher_key:
            result.append(node)
        if key >= lower_key:
            self._node_list(
                node.get_left_child(),
                lower_key,
                higher_key,
                result
            )
        if key <= higher_key:
            self._node_list(
                node.get_right_child(),
                lower_key,
                higher_key,
                result
            )

    def _last_common_ancestor(self, lower_key, higher_key):
        node = self.get_root()

        while node:
            key = node.get_key()
            if lower_key <= key and higher_key >= key:
                return node

            if lower_key < key:
                node = node.get_left_child()
            else:
                node = node.get_right_child()

    def _balance(self, node):
        if node is None:
            return

        if self._has_unbalanced_children(node):
            node = self._balance_children(node)
            self._balance(node.get_parent())
        else:
            self._balance(node.get_parent())

    def _has_unbalanced_children(self, node):
        absolute_difference = abs(
            self._get_node_height(node.get_right_child())
            -
            self._get_node_height(node.get_left_child())
        )
        if absolute_difference > 1:
            return True
        return False

    def _balance_children(self, node):
        if self._is_heavy_path_zig_zag(node):
            return self._double_rotation(node)
        else:
            return self._simple_rotation(node)

    def _is_heavy_path_zig_zag(self, node):
        heavy_path = self._get_heavy_path(node)
        if heavy_path == 'right':
            heavy_path = self._get_heavy_path(node.get_right_child())
            if heavy_path == 'right':
                return False
            elif heavy_path == 'left':
                return True
            else:
                return False
        elif heavy_path == 'left':
            heavy_path = self._get_heavy_path(node.get_left_child())
            if heavy_path == 'right':
                return True
            elif heavy_path == 'left':
                return False
            else:
                return False
        else:
            raise AVLException(
                message='At this point in the algorithm,\
                         the paths cannot have equal weights'
            )

    def _get_heavy_path(self, node):
        right_child_height = self._get_node_height(node.get_right_child())
        left_child_height = self._get_node_height(node.get_left_child())

        if right_child_height > left_child_height:
            return 'right'
        elif right_child_height < left_child_height:
            return 'left'
        else:
            return 'equal'

    def _double_rotation(self, node):
        heavy_path = self._get_heavy_path(node)
        if heavy_path == 'left':
            self._left_rotate(node.get_left_child())
            self._right_rotate(node)
        elif heavy_path == 'right':
            self._right_rotate(node.get_right_child())
            self._left_rotate(node)
        else:
            raise AVLException(
                    message='At this point in the algorithm,\
                             the paths cannot have equal weights'
            )
        return node.get_parent()

    def _simple_rotation(self, node):
        heavy_path = self._get_heavy_path(node)
        if heavy_path == 'left':
            self._right_rotate(node)
        elif heavy_path == 'right':
            self._left_rotate(node)
        else:
            raise AVLException(
                    message='At this point in the algorithm,\
                             the paths cannot have equal weights'
            )
        return node.get_parent()

    def _bubble_down_to_place(self, node, new_node):
        if node is None:
            self._set_root(new_node)
            return

        if node.get_key() > new_node.get_key():
            if node.get_left_child() is None:
                node.set_left_child(new_node)
                new_node.set_parent(node)
            else:
                self._bubble_down_to_place(node.get_left_child(), new_node)

        elif node.get_key() < new_node.get_key():
            if node.get_right_child() is None:
                node.set_right_child(new_node)
                new_node.set_parent(node)
            else:
                self._bubble_down_to_place(node.get_right_child(), new_node)

    def _update_node_counts(self, node):
        if node is None:
            return

        left_child_node_count = self._get_node_count(node.get_left_child())
        right_child_node_count = self._get_node_count(node.get_right_child())

        node.set_node_count(left_child_node_count + right_child_node_count + 1)

        self._update_node_counts(node.get_parent())

    def _get_node_count(self, node):
        if node is None:
            return 0
        return node.get_node_count()

    def _update_heights(self, node):
        if node is None:
            return

        left_child_height = self._get_node_height(node.get_left_child())
        right_child_height = self._get_node_height(node.get_right_child())

        new_height = max(left_child_height, right_child_height) + 1

        node._set_height(new_height)

        self._update_heights(node.get_parent())

    def _get_node_height(self, node):
        height = -1
        if node:
            height = node.get_height()
        return height

    def _right_rotate(self, node):
        parent = node.get_parent()
        A = node
        B = node.get_left_child()
        b = B.get_right_child()

        if parent:
            if parent.get_left_child() == A:
                parent.set_left_child(B)
            else:
                parent.set_right_child(B)

        B.set_parent(parent)
        B.set_right_child(A)
        A.set_parent(B)
        A.set_left_child(b)
        if b:
            b.set_parent(A)

        if self._root == A:
            self._set_root(B)

        self._update_heights(A)
        self._update_node_counts(A)

    def _left_rotate(self, node):
        parent = node.get_parent()
        A = node
        B = node.get_right_child()
        b = B.get_left_child()

        if parent:
            if parent.get_left_child() == A:
                parent.set_left_child(B)
            else:
                parent.set_right_child(B)

        B.set_parent(parent)
        B.set_left_child(A)
        A.set_parent(B)
        A.set_right_child(b)
        if b:
            b.set_parent(A)

        if self._root == A:
            self._set_root(B)

        self._update_heights(A)
        self._update_node_counts(A)

    def _set_root(self, node):
        self._root = node
