'''
Clone a linked list with next and random pointer 
Medium Accuracy: 49.62% Submissions: 19763 Points: 4
You are given a Singly Linked List with N nodes where each node next pointing to its next node. You are also given M random pointers , where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b.

ArbitLinked List1

Example 1:

Input:
N = 4, M = 
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
Output: 1
Explanation: In this test case, there
re 4 nodes in linked list.  Among these
4 nodes,  2 nodes have arbit pointer
set, rest two nodes have arbit pointer
as NULL. Third line tells us the value
of four nodes. The fourth line gives the
information about arbitrary pointers.
The first node arbit pointer is set to
node 2.  The second node arbit pointer
is set to node 4.
Example 2:

Input:
N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
Output: 1
Explanation: In the given testcase ,
applying the method as stated in the
above example, the output will be 1.
Your Task:
The task is to complete the function copyList() which takes one argument the head of the linked list to be cloned and should return the head of the cloned linked list.
NOTE : If their is any node whose arbitrary pointer is not given then its by default null.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 100
1 <= M <= N
1 <= a, b <= 100
'''

#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
'''
def copynode(node, visited):
    if node:
        if node in visited:
            return visited[node]
        else:
            visited[node] = Node(node.data)
            return visited[node]
    return None
        

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    if not head: return head
    visited = {}
    old_node = head
    new_node = Node(old_node.data)
    visited[old_node] = new_node
    while old_node:
        new_node.arb = copynode(old_node.arb, visited)
        new_node.next = copynode(old_node.next, visited)
        new_node = new_node.next
        old_node = old_node.next
    return visited[head]
