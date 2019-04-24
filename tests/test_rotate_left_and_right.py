from sure import expect

from avl import Node, AVL


def create_not_zig_zag_tree_left():
    node_12 = Node(12)
    node_11 = Node(11)
    node_10 = Node(10)

    node_12.set_left_child(node_11)
    node_11.set_parent(node_12)

    node_11.set_left_child(node_10)
    node_10.set_parent(node_11)

    node_12._set_height(2)
    node_11._set_height(1)
    node_10._set_height(0)

    return node_12


def create_not_zig_zag_tree_right():
    node_10 = Node(10)
    node_11 = Node(11)
    node_12 = Node(12)

    node_10.set_right_child(node_11)
    node_11.set_parent(node_10)

    node_11.set_right_child(node_12)
    node_12.set_parent(node_11)

    node_12._set_height(0)
    node_11._set_height(1)
    node_10._set_height(2)

    return node_10

def create_zig_zag_tree_right_left():
    node_12 = Node(12)
    node_14 = Node(14)
    node_13 = Node(13)

    node_12.set_right_child(node_14)
    node_14.set_parent(node_12)

    node_14.set_left_child(node_13)
    node_13.set_parent(node_14)

    node_12._set_height(2)
    node_14._set_height(1)
    node_13._set_height(0)

    return node_12


def create_zig_zag_tree_left_right():
    node_12 = Node(12)
    node_6 = Node(6)
    node_8 = Node(8)

    node_12.set_left_child(node_6)
    node_6.set_parent(node_12)

    node_6.set_right_child(node_8)
    node_8.set_parent(node_6)

    node_12._set_height(2)
    node_6._set_height(1)
    node_8._set_height(0)

    return node_12


def create_balanced_tree():
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)

    node_1.set_left_child(node_0)
    node_1.set_right_child(node_2)
    node_0.set_parent(node_1)
    node_2.set_parent(node_1)

    node_1._set_height(1)
    node_0._set_height(0)
    node_2._set_height(0)

    return node_1


def create_unbalanced_tree():
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_4 = Node(4)
    node_5 = Node(5)

    node_1.set_left_child(node_0)
    node_1.set_right_child(node_2)
    node_0.set_parent(node_1)
    node_2.set_parent(node_1)

    node_2.set_right_child(node_4)
    node_4.set_parent(node_2)

    node_4.set_right_child(node_5)
    node_5.set_parent(node_4)

    node_1._set_height(3)
    node_0._set_height(0)
    node_2._set_height(2)
    node_4._set_height(1)
    node_5._set_height(0)

    return node_1


def create_unbalanced_tree_with_equal_weight_on_second_level():
    node_5 = Node(5)
    node_4 = Node(4)
    node_2 = Node(2)
    node_3 = Node(3)

    node_5.set_left_child(node_4)
    node_4.set_parent(node_5)

    node_4.set_left_child(node_2)
    node_4.set_right_child(node_3)
    node_2.set_parent(node_4)
    node_3.set_parent(node_4)

    node_2._set_height(0)
    node_3._set_height(0)
    node_4._set_height(1)
    node_5._set_height(2)

    node_2.set_node_count(1)
    node_3.set_node_count(1)
    node_4.set_node_count(3)
    node_5.set_node_count(4)

    return node_5


def create_unbalanced_tree_with_zig_zag():
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.set_left_child(node_0)
    node_1.set_right_child(node_2)
    node_0.set_parent(node_1)
    node_2.set_parent(node_1)

    node_2.set_right_child(node_4)
    node_4.set_parent(node_2)

    node_4.set_left_child(node_3)
    node_3.set_parent(node_4)

    node_1._set_height(3)
    node_0._set_height(0)
    node_2._set_height(2)
    node_4._set_height(1)
    node_3._set_height(0)

    return (node_1, node_3)


def create_left_rotable_tree():
    A = Node(24, name='A')
    B = Node(18, name='B')
    a = Node(16, name='a')
    b = Node(17, name='b')
    c = Node(26, name='c')

    A.set_left_child(c)
    A.set_right_child(B)
    B.set_parent(A)
    c.set_parent(A)
    B.set_left_child(b)
    B.set_right_child(a)
    b.set_parent(B)
    a.set_parent(B)

    A._set_height(2)
    B._set_height(1)
    a._set_height(0)
    b._set_height(0)
    c._set_height(0)

    return A


def create_right_rotable_tree():
    A = Node(24, name='A')
    B = Node(18, name='B')
    a = Node(16, name='a')
    b = Node(14, name='b')
    c = Node(17, name='c')

    A.set_right_child(c)
    c.set_parent(A)
    A.set_left_child(B)
    B.set_parent(A)
    B.set_right_child(b)
    B.set_left_child(a)
    a.set_parent(B)
    b.set_parent(B)

    A._set_height(2)
    B._set_height(1)
    a._set_height(0)
    b._set_height(0)
    c._set_height(0)

    return A


def create_tree_for_testing_predecessor():
    node_90 = Node(90)
    node_50 = Node(50)
    node_150 = Node(150)
    node_160 = Node(160)
    node_140 = Node(140)
    node_144 = Node(144)
    node_147 = Node(147)

    node_90.set_right_child(node_150)
    node_90.set_left_child(node_50)
    node_150.set_parent(node_90)
    node_50.set_parent(node_90)

    node_150.set_right_child(node_160)
    node_150.set_left_child(node_140)
    node_160.set_parent(node_150)
    node_140.set_parent(node_150)

    node_140.set_right_child(node_144)
    node_144.set_parent(node_140)

    node_144.set_right_child(node_147)
    node_147.set_parent(node_144)

    return node_90


def create_tree_for_testing_successor():
    node_40 = Node(40)
    node_50 = Node(50)
    node_55 = Node(55)
    node_65 = Node(65)
    node_70 = Node(70)
    node_90 = Node(90)
    node_105 = Node(105)

    node_90.set_right_child(node_105)
    node_90.set_left_child(node_50)
    node_105.set_parent(node_90)
    node_50.set_parent(node_90)

    node_50.set_right_child(node_70)
    node_50.set_left_child(node_40)
    node_70.set_parent(node_50)
    node_40.set_parent(node_50)

    node_70.set_left_child(node_65)
    node_65.set_parent(node_70)

    node_65.set_left_child(node_55)
    node_55.set_parent(node_65)

    return node_90


def create_valid_avl_tree():
    node_10 = Node(10)
    node_minus_3 = Node(-3)
    node_minus_20 = Node(-20)
    node_5 = Node(5)
    node_3 = Node(3)
    node_15 = Node(15)
    node_20 = Node(20)
    node_12 = Node(12)
    node_13 = Node(13)

    node_10.set_left_child(node_minus_3)
    node_10.set_right_child(node_15)
    node_minus_3.set_parent(node_10)
    node_15.set_parent(node_10)

    node_minus_3.set_right_child(node_5)
    node_minus_3.set_left_child(node_minus_20)
    node_5.set_parent(node_minus_3)
    node_minus_20.set_parent(node_minus_3)

    node_5.set_left_child(node_3)
    node_3.set_parent(node_5)

    node_15.set_left_child(node_12)
    node_15.set_right_child(node_20)
    node_12.set_parent(node_15)
    node_20.set_parent(node_15)

    node_12.set_right_child(node_13)
    node_13.set_parent(node_12)

    node_10._set_height(3)
    node_minus_3._set_height(2)
    node_minus_20._set_height(0)
    node_5._set_height(1)
    node_3._set_height(0)
    node_15._set_height(2)
    node_20._set_height(0)
    node_12._set_height(1)
    node_13._set_height(0)

    node_10.set_node_count(9)
    node_minus_3.set_node_count(4)
    node_minus_20.set_node_count(1)
    node_5.set_node_count(2)
    node_3.set_node_count(1)
    node_15.set_node_count(4)
    node_20.set_node_count(1)
    node_12.set_node_count(2)
    node_13.set_node_count(1)

    return node_10


class TestAVL:
    def setUp(self): pass

    def tearDown(self): pass

    def test_higher_inmediate(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        node_5 = tree.search_higher_inmediate(5)
        node_3 = tree.search_higher_inmediate(2)
        node_minus_20 = tree.search_higher_inmediate(-30)
        node_minus_3 = tree.search_higher_inmediate(-15)

        expect(node_5.get_key()).to.equal(5)
        expect(node_3.get_key()).to.equal(3)
        expect(node_minus_20.get_key()).to.equal(-20)
        expect(node_minus_3.get_key()).to.equal(-3)

    def test_lower_inmediate(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        node_5 = tree.search_lower_inmediate(5)
        node_minus_3 = tree.search_lower_inmediate(2)

        expect(node_5.get_key()).to.equal(5)
        expect(node_minus_3.get_key()).to.equal(-3)

    def test_list_node_in_range_list(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        nodes_from_minus_3_to_15 = \
            set([node.get_key() for node in tree.list_nodes_in_range(-4, 16)])

        expect(nodes_from_minus_3_to_15).to.equal(
            set([10, -3, 5, 3, 15, 12, 13])
        )

    def test_count(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        expect(tree.count(-3, 15)).to.equal(7)
        expect(tree.count(10, 15)).to.equal(4)
        expect(tree.count(-2, 10)).to.equal(3)
        expect(tree.count(-100, 100)).to.equal(9)

    def test_rank(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        expect(tree.rank(15)).to.equal(8)
        expect(tree.rank(20)).to.equal(9)
        expect(tree.rank(12)).to.equal(6)
        expect(tree.rank(-20)).to.equal(1)
        expect(tree.rank(3)).to.equal(3)

    def test_delete_of_a_single_root_node(self):
        tree = AVL(Node(10))
        tree.delete(10)

        expect(tree.get_root()).to.equal(None)

    def test_delete_that_requires_a_balance(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        tree.delete(-20)

        node_3 = node_10.get_left_child()
        node_15 = node_10.get_right_child()
        node_minus_3 = node_3.get_left_child()
        node_5 = node_3.get_right_child()

        expect(node_10.get_key()).to.equal(10)
        expect(node_minus_3.get_key()).to.equal(-3)
        expect(node_3.get_key()).to.equal(3)
        expect(node_5.get_key()).to.equal(5)
        expect(node_15.get_key()).to.equal(15)

        expect(node_10.get_height()).to.equal(3)
        expect(node_minus_3.get_height()).to.equal(0)
        expect(node_3.get_height()).to.equal(1)
        expect(node_5.get_height()).to.equal(0)
        expect(node_15.get_height()).to.equal(2)

    def test_delete_of_node_with_two_children(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        tree.delete(10)

        node_12 = tree.get_root()
        node_15 = node_12.get_right_child()
        node_13 = node_15.get_left_child()
        node_20 = node_15.get_right_child()
        node_minus_3 = node_12.get_left_child()

        expect(node_12.get_key()).to.equal(12)
        expect(node_15.get_key()).to.equal(15)
        expect(node_13.get_key()).to.equal(13)
        expect(node_20.get_key()).to.equal(20)
        expect(node_minus_3.get_key()).to.equal(-3)

        expect(node_12.get_height()).to.equal(3)
        expect(node_minus_3.get_height()).to.equal(2)
        expect(node_15.get_height()).to.equal(1)
        expect(node_13.get_height()).to.equal(0)
        expect(node_20.get_height()).to.equal(0)

    def test_delete_of_root_with_one_children(self):
        tree = AVL()
        tree.insert(0)
        tree.insert(2)

        tree.delete(0)

        node_2 = tree.get_root()
        expect(node_2.get_parent()).to.equal(None)
        expect(node_2.get_left_child()).to.equal(None)
        expect(node_2.get_right_child()).to.equal(None)

    def test_delete_of_node_with_one_children(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        tree.delete(5)

        node_10 = tree.get_root()
        node_minus_3 = node_10.get_left_child()
        node_3 = node_minus_3.get_right_child()
        node_minus_20 = node_minus_3.get_left_child()

        expect(node_10.get_key()).to.equal(10)
        expect(node_minus_3.get_key()).to.equal(-3)
        expect(node_3.get_key()).to.equal(3)
        expect(node_minus_20.get_key()).to.equal(-20)

        expect(node_3.get_height()).to.equal(0)
        expect(node_minus_20.get_height()).to.equal(0)
        expect(node_minus_3.get_height()).to.equal(1)
        expect(node_10.get_height()).to.equal(3)

    def test_delete_of_node_with_no_children(self):
        node_10 = create_valid_avl_tree()
        tree = AVL(node_10)

        tree.delete(3)

        node_10 = tree.get_root()
        node_minus_3 = node_10.get_left_child()
        node_5 = node_minus_3.get_right_child()
        node_3 = node_5.get_left_child()

        expect(node_10.get_key()).to.equal(10)
        expect(node_minus_3.get_key()).to.equal(-3)
        expect(node_5.get_key()).to.equal(5)
        expect(node_3).to.equal(None)

        expect(node_5.get_height()).to.equal(0)
        expect(node_minus_3.get_height()).to.equal(1)
        expect(node_10.get_height()).to.equal(3)

    def test_predecessor_when_there_is_none(self):
        node_90 = create_tree_for_testing_predecessor()
        tree = AVL(node_90)
        expect(tree.get_predecessor(tree.search(50))).to.be.equal(None)

    def test_predecessor_when_predecessor_is_parent(self):
        node_90 = create_tree_for_testing_predecessor()
        tree = AVL(node_90)
        expect(tree.get_predecessor(tree.search(160))).to.be.equal(
            tree.get_root().get_right_child()
        )

    def test_predecessor_when_predecessor_is_in_left_subtree(self):
        node_90 = create_tree_for_testing_predecessor()
        tree = AVL(node_90)
        expect(tree.get_predecessor(tree.search(150))).to.be.equal(
            tree.get_root()
            .get_right_child()
            .get_left_child()
            .get_right_child()
            .get_right_child()
        )

    def test_predecessor_when_succesor_is_the_first_turn_going_up(self):
        node_90 = create_tree_for_testing_predecessor()
        tree = AVL(node_90)
        expect(tree.get_predecessor(tree.search(140))).to.equal(node_90)

    def test_succesor_when_there_is_none(self):
        node_90 = create_tree_for_testing_successor()
        tree = AVL(node_90)
        expect(tree.get_successor(tree.search(105))).to.be.equal(None)

    def test_succesor_when_succesor_is_parent(self):
        node_90 = create_tree_for_testing_successor()
        tree = AVL(node_90)
        expect(tree.get_successor(tree.search(40))).to.be.equal(
            tree.get_root().get_left_child()
        )

    def test_succesor_when_succesor_is_in_right_subtree(self):
        node_90 = create_tree_for_testing_successor()
        tree = AVL(node_90)
        expect(tree.get_successor(tree.search(50))).to.be.equal(
            tree.get_root()
            .get_left_child()
            .get_right_child()
            .get_left_child()
            .get_left_child()
        )

    def test_succesor_when_succesor_is_the_first_turn_going_up(self):
        node_90 = create_tree_for_testing_successor()
        tree = AVL(node_90)
        expect(tree.get_successor(tree.search(70)).get_key()).to.equal(node_90.get_key())

    def test_find_smallest(self):
        node_1 = create_balanced_tree()
        balanced_tree = AVL(node_1)
        expect(balanced_tree.find_smallest()).to.be.equal(
            balanced_tree.get_root().get_left_child()
        )

    def test_search_with_invalid_key(self):
        node_1 = create_balanced_tree()
        balanced_tree = AVL(node_1)
        expect(balanced_tree.search(3)).to.be.equal(None)

    def test_search_with_valid_key(self):
        node_1 = create_balanced_tree()
        balanced_tree = AVL(node_1)
        expect(balanced_tree.search(2)).to.be.equal(
            balanced_tree.get_root().get_right_child()
        )

    def test_insert(self):
        tree = AVL()
        tree.insert(10)
        tree.insert(20)
        tree.insert(5)
        tree.insert(-3)
        tree.insert(-20)
        tree.insert(15)
        tree.insert(12)
        tree.insert(13)

        node_10 = tree.get_root()
        node_minus_3 = node_10.get_left_child()
        node_minus_20 = node_minus_3.get_left_child()
        node_5 = node_minus_3.get_right_child()
        node_15 = node_10.get_right_child()
        node_20 = node_15.get_right_child()
        node_12 = node_15.get_left_child()
        node_13 = node_12.get_right_child()

        expect(node_10.get_key()).to.be.equal(10)
        expect(node_minus_3.get_key()).to.be.equal(-3)
        expect(node_minus_20.get_key()).to.be.equal(-20)
        expect(node_5.get_key()).to.be.equal(5)
        expect(node_15.get_key()).to.be.equal(15)
        expect(node_20.get_key()).to.be.equal(20)
        expect(node_12.get_key()).to.be.equal(12)
        expect(node_13.get_key()).to.be.equal(13)

        expect(node_10.get_height()).to.be.equal(3)
        expect(node_minus_3.get_height()).to.be.equal(1)
        expect(node_minus_20.get_height()).to.be.equal(0)
        expect(node_5.get_height()).to.be.equal(0)
        expect(node_15.get_height()).to.be.equal(2)
        expect(node_20.get_height()).to.be.equal(0)
        expect(node_12.get_height()).to.be.equal(1)
        expect(node_13.get_height()).to.be.equal(0)

        expect(node_10.get_node_count()).to.be.equal(8)
        expect(node_minus_3.get_node_count()).to.be.equal(3)
        expect(node_minus_20.get_node_count()).to.be.equal(1)
        expect(node_5.get_node_count()).to.be.equal(1)
        expect(node_15.get_node_count()).to.be.equal(4)
        expect(node_20.get_node_count()).to.be.equal(1)
        expect(node_12.get_node_count()).to.be.equal(2)
        expect(node_13.get_node_count()).to.be.equal(1)

    def test_balance_tree_with_same_weight_on_second_level(self):
        node_5 = create_unbalanced_tree_with_equal_weight_on_second_level()
        tree = AVL(node_5)
        tree._balance(node_5)

        node_4 = tree.get_root()
        node_2 = node_4.get_left_child()
        node_5 = node_4.get_right_child()
        node_3 = node_5.get_left_child()

        expect(node_4.get_key()).to.equal(4)
        expect(node_2.get_key()).to.equal(2)
        expect(node_5.get_key()).to.equal(5)
        expect(node_3.get_key()).to.equal(3)

    def test_balance_tree(self):
        node_1, node_3 = create_unbalanced_tree_with_zig_zag()
        tree = AVL(node_1)
        tree._balance(node_3)

        node_1 = tree.get_root()
        node_0 = node_1.get_left_child()
        node_3 = node_1.get_right_child()
        node_2 = node_3.get_left_child()
        node_4 = node_3.get_right_child()

        expect(node_0.get_key()).to.be.equal(0)
        expect(node_1.get_key()).to.be.equal(1)
        expect(node_2.get_key()).to.be.equal(2)
        expect(node_3.get_key()).to.be.equal(3)
        expect(node_4.get_key()).to.be.equal(4)

        expect(node_0.get_height()).to.be.equal(0)
        expect(node_1.get_height()).to.be.equal(2)
        expect(node_2.get_height()).to.be.equal(0)
        expect(node_3.get_height()).to.be.equal(1)
        expect(node_4.get_height()).to.be.equal(0)

        expect(node_0.get_node_count()).to.be.equal(1)
        expect(node_1.get_node_count()).to.be.equal(5)
        expect(node_2.get_node_count()).to.be.equal(1)
        expect(node_3.get_node_count()).to.be.equal(3)
        expect(node_4.get_node_count()).to.be.equal(1)

    def test_simple_rotation_with_left_left_tree(self):
        node_12 = create_not_zig_zag_tree_left()
        tree = AVL(node_12)
        returned_tree = tree._simple_rotation(tree.get_root())

        node_11 = tree.get_root()
        node_10 = node_11.get_left_child()
        node_12 = node_11.get_right_child()

        expect(node_10.get_key()).to.be.equal(10)
        expect(node_11.get_key()).to.be.equal(11)
        expect(node_12.get_key()).to.be.equal(12)
        expect(returned_tree).to.be.equal(node_11)

    def test_simple_rotation_with_right_right_tree(self):
        node_10 = create_not_zig_zag_tree_right()
        tree = AVL(node_10)
        returned_tree = tree._simple_rotation(tree.get_root())

        node_11 = tree.get_root()
        node_10 = node_11.get_left_child()
        node_12 = node_11.get_right_child()

        expect(node_10.get_key()).to.be.equal(10)
        expect(node_11.get_key()).to.be.equal(11)
        expect(node_12.get_key()).to.be.equal(12)
        expect(returned_tree).to.be.equal(node_11)

    def test_double_rotation_with_right_zig_zag_tree(self):
        node_12 = create_zig_zag_tree_right_left()
        tree = AVL(node_12)
        returned_node = tree._double_rotation(node_12)

        node_13 = tree.get_root()
        node_12 = node_13.get_left_child()
        node_14 = node_13.get_right_child()

        expect(node_12.get_key()).to.be.equal(12)
        expect(node_13.get_key()).to.be.equal(13)
        expect(node_14.get_key()).to.be.equal(14)
        expect(returned_node).to.be.equal(node_13)

    def test_double_rotation_with_left_zig_zag_tree(self):
        node_12 = create_zig_zag_tree_left_right()
        tree = AVL(node_12)
        returned_node = tree._double_rotation(node_12)

        node_8 = tree.get_root()
        node_6 = node_8.get_left_child()
        node_12 = node_8.get_right_child()

        expect(node_8.get_key()).to.be.equal(8)
        expect(node_6.get_key()).to.be.equal(6)
        expect(node_12.get_key()).to.be.equal(12)
        expect(returned_node).to.be.equal(node_8)

    def test_is_heavy_path_zig_zag_left_left_tree(self):
        node_12 = create_not_zig_zag_tree_left()
        tree = AVL(node_12)
        expect(tree._is_heavy_path_zig_zag(tree.get_root())).to.be(False)

    def test_is_heavy_path_zig_zag_right_right_tree(self):
        node_10 = create_not_zig_zag_tree_right()
        tree = AVL(node_10)
        expect(tree._is_heavy_path_zig_zag(tree.get_root())).to.be(False)

    def test_is_heavy_path_zig_zag_right_left_tree(self):
        node_12 = create_zig_zag_tree_right_left()
        tree = AVL(node_12)
        expect(tree._is_heavy_path_zig_zag(tree.get_root())).to.be(True)

    def test_is_heavy_path_zig_zag_left_right_tree(self):
        node_12 = create_zig_zag_tree_left_right()
        tree = AVL(node_12)
        expect(tree._is_heavy_path_zig_zag(tree.get_root())).to.be(True)

    def test_has_unbalanced_children_with_unbalanced_tree(self):
        root = create_unbalanced_tree()
        tree = AVL(root)
        expect(tree._has_unbalanced_children(tree.get_root())).to.be(True)

    def test_has_unbalanced_children_with_balanced_tree(self):
        root = create_balanced_tree()
        tree = AVL(root)
        expect(tree._has_unbalanced_children(tree.get_root())).to.be(False)

    def test_update_node_count(self):
        node_5 = Node(5)
        node_0 = Node(0)
        node_12 = Node(12)

        tree = AVL(node_5)
        tree._set_root(node_5)
        node_5.set_left_child(node_0)
        node_5.set_right_child(node_12)
        node_0.set_parent(node_5)
        node_12.set_parent(node_5)

        node_5.set_node_count(2)

        node_6 = Node(6)
        node_12.set_left_child(node_6)
        node_6.set_parent(node_12)

        tree._update_node_counts(node_6)

        expect(node_5.get_node_count()).to.be.equal(4)
        expect(node_0.get_node_count()).to.be.equal(1)
        expect(node_12.get_node_count()).to.be.equal(2)
        expect(node_6.get_node_count()).to.be.equal(1)

    def test_update_heights(self):
        node_5 = Node(5)
        node_0 = Node(0)
        node_12 = Node(12)

        tree = AVL(node_5)
        tree._set_root(node_5)
        node_5.set_left_child(node_0)
        node_5.set_right_child(node_12)
        node_0.set_parent(node_5)
        node_12.set_parent(node_5)

        node_5._set_height(1)
        node_0._set_height(0)
        node_12._set_height(0)

        node_6 = Node(6)
        node_12.set_left_child(node_6)
        node_6.set_parent(node_12)

        tree._update_heights(node_6)

        expect(node_5.get_height()).to.be.equal(2)
        expect(node_0.get_height()).to.be.equal(0)
        expect(node_12.get_height()).to.be.equal(1)
        expect(node_6.get_height()).to.be.equal(0)

    def test_bubble_down(self):
        tree = AVL(Node(5))
        tree._bubble_down_to_place(tree.get_root(), Node(12))
        tree._bubble_down_to_place(tree.get_root(), Node(0))
        tree._bubble_down_to_place(tree.get_root(), Node(6))
        tree._bubble_down_to_place(tree.get_root(), Node(8))

        node_5 = tree.get_root()
        node_12 = node_5.get_right_child()
        node_0 = node_5.get_left_child()
        node_6 = node_12.get_left_child()
        node_8 = node_6.get_right_child()

        expect(node_5.get_key()).to.be.equal(5)
        expect(node_12.get_key()).to.be.equal(12)
        expect(node_0.get_key()).to.be.equal(0)
        expect(node_6.get_key()).to.be.equal(6)
        expect(node_8.get_key()).to.be.equal(8)

    def test_rotate_right_subtree_is_right_child_from_root(self):
        A = create_right_rotable_tree()

        root = Node(10, name='root')
        root.set_right_child(A)
        A.set_parent(root)
        root._set_height(3)

        rotable_to_right_tree = AVL(root)
        rotable_to_right_tree._right_rotate(
            rotable_to_right_tree.get_root().get_right_child()
        )

        root = rotable_to_right_tree.get_root()
        B = root.get_right_child()
        A = B.get_right_child()
        a = B.get_left_child()
        c = A.get_right_child()
        b = A.get_left_child()

        expect(root.get_name()).to.be.equal('root')
        expect(B.get_name()).to.be.equal('B')
        expect(A.get_name()).to.be.equal('A')
        expect(a.get_name()).to.be.equal('a')
        expect(b.get_name()).to.be.equal('b')
        expect(c.get_name()).to.be.equal('c')

        expect(root.get_height()).to.be.equal(3)
        expect(B.get_height()).to.be.equal(2)
        expect(A.get_height()).to.be.equal(1)
        expect(a.get_height()).to.be.equal(0)
        expect(b.get_height()).to.be.equal(0)
        expect(c.get_height()).to.be.equal(0)

        expect(root.get_node_count()).to.be.equal(6)
        expect(B.get_node_count()).to.be.equal(5)
        expect(A.get_node_count()).to.be.equal(3)
        expect(a.get_node_count()).to.be.equal(1)
        expect(b.get_node_count()).to.be.equal(1)
        expect(c.get_node_count()).to.be.equal(1)

    def test_rotate_right_subtree_is_left_child_from_root(self):
        A = create_right_rotable_tree()

        root = Node(10, name='root')
        root.set_left_child(A)
        A.set_parent(root)

        rotable_to_right_tree = AVL(root)
        rotable_to_right_tree._right_rotate(
            rotable_to_right_tree.get_root().get_left_child()
        )

        root = rotable_to_right_tree.get_root()
        B = root.get_left_child()
        A = B.get_right_child()
        a = B.get_left_child()
        c = A.get_right_child()
        b = A.get_left_child()

        expect(root.get_name()).to.be.equal('root')
        expect(B.get_name()).to.be.equal('B')
        expect(A.get_name()).to.be.equal('A')
        expect(a.get_name()).to.be.equal('a')
        expect(b.get_name()).to.be.equal('b')
        expect(c.get_name()).to.be.equal('c')

        expect(root.get_height()).to.be.equal(3)
        expect(B.get_height()).to.be.equal(2)
        expect(A.get_height()).to.be.equal(1)
        expect(a.get_height()).to.be.equal(0)
        expect(b.get_height()).to.be.equal(0)
        expect(c.get_height()).to.be.equal(0)

        expect(root.get_node_count()).to.be.equal(6)
        expect(B.get_node_count()).to.be.equal(5)
        expect(A.get_node_count()).to.be.equal(3)
        expect(a.get_node_count()).to.be.equal(1)
        expect(b.get_node_count()).to.be.equal(1)
        expect(c.get_node_count()).to.be.equal(1)

    def test_rotate_right_subtree_with_no_parent(self):
        A = create_right_rotable_tree()

        rotable_to_right_tree = AVL(A)
        rotable_to_right_tree._right_rotate(rotable_to_right_tree.get_root())

        B = rotable_to_right_tree.get_root()
        A = B.get_right_child()
        a = B.get_left_child()
        c = A.get_right_child()
        b = A.get_left_child()

        expect(B.get_name()).to.be.equal('B')
        expect(A.get_name()).to.be.equal('A')
        expect(a.get_name()).to.be.equal('a')
        expect(b.get_name()).to.be.equal('b')
        expect(c.get_name()).to.be.equal('c')

        expect(B.get_height()).to.be.equal(2)
        expect(A.get_height()).to.be.equal(1)
        expect(a.get_height()).to.be.equal(0)
        expect(b.get_height()).to.be.equal(0)
        expect(c.get_height()).to.be.equal(0)

        expect(B.get_node_count()).to.be.equal(5)
        expect(A.get_node_count()).to.be.equal(3)
        expect(b.get_node_count()).to.be.equal(1)
        expect(c.get_node_count()).to.be.equal(1)

    def test_rotate_left_subtree_is_right_child_from_root(self):
        A = create_left_rotable_tree()

        root = Node(10, name='root')
        root.set_right_child(A)
        A.set_parent(root)

        rotable_to_left_tree = AVL(root)
        rotable_to_left_tree._left_rotate(
            rotable_to_left_tree.get_root().get_right_child()
        )

        root = rotable_to_left_tree.get_root()
        B = root.get_right_child()
        a = B.get_right_child()
        A = B.get_left_child()
        b = A.get_right_child()
        c = A.get_left_child()

        expect(root.get_name()).to.be.equal('root')
        expect(B.get_name()).to.be.equal('B')
        expect(A.get_name()).to.be.equal('A')
        expect(c.get_name()).to.be.equal('c')
        expect(a.get_name()).to.be.equal('a')
        expect(b.get_name()).to.be.equal('b')

        expect(root.get_height()).to.be.equal(3)
        expect(B.get_height()).to.be.equal(2)
        expect(A.get_height()).to.be.equal(1)
        expect(a.get_height()).to.be.equal(0)
        expect(b.get_height()).to.be.equal(0)
        expect(c.get_height()).to.be.equal(0)

        expect(root.get_node_count()).to.be.equal(6)
        expect(B.get_node_count()).to.be.equal(5)
        expect(A.get_node_count()).to.be.equal(3)
        expect(a.get_node_count()).to.be.equal(1)
        expect(b.get_node_count()).to.be.equal(1)
        expect(c.get_node_count()).to.be.equal(1)

    def test_rotate_left_subtree_is_left_child_from_root(self):
            A = create_left_rotable_tree()

            root = Node(10, name='root')
            root.set_left_child(A)
            A.set_parent(root)

            rotable_to_left_tree = AVL(root)
            rotable_to_left_tree._left_rotate(
                rotable_to_left_tree.get_root().get_left_child()
            )

            root = rotable_to_left_tree.get_root()
            B = root.get_left_child()
            a = B.get_right_child()
            A = B.get_left_child()
            b = A.get_right_child()
            c = A.get_left_child()

            expect(root.get_name()).to.be.equal('root')
            expect(B.get_name()).to.be.equal('B')
            expect(A.get_name()).to.be.equal('A')
            expect(c.get_name()).to.be.equal('c')
            expect(a.get_name()).to.be.equal('a')
            expect(b.get_name()).to.be.equal('b')

            expect(root.get_height()).to.be.equal(3)
            expect(B.get_height()).to.be.equal(2)
            expect(A.get_height()).to.be.equal(1)
            expect(a.get_height()).to.be.equal(0)
            expect(b.get_height()).to.be.equal(0)
            expect(c.get_height()).to.be.equal(0)

            expect(root.get_node_count()).to.be.equal(6)
            expect(B.get_node_count()).to.be.equal(5)
            expect(A.get_node_count()).to.be.equal(3)
            expect(a.get_node_count()).to.be.equal(1)
            expect(b.get_node_count()).to.be.equal(1)
            expect(c.get_node_count()).to.be.equal(1)

    def test_rotate_left_subtree_with_no_parent(self):
            A = create_left_rotable_tree()

            rotable_to_left_tree = AVL(A)
            rotable_to_left_tree._left_rotate(rotable_to_left_tree.get_root())

            B = rotable_to_left_tree.get_root()
            a = B.get_right_child()
            A = B.get_left_child()
            b = A.get_right_child()
            c = A.get_left_child()

            expect(B.get_name()).to.be.equal('B')
            expect(A.get_name()).to.be.equal('A')
            expect(c.get_name()).to.be.equal('c')
            expect(a.get_name()).to.be.equal('a')
            expect(b.get_name()).to.be.equal('b')

            expect(B.get_height()).to.be.equal(2)
            expect(A.get_height()).to.be.equal(1)
            expect(a.get_height()).to.be.equal(0)
            expect(b.get_height()).to.be.equal(0)
            expect(c.get_height()).to.be.equal(0)

            expect(B.get_node_count()).to.be.equal(5)
            expect(A.get_node_count()).to.be.equal(3)
            expect(a.get_node_count()).to.be.equal(1)
            expect(b.get_node_count()).to.be.equal(1)
            expect(c.get_node_count()).to.be.equal(1)
