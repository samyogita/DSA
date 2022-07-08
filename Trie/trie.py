from asyncio import FastChildWatcher
from xmlrpc.client import FastMarshaller


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
newTrie = Trie()