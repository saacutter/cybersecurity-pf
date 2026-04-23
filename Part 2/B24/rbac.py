class RBAC:
    """
    This is a class which implements a role-based (like) access control system. It supports users, groups, and
    individual permissions for each group.
    """

    def __init__(self):
        # Initialise the groups for each user
        self.groups = {}

        # Set the "guest" user's group
        self.groups["guest"] = {}

    def get_group(self, user):
        return self.groups[user]

    def set_group(self, use, group):
        return self.groups[user] = group
    
    def add_user(self, user, group=[]):
        self.groups[user] = group

    def create_resource(self, name, cur_user):
        with open(name, "w") as file:
            # Write the current user's name and group to the file
            file.write(f"{cur_user} {self.get_group(cur_user)}")
            file.write("")

            # Write some additional data to the file
            print("What data do you want inside the file? (\0 to stop)")
            while True:
                data = input()

                if data == "\0":
                    break   
                file.write(data)             

    def access_resource(self, name, cur_user):
        with open(name, "r") as file:
            # Extract the owner and group of the file
            owner, group = file.readline()

            # Read the file if the current user is the owner or part of the same group as the owner
            if cur_user == owner or self.get_group(cur_user) == group or self.get_group(cur_user) == "Administrator":
                print(file.read())
            else:
                print("You do not have permission to access that file.")

if __name__ == '__main__':
    # Create the access controller
    controller = RBAC()

    # Add some sample users to the controller
    controller.add_user("Alice", "Students")
    controller.add_user("Bob", "Students")
    controller.add_user("Charlie", "Administrator")

    cur_user = "guest"
    while True:
        # Print options available
        print(f"What would you like to do? (currently signed in as {cur_user})")
        print("1. Change role (root users only).")
        print("2. Add a new role.")
        print("3. Create a resource.")
        print("4. Access a resource.")
        print("5. Delete a resource.")
        print("5. Quit.")

        # Get the user's choice and input it
        try:
            choice = int(input())
        except:
            continue

        # Decide what to do based on the choice
        if choice == 1:
            if controller.get_group(cur_user) == "Administrator":
                group = input("Which role would you like to be? ")

                controller.set_group(cur_user, group)
            else:
                print("You need administrator privileges to perform this action.")
        elif choice == 2:
            pass
        elif choice == 3:
            # Get the name for the resource to be created
            resource_name = input("What do you want the resource to be called? ")

            # Create the resource
            controller.create_resource()
        elif choice == 4:
            pass
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

        print()