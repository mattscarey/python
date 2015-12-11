<h1>Python Files</h1>
<h5>This is where I will keep my python files and libraries that I make.</h5>
<br/>
<h3>Binary Search Tree</h3>
<h6>BinarySearchTree.py</h6>
<p>Binary search trees are a great way to store data that needs to by searched through many times. While searching through a standard list as a data model, it is possible to traverse every
element before finding the target. With binary search trees, the amount of elements traversed will be closer to the log (base two) of the number of elements in the model. This happens
because at every node starting from the root, we use our (binary) comparison function to find out which way we need to continue down the tree, thus runling out half of the 
tree at each node. While the log(n) search time is not guaranteed, it will be very close. Later I will implement a new type of tree that will <i>always</i> be log(n) (AVL Trees)</p>
<b>What's in the file:</b>
<ul>
<li>BinarySearchTree Class</li>
<li>BSTNode Class</li>
<li>insert(k)</li>
<li>delete(k)</li>
<li>successor(k)</li>
<li>predecessor(k)</li>
<li>search(k)</li>
</ul>

<b>BinarySearchTree Class</b>
<p>
The binary search tree class is initialized with a function that compares two values. Ex:
less(a,b)
returns True if a is less than b.
The BinarySearchTree class can also be initialized with a root element. If nothing is put into the constructor, the less than function
will default to comparing two integers and the tree wil lbe empty.
</p>
<b>BSTNode Class</b>
<p>
The BST Node class is used to keep track of all of the nodes in the binary search tree. The search, predecessor, and successor fuctions return objects of this class. The values are easily obtained be calling node<i>.key</i>. The other instance variables:
node<i>.right</i>
node<i>.left</i>
</p>
<b>insert(k)</b>
<p>The insert fuction takes a key and returns a node representing the key in case you need it.</p>
<b>delete(k)</b>
<p>The delete function takes a key and returns the new node taking the place of the deleted node. Returns None if node was not found.</p>
<b>successor(k)</b>
<p>Successor takes a key and retruns the smallest node greater than k</p>
<b>predecesor(k)</b>
<p>Predecesor takes a key and returns the largest node smaller than k</p>
<b>search(k)</b>
<p>The best for last! Search looks through the tree for a key and returns the node representing that key if found. Will return none if key is not found in tree.</p>
<br/>
