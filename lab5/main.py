from collections import defaultdict
import copy

class CFG:
    def __init__(self):
        self.productions = defaultdict(set)
        self.start = 'S'

    def add(self, left, right):
        self.productions[left].add(tuple(right))

    def print(self, title):
        print(f"\n=== {title} ===")
        for left in self.productions:
            for right in self.productions[left]:
                print(f"{left} -> {''.join(right)}")


# ---------------- STEP 1: Remove ε-productions ---------------- #

def remove_epsilon(cfg):
    nullable = set()

    # Find nullable variables
    changed = True
    while changed:
        changed = False
        for A in cfg.productions:
            for prod in cfg.productions[A]:
                if prod == ('ε',) or all(symbol in nullable for symbol in prod):
                    if A not in nullable:
                        nullable.add(A)
                        changed = True

    new_cfg = CFG()

    for A in cfg.productions:
        for prod in cfg.productions[A]:
            subsets = [[]]

            for symbol in prod:
                if symbol in nullable:
                    subsets = [s + [symbol] for s in subsets] + [s[:] for s in subsets]
                else:
                    subsets = [s + [symbol] for s in subsets]

            for s in subsets:
                if s:
                    new_cfg.add(A, s)

    return new_cfg


# ---------------- STEP 2: Remove Unit Productions ---------------- #

def remove_unit(cfg):
    new_cfg = CFG()

    for A in cfg.productions:
        stack = [A]
        visited = set()

        while stack:
            B = stack.pop()
            for prod in cfg.productions[B]:
                if len(prod) == 1 and prod[0].isupper():
                    if prod[0] not in visited:
                        visited.add(prod[0])
                        stack.append(prod[0])
                else:
                    new_cfg.add(A, prod)

    return new_cfg


# ---------------- STEP 3: Remove Non-Productive ---------------- #

def remove_non_productive(cfg):
    productive = set()

    # Step 1: direct terminals
    changed = True
    while changed:
        changed = False
        for A in cfg.productions:
            for prod in cfg.productions[A]:
                if all(symbol.islower() for symbol in prod):
                    if A not in productive:
                        productive.add(A)
                        changed = True
                elif all(symbol in productive for symbol in prod if symbol.isupper()):
                    if A not in productive:
                        productive.add(A)
                        changed = True

    new_cfg = CFG()
    for A in productive:
        for prod in cfg.productions[A]:
            if all(not symbol.isupper() or symbol in productive for symbol in prod):
                new_cfg.add(A, prod)

    return new_cfg


# ---------------- STEP 4: Remove Inaccessible ---------------- #

def remove_inaccessible(cfg):
    reachable = set([cfg.start])

    changed = True
    while changed:
        changed = False
        for A in list(reachable):
            for prod in cfg.productions[A]:
                for symbol in prod:
                    if symbol.isupper() and symbol not in reachable:
                        reachable.add(symbol)
                        changed = True

    new_cfg = CFG()
    for A in reachable:
        for prod in cfg.productions[A]:
            new_cfg.add(A, prod)

    return new_cfg


# ---------------- STEP 5: Convert to CNF ---------------- #

def to_cnf(cfg):
    new_cfg = CFG()
    new_var_count = 0
    terminal_map = {}

    def new_var():
        nonlocal new_var_count
        new_var_count += 1
        return f"X{new_var_count}"

    for A in cfg.productions:
        for prod in cfg.productions[A]:

            # Replace terminals in long rules
            new_prod = []
            for symbol in prod:
                if symbol.islower() and len(prod) > 1:
                    if symbol not in terminal_map:
                        v = new_var()
                        terminal_map[symbol] = v
                        new_cfg.add(v, [symbol])
                    new_prod.append(terminal_map[symbol])
                else:
                    new_prod.append(symbol)

            # Break long rules into binary
            while len(new_prod) > 2:
                v = new_var()
                new_cfg.add(v, new_prod[:2])
                new_prod = [v] + new_prod[2:]

            new_cfg.add(A, new_prod)

    return new_cfg


# ---------------- MAIN ---------------- #

cfg = CFG()

# Variant 1 grammar
cfg.add('S', ['a', 'B'])
cfg.add('S', ['A', 'C'])
cfg.add('A', ['a'])
cfg.add('A', ['A', 'S', 'C'])
cfg.add('A', ['B', 'C'])
cfg.add('A', ['a', 'D'])
cfg.add('B', ['b'])
cfg.add('B', ['b', 'S'])
cfg.add('C', ['ε'])
cfg.add('C', ['B', 'A'])
cfg.add('E', ['a', 'B'])
cfg.add('D', ['a', 'b', 'C'])

cfg.print("Original")

cfg = remove_epsilon(cfg)
cfg.print("After ε removal")

cfg = remove_unit(cfg)
cfg.print("After unit removal")

cfg = remove_non_productive(cfg)
cfg.print("After removing non-productive")

cfg = remove_inaccessible(cfg)
cfg.print("After removing inaccessible")

cfg = to_cnf(cfg)
cfg.print("Final CNF")