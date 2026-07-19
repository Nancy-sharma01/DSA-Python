# Day 27 Notes - Linked List

## What is a Linked List?

A Linked List is a linear data structure where each element is called a **Node**.

Each node contains:

- `val` → stores the data
- `next` → stores the reference to the next node

Example:

1 → 2 → 3 → None

---

## Node Structure

```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Head

- `head` points to the first node of the linked list.
- It is **not** a built-in keyword.
- It is simply a variable name.

Example:

```python
head = ListNode(10)
```

---

## Traversing a Linked List

```python
current = head

while current:
    print(current.val)
    current = current.next
```

Always move using:

```python
current = current.next
```

Otherwise, the loop becomes infinite.

---

## Fast & Slow Pointer Technique

Initialize:

```python
slow = head
fast = head
```

Move:

```python
slow = slow.next
fast = fast.next.next
```

Loop condition:

```python
while fast and fast.next:
```

Why?

Because `fast` moves two steps, so both `fast` and `fast.next` must exist.

Applications:
- Find Middle Node
- Detect Cycle
- Find nth node from the end
- Happy Number (similar concept)

---

## Deleting Duplicate Nodes

Duplicate condition:

```python
if current.val == current.next.val:
```

Delete duplicate:

```python
current.next = current.next.next
```

Do **not** move `current` immediately after deletion.

Move only when values are different:

```python
current = current.next
```

---

## Common Beginner Mistakes

❌ Treating `head` as a value.

✔ `head` is a reference to the first node.

---

❌ Forgetting to move `current`.

```python
current = current.next
```

Missing this causes an infinite loop.

---

❌ Returning the wrong thing.

Most Linked List questions require:

```python
return head
```

or

```python
return slow
```

instead of returning values.

---

## Key Takeaways

- Think in terms of **nodes and links**, not indices.
- Update pointers carefully.
- Always visualize how links change after every operation.
- Dry running pointer movement makes Linked List problems much easier.
