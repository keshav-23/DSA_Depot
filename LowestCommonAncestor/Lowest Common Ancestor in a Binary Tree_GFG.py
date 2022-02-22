def lca(root, n1, n2):
    if not root:
        return None
    if root.data == n1 or root.data == n2:
        return root

    leftLCA = lca(root.left,n1,n2)
    rightLCA = lca(root.right,n1,n2)
    
    if leftLCA and rightLCA:
        return root
    if leftLCA:
        return leftLCA
    else:
        return rightLCA
