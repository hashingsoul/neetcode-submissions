# Concatenation of Array

**Difficulty:** Easy  
**Topics:** Array  
**Acceptance Rate:** 87.3%

## Problem Statement

You are given an integer array `nums` of length `n`.

Create an array `ans` of length `2n` such that:

- `ans[i] = nums[i]`
- `ans[i + n] = nums[i]`

for every `0 <= i < n`.

In simple terms, return an array that contains the original array **twice**.

---

## Examples

### Example 1

**Input**
```text
nums = [1,4,1,2]
```

**Output**
```text
[1,4,1,2,1,4,1,2]
```

---

### Example 2

**Input**
```text
nums = [22,21,20,1]
```

**Output**
```text
[22,21,20,1,22,21,20,1]
```

---

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

---

# Approach

The task is straightforward:

1. Create an empty array `ans`.
2. Traverse the input array.
3. Append each element to `ans`.
4. Traverse the array again.
5. Append each element once more.
6. Return `ans`.

Alternatively, most programming languages provide an easy way to concatenate arrays directly.

---

# Algorithm

1. Initialize an empty array `ans`.
2. Loop through `nums` and append every element to `ans`.
3. Loop through `nums` again and append every element.
4. Return `ans`.

---

# Dry Run

### Input

```text
nums = [1,4,1,2]
```

### Step-by-Step

| Step | ans |
|------|-----|
| Start | [] |
| Add 1 | [1] |
| Add 4 | [1,4] |
| Add 1 | [1,4,1] |
| Add 2 | [1,4,1,2] |
| Add 1 | [1,4,1,2,1] |
| Add 4 | [1,4,1,2,1,4] |
| Add 1 | [1,4,1,2,1,4,1] |
| Add 2 | [1,4,1,2,1,4,1,2] |

### Output

```text
[1,4,1,2,1,4,1,2]
```

---

# Python Solution

```python
class Solution:
    def getConcatenation(self, nums):
        ans = []

        for num in nums:
            ans.append(num)

        for num in nums:
            ans.append(num)

        return ans
```

---

# Optimized Python Solution

Python allows list concatenation using the `+` operator.

```python
class Solution:
    def getConcatenation(self, nums):
        return nums + nums
```

---

# Complexity Analysis

### Time Complexity

```
O(n)
```

We traverse the array once (or twice), where `n` is the length of `nums`.

### Space Complexity

```
O(n)
```

A new array of size `2n` is created.

---

# Key Takeaways

- Simple array manipulation problem.
- Understand how array concatenation works.
- Many languages provide built-in concatenation operators.
- Great beginner problem for practicing arrays.

---

# Tags

- Array
- Simulation
- Beginner
