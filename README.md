# Introduction
### Nullnian
*This is based on personal practice about the leetcode problem solution code.*

The code is about the Leetcode_solution
The code is based on the Java and Python programming languages.
There are two branches: one for the solutions based on Python, and the other for the solutions based on Java.

# Patterns
## Arrays & Hashing
**Example:** Leetcode 1
### Hashmap  
[key,value]  
**Use:** No need to maintain array order  

**New hashmap:**  
    ``` Map<Integer, Integer> hashmap = new HashMap<Integer, Integer>(); ```  
**Find item:**   
    ``` hashmap.containsKey(key); ```  
**Add item:**  
    ``` hashmap.put(key, value); ```  
**Get value of key:**  
    ``` hashmap.get(key); ```  
  
    

## Recursion
### The Fibonacci sequence
**Example:** Leetcode 70
**Use:** f(n) = f(n-1) + f(n-2)

**Solve:** Scrolling array
    ``` p = q;
        q = r;
        r = p+q; ```

## Two Pointers, sliding window
**Example:** Leetcode 88; 283

## Stack, Queue

## Trees, backtracking, graphs

## Linked Lists
**Example:** Leetcode 21

**New list node:** 
    ```ListNode nodename = new ListNode(0);```
    
**Point:**
    ``` l1=l1.next; ```

# Summerization
1. ASCII
2. Sorting
3. Eliminating
