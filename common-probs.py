# 1. Find the missing number in the array
# You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.

def find_missing(input):
    # calculate sum of all elements
    # in input list
    sum_of_elements = sum(input)
    # There is exactly 1 number missing
    n = len(input) + 1
    actual_sum = (n * (n + 1)) / 2
    return actual_sum - sum_of_elements

# 2. Determine if the sum of two integers is equal to the given value
# Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:


def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return True

        found_values.add(a)

    return False

# 3. Merge two sorted linked lists


def merge_sorted(head1, head2):
    # if both lists are empty then merged list is also empty
    # if one of the lists is empty then other is the merged list
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead

# 4. Copy linked list with arbitrary pointer


def deep_copy_arbitrary_pointer(head):
    if head == None:
        return None

    current = head
    new_head = None
    new_prev = None
    ht = dict()

    # create copy of the linked list, recording the corresponding
    # nodes in hashmap without updating arbitrary pointer
    while current != None:
        new_node = LinkedListNode(current.data)

        # copy the old arbitrary pointer in the new node
        new_node.arbitrary = current.arbitrary

        if new_prev != None:
            new_prev.next = new_node
        else:
            new_head = new_node

        ht[current] = new_node

        new_prev = new_node
        current = current.next

    new_current = new_head

    # updating arbitrary pointer
    while new_current != None:
        if new_current.arbitrary != None:
            node = ht[new_current.arbitrary]

            new_current.arbitrary = node

        new_current = new_current.next

    return new_head

# 5. Level Order Traversal of Binary Tree
# Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines.
# Using two queues


def level_order_traversal(root):
    if root == None:
        return
    result = ""
    queues = [deque(), deque()]

    current_queue = queues[0]
    next_queue = queues[1]

    current_queue.append(root)
    level_number = 0

    while current_queue:
        temp = current_queue.popleft()
        result += str(temp.data) + " "

        if temp.left != None:
            next_queue.append(temp.left)

        if temp.right != None:
            next_queue.append(temp.right)

        if not current_queue:
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]
    return result

# 6. Determine if a binary tree is a binary search tree


def is_bst_rec(root, min_value, max_value):
    if root == None:
        return True

    if root.data < min_value or root.data > max_value:
        return False

    return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)


def is_bst(root):
    return is_bst_rec(root, -sys.maxsize - 1, sys.maxsize)


def str_rev(str, start, end):
    if str == None or len(str) < 2:
        return

    while start < end:
        temp = str[start]
        str[start] = str[end]
        str[end] = temp

        start += 1
        end -= 1
    return str


# 8. Reverse Words in a Sentence
# Reverse the order of words in a given sentence(an array of characters).


def reverse_words(sentence):

    # Here sentence is a null-terminated string ending with char '\0'.

    if sentence == None or len(sentence) == 0:
        return

    #  To reverse all words in the string, we will first reverse
    #  the string. Now all the words are in the desired location, but
    #  in reverse order: "Hello World" -> "dlroW olleH".

    str_len = len(sentence)
    sentence = str_rev(sentence, 0, str_len - 2)

    # Now, let's iterate the sentence and reverse each word in place.
    # "dlroW olleH" -> "World Hello"

    start = 0
    end = 0

    while True:

        # find the  start index of a word while skipping spaces.
        while start < len(sentence) and sentence[start] == ' ':
            start += 1

        if start == str_len:
            break

    # find the end index of the word.
        end = start + 1
        while end < str_len and sentence[end] != ' ' and sentence[end] != '\0':
            end += 1

    # let's reverse the word in-place.
        sentence = str_rev(sentence, start, end - 1)
        start = end
    return sentence


# 9. How many ways can you make change with coins and a total amount
def solve_coin_change(denominations, amount):
    solution = [0] * (amount + 1)
    solution[0] = 1
    for den in denominations:
        for i in range(den, amount + 1):
            solution[i] += solution[i - den]

    return solution[len(solution) - 1]
