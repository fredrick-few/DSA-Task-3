## Repository Contents

This repository contains the programming solutions for **CCS 2214 Task 3**, implemented in Python and C. *(Theoretical derivations, expression trees, and infix-to-postfix conversion trace tables are submitted in the accompanying handwritten document.)*

| Question | File | Language | Description |
| :--- | :--- | :--- | :--- |
| **Q1** | `Question1.py` | Python | Circular Queue implementation using array wrap-around |
| **Q4(a)** | `Question4a.py` | Python | Recursive function to find the sum of the first $N$ natural numbers |
| **Q4(b)** | `Question4b.py` | Python | Recursive function to compute the factorial of a number |
| **Q4(c)** | `Question4c.py` | Python | Recursive function to find the $N^{\text{th}}$ term of a Fibonacci series |
| **Q4(d)** | `Question4d.py` | Python | Recursive program to generate $N$ terms of a Fibonacci series |
| **Q5** | `Question5.py` | Python | Linear Queue implementation supporting `enqueue` and `dequeue` |
| **Q6** | `Question6.py` | Python | Sparse matrix 3-tuple (triplet) array representation |
| **Q7** | `Question7.c` | C | Double-Ended Queue (Deque) operations: front/rear insertion & deletion |

---

## How to Run

### Python Files (`Question1.py` – `Question6.py`)
```bash
python Question1.py

gcc Question7.c -o Question7
./Question7