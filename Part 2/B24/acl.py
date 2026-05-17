class ACL:
    """
    This is a class which implements a role-based (like) access control system based on the Windows implementation.
    """

    def __init__(self):
        # Initialise the group of resources
        self.resources = {}

        # Initialise the resource owners
        self.owners = {}

    def get_owner(self, resource):
        return self.owners[resource]

    def set_owner(self, resource, cur_owner, new_owner):
        # Only the resource owner can change the owner
        if self.owners[resource] != cur_owner:
            print("You do not have permission to perform this action.")
            return
        
        # Set the new owner
        self.owners[resource] = new_owner

        # Remove the new owner from the resource's permissions if they exist
        for i in range(len(self.resources[resource])):
            if i[0] == new_owner:
                self.resources.remove(i)
    
    def add_permissions(self, resource, setting_user, user, permissions="--"):
        # Don't let the resource owner set their own permission bits (they automatically have full access)
        if self.owners[resource] == user:
            print("You cannot set your own permission bits!")
            return
        
        # The setting user must be the resource owner
        if self.owners[resource] != setting_user:
            print("You must be the resource owner to change permission bits!")
            return
    
        if (user, permissions) not in self.resources[resource]: self.resources[resource].append((user, permissions))

    def create_resource(self, name, user):
        try:
            # Create the resource
            open(name, "x").close()

            # Assign the resource to the user who initiated the command
            self.owners[name] = user
            self.resources[name] = []
        except:
            print("File name already used by another user. Please try again.")

    def access_resource(self, resource, user):
        # If the user does not have permission to read the resource, return
        if not self.has_permissions(resource, user, "r"):
            print("You don't have permission to read this file!")
            return

        # Read the resource
        with open(resource, "r") as file:
            print(file.read())

    def write_resource(self, resource, data, user):
        # If the user does not have permission to write the resource, return
        if not self.has_permissions(resource, user, "w"):
            print("You don't have permission to write to this file!")
            return
        
        # Write the data to the resource
        with open(resource, "a") as file:
            file.write(data)

    def has_permissions(self, resource, user, permission):
        # Check that the resource is valid
        if resource not in self.resources:
            return False

        # The resource owner always has all permissions
        if self.owners[resource] == user:
            return True

        # If the user does not have permission, 
        for u, p in self.resources[resource]:
            if u == user and permission in p:
                return True
        
        return False
        


if __name__ == '__main__':
    # Create the access controller
    controller = ACL()

    cur_user = "alice"
    while True:
        # Print options available
        print(f"What would you like to do? (currently signed in as {cur_user})")
        print("1. Sign in as another user.")
        print("2. Create a resource.")
        print("3. Access a resource.")
        print("4. Write to a resource.")
        print("5. Set a resource's permissions.")
        print("6. Change a resource's owner.")
        print("7. Quit.")

        # Get the user's choice
        choice = input()

        # Decide what to do based on the choice
        if choice == "1":
            cur_user = input("Who do you want to sign in as? ")
        elif choice == "2":
            name = input("What should the resource be called? ")
            controller.create_resource(name, cur_user)
        elif choice == "3":
            name = input("What resource do you want to access? ")
            controller.access_resource(name, cur_user)
        elif choice == "4":
            name = input("What resource do you want to access? ")
            data = input("What do you want to write to the resource? ")
            controller.write_resource(name, data, cur_user)
        elif choice == "5":
            name = input("What resource do you want to access? ")
            user = input("What user do you want to adjust the permissions for? ")
            permissions = input("What permissions should the user have? (r-/w-/rw/--) ")
            controller.add_permissions(name, cur_user, user, permissions)
        elif choice == "6":
            name = input("What resource do you want to access? ")
            user = input("What user do you want to be the resource owner? ")
            controller.set_owner(name, cur_user, user)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

        print()