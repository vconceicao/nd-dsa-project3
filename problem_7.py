class RouteTrieNode:

    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler=None):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode(handler)
            


    def __repr__(self):
        return "{} handler: {}".format(self.children, self.handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root_node = RouteTrieNode(handler)
        

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        index = 0
        current_node = self.root_node
        while index < len(path_list):
            char = path_list[index]
            current_node.insert(char) 

            index+=1
            current_node = current_node.children[char]
        
        current_node.handler= handler
 

        
    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        cur_node = self.root_node
        if len(path_list)==1 and path_list[0]=='':
            return cur_node.handler

        index = 0
        while index < len(path_list):
            char = path_list[index]
            if char not in cur_node.children:
                return None

            index+=1
            cur_node = cur_node.children[char]
        
        return cur_node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_message=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_manager = RouteTrie(handler) 
        self.not_found_message = not_found_message

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route_manager.insert(path_list, handler)

        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        splitted_path = self.split_path(path)
        handler = self.route_manager.find(splitted_path)
        if handler is None:
            return self.not_found_message
        else:
            return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path.endswith('/'):
            path= path[:len(path)-1]

        splitted = path.split("/")
        
        return splitted

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one