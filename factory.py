# Creates a class BreadFactory
class BreadFactory:
    # Function for checking if user can make dough
    def make_dough(self, has_water, has_flour):
        if has_water and has_flour:
            # Returns True if user has BOTH water and flour
            return True
        else:
            return False

    # Function for checking if user can bake a naan bread
    def bake_naan(self, has_dough):
        if has_dough:
            # Returns string "naan" if user already made dough
            return "naan"
        return "failed"

    # Main function for running the whole factory
    # Input is a list of all ingredients available
    def run_factory(self, ingredients):
        # Sets local variables for future use
        has_water = False
        has_flour = False

        # If water and flour is in the ingredients list then set variables to true
        if "water" in ingredients and "flour" in ingredients:
            has_water = True
            has_flour = True

        # Check if user can make dough
        dough = self.make_dough(has_water, has_flour)
        # Check if user can make a naan bread
        naan = self.bake_naan(dough)
        # Return the result of previous function (either "naan" or "failed")
        return naan