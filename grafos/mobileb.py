def build_tree(n, connections):
    from collections import defaultdict
    tree = defaultdict(list)
    for child, parent in connections:
        tree[parent].append(child)
    return tree

def count_pieces(tree, node, memo):
    if node in memo:
        return memo[node]
    count = 1  # count the node itself
    for child in tree[node]:
        count += count_pieces(tree, child, memo)
    memo[node] = count
    return count

def is_balanced(tree, node, memo):
    if not tree[node]:  # No children means it's balanced
        return True, None
    child_counts = set()
    for child in tree[node]:
        count = memo[child]
        child_counts.add(count)
    if len(child_counts) == 1:
        return True, next(iter(child_counts))
    return False, None

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    connections = [(int(data[i]), int(data[i + 1])) for i in range(1, len(data), 2)]
    # Build the tree from connections
    tree = build_tree(N, connections)

    # Dictionary to memoize number of pieces in each sub-móbile
    memo = {}

    # Count pieces in each sub-móbile
    for node in tree:
        count_pieces(tree, node, memo)

    # Check balance for the root piece (0)
    is_bal, _ = is_balanced(tree, 0, memo)

    # Output result
    if is_bal:
        print("bem")
    else:
        print("mal")

if __name__ == "__main__":
    main()