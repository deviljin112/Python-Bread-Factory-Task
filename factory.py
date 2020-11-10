class BreadFactory:
    def make_dough(self, has_water, has_flour):
        if has_water and has_flour:
            return True
        else:
            return False

    def bake_naan(self, has_dough):
        if has_dough:
            return "naan"
        return "failed"

    def run_factory(self, ingredients):
        has_water = False
        has_flour = False

        if "water" in ingredients and "flour" in ingredients:
            has_water = True
            has_flour = True

        dough = self.make_dough(has_water, has_flour)
        naan = self.bake_naan(dough)
        return naan