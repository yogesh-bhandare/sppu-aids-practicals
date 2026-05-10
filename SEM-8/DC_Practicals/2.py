# client
import Pyro4

# Get the server object using its URI
uri = input("Enter the server URI : ")
string_concatenator = Pyro4.Proxy(uri)

# Get inputs string from the user
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

# Call the remote method on the server
result = string_concatenator.concatenate(str1, str2)

print("Concatenated String : ", result)

# server
import Pyro4


@Pyro4.expose
class StringConcatenator(object):
    def concatenate(self, str1, str2):
        return str1 + " " + str2


# Register the StringConcatenator class as a Pyro Object
daemon = Pyro4.Daemon()
uri = daemon.register(StringConcatenator)

print("Server URI : ", uri)

# Start the server
daemon.requestLoop()
