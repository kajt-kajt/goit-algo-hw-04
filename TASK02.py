from collections import deque

def merge_k_lists(lists:list[list[object]]):
    """
    Merge k presorted lists into a single sorted one.
    Using divide and conquer approach: merge pairs of lists first, 
    than pairs of resulting lists and so on till only single is left in queue.
    
    :param lists: list of lists
    :type lists: list[list[object]]
    """
    q = deque()
    q.extend(lists)
    while len(q)>1:
        a = q.pop()
        b = q.pop()
        print("a=",a)
        print("b=",b)
        i, j = 0, 0
        len_a = len(a)
        len_b = len(b)
        c = []
        while len_a > i and len_b > j:
            if a[i]<b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        c.extend(a[i:])
        c.extend(b[j:])
        print("c=",c)
        q.appendleft(c)
    return q.pop()

