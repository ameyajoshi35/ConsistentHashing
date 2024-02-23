# storage_nodes holding instances of actual storage node objects
from storage_node import StorageNode

storage_nodes = [
    StorageNode(name='A', host='239.67.52.72'),
    StorageNode(name='B', host='137.70.131.229'),
    StorageNode(name='C', host='98.5.87.182'),
    StorageNode(name='D', host='11.225.158.95'),
    StorageNode(name='E', host='203.187.116.210'),
]


def hash_fn(key):
    """The function sums the bytes present in the `key` and then
    take a mod with 5. This hash function thus generates output
    in the range [0, 4].
    """
    return sum(bytearray(key.encode('utf-8'))) % 5

def upload(path):
    # we use the hash function to get the index of the storage node
    # that would hold the file
    index = hash_fn(path)

    # we get the StorageNode instance
    node = storage_nodes[index]

    # we put the file on the node and return
    return node.put_file(path)


def fetch(path):
    # we use the hash function to get the index of the storage node
    # that would hold the file
    index = hash_fn(path)

    # we get the StorageNode instance
    node = storage_nodes[index]

    # we fetch the file from the node and return
    return node.fetch_file(path)


if __name__ == '__main__':
    # Now we find where the 5 files 'f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f5.txt'
    # reside on the storage nodes.

    for file in ['f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f5.txt']:
        print(
            f"file {file} resides on node {storage_nodes[hash_fn(file)].name}")