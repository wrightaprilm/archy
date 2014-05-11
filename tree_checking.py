tree_list = dendropy.TreeList()
tree_list.read_from_path(tree_file, 'nexus')

def find_ifroot():
for tree in tree_list:
    node = tree.find_node_with_taxon_label(taxon)
    print node.parent_node

def rooted():
for tree in tree_list:
    if tree.is_rooted == True:
        print 'yes'
